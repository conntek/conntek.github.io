"""用无头 Edge（经 Chrome DevTools Protocol 驱动）给本地站点截整页图，供排版检查用。

用法：python scripts/shot.py <输出目录> <路径>[:名字] ... [--mobile] [--dark|--light] [--full|--viewport]
例：  python scripts/shot.py C:/tmp/ss products/encoder/kth78:kth78 products/:products --mobile --light

  --mobile    390px 宽、mobile=true、deviceScaleFactor=2（真正的 390 布局，不受无头窗口最小宽度限制）
  --dark      强制暗色（prefers-color-scheme=dark + localStorage vitepress-theme-appearance=dark）
  --light     强制亮色（同上，light）；两者都不给时跟随系统
  --full      截整页高度（默认）；--viewport 只截首屏
输出文件名：<名字>[-m][-dark|-light].png，每张打印一行路径；页面横向溢出时额外打印 WARN。
站点地址默认 http://127.0.0.1:5174/msite/，可用环境变量 SHOT_BASE 覆盖。
只用标准库（内置极简 websocket 客户端），无需安装依赖。
"""
import base64, json, os, shutil, socket, struct, subprocess, sys, tempfile, time, urllib.parse, urllib.request

EDGE = os.environ.get('SHOT_EDGE', r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
BASE = os.environ.get('SHOT_BASE', 'http://127.0.0.1:5174/msite/')
MAX_PX = 16000          # 输出图最大像素高度（超过则按比例缩小，不截断）
SETTLE = 1.5            # load 之后额外等待秒数

_opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))


# ---------------- 极简 websocket 客户端（RFC 6455，文本帧，无扩展） ----------------
class WS:
    def __init__(self, url, timeout=60):
        u = urllib.parse.urlparse(url)
        self.sock = socket.create_connection((u.hostname, u.port or 80), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        path = u.path + ('?' + u.query if u.query else '')
        req = (f'GET {path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\n'
               f'Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n')
        self.sock.sendall(req.encode())
        self.buf = b''
        while b'\r\n\r\n' not in self.buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError('websocket handshake: connection closed')
            self.buf += chunk
        head, self.buf = self.buf.split(b'\r\n\r\n', 1)
        if b' 101 ' not in head.split(b'\r\n', 1)[0]:
            raise ConnectionError('websocket handshake failed: ' + head.decode(errors='replace'))

    def _read(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(max(65536, n - len(self.buf)))
            if not chunk:
                raise ConnectionError('websocket closed')
            self.buf += chunk
        data, self.buf = self.buf[:n], self.buf[n:]
        return data

    def send(self, text):
        payload = text.encode()
        n = len(payload)
        hdr = bytearray([0x81])
        if n < 126:
            hdr.append(0x80 | n)
        elif n < 65536:
            hdr.append(0x80 | 126); hdr += struct.pack('>H', n)
        else:
            hdr.append(0x80 | 127); hdr += struct.pack('>Q', n)
        mask = os.urandom(4)
        hdr += mask
        masked = bytes(b ^ mask[i & 3] for i, b in enumerate(payload))
        self.sock.sendall(bytes(hdr) + masked)

    def recv(self):
        parts = []
        while True:
            b1, b2 = self._read(2)
            fin, op = b1 & 0x80, b1 & 0x0F
            n = b2 & 0x7F
            if n == 126:
                n = struct.unpack('>H', self._read(2))[0]
            elif n == 127:
                n = struct.unpack('>Q', self._read(8))[0]
            mask = self._read(4) if b2 & 0x80 else None
            data = self._read(n)
            if mask:
                data = bytes(b ^ mask[i & 3] for i, b in enumerate(data))
            if op == 0x8:
                raise ConnectionError('websocket closed by peer')
            if op == 0x9:  # ping -> pong
                data = data[:125]
                m = os.urandom(4)
                self.sock.sendall(bytes([0x8A, 0x80 | len(data)]) + m +
                                  bytes(b ^ m[i & 3] for i, b in enumerate(data)))
                continue
            if op in (0x1, 0x2, 0x0):
                parts.append(data)
                if fin:
                    return b''.join(parts).decode()

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


class CDP:
    def __init__(self, ws_url):
        self.ws = WS(ws_url)
        self.next_id = 0
        self.events = []

    def call(self, method, params=None, timeout=60):
        self.next_id += 1
        mid = self.next_id
        self.ws.send(json.dumps({'id': mid, 'method': method, 'params': params or {}}))
        end = time.time() + timeout
        while time.time() < end:
            msg = json.loads(self.ws.recv())
            if msg.get('id') == mid:
                if 'error' in msg:
                    raise RuntimeError(f'{method}: {msg["error"]}')
                return msg.get('result', {})
            if 'method' in msg:
                self.events.append(msg)
        raise TimeoutError(method)

    def wait_event(self, name, timeout=30):
        for i, ev in enumerate(self.events):
            if ev['method'] == name:
                return self.events.pop(i)
        end = time.time() + timeout
        self.ws.sock.settimeout(timeout)
        while time.time() < end:
            msg = json.loads(self.ws.recv())
            if msg.get('method') == name:
                return msg
        raise TimeoutError(name)

    def eval(self, expr, timeout=30):
        r = self.call('Runtime.evaluate', {'expression': expr, 'awaitPromise': True, 'returnByValue': True},
                      timeout=timeout)
        return r.get('result', {}).get('value')

    def close(self):
        self.ws.close()


# ---------------- 浏览器生命周期 ----------------
def http_json(port, path, method='GET'):
    req = urllib.request.Request(f'http://127.0.0.1:{port}{path}', method=method)
    with _opener.open(req, timeout=10) as r:
        return json.loads(r.read().decode())


def launch_edge():
    profile = tempfile.mkdtemp(prefix='conntek-shot-')
    proc = subprocess.Popen(
        [EDGE, '--headless=new', f'--user-data-dir={profile}', '--remote-debugging-port=0',
         '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--hide-scrollbars',
         '--no-proxy-server', '--disable-extensions', '--mute-audio', 'about:blank'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    port_file = os.path.join(profile, 'DevToolsActivePort')
    end = time.time() + 30
    while time.time() < end:
        if os.path.exists(port_file):
            try:
                port = int(open(port_file).read().split()[0])
                http_json(port, '/json/version')
                return proc, profile, port
            except (ValueError, IndexError, OSError):
                pass
        if proc.poll() is not None:
            break
        time.sleep(0.2)
    kill_edge(proc, profile, None)
    raise RuntimeError('Edge DevTools did not come up')


def kill_edge(proc, profile, port):
    if port:
        try:
            b = CDP(http_json(port, '/json/version')['webSocketDebuggerUrl'])
            b.ws.send(json.dumps({'id': 1, 'method': 'Browser.close'}))
            b.close()
            proc.wait(timeout=5)
        except Exception:
            pass
    if proc.poll() is None:
        subprocess.run(['taskkill', '/F', '/T', '/PID', str(proc.pid)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(10):
        try:
            shutil.rmtree(profile)
            break
        except OSError:
            time.sleep(0.3)


# ---------------- 截图 ----------------
def shoot(port, url, png, mobile, theme, full):
    width, vh, dsf = (390, 844, 2) if mobile else (int(os.environ.get('SHOT_W', 1440)), int(os.environ.get('SHOT_H', 900)), 1)
    target = http_json(port, '/json/new?about:blank', method='PUT')
    c = CDP(target['webSocketDebuggerUrl'])
    try:
        c.call('Page.enable')
        c.call('Runtime.enable')
        c.call('Emulation.setDeviceMetricsOverride',
               {'width': width, 'height': vh, 'deviceScaleFactor': dsf, 'mobile': mobile})
        if mobile:
            c.call('Emulation.setTouchEmulationEnabled', {'enabled': True, 'maxTouchPoints': 5})
        c.call('Emulation.setScrollbarsHidden', {'hidden': True})
        if theme:
            c.call('Emulation.setEmulatedMedia', {'features': [{'name': 'prefers-color-scheme', 'value': theme}]})
            c.call('Page.addScriptToEvaluateOnNewDocument', {'source':
                   f"try{{localStorage.setItem('vitepress-theme-appearance','{theme}')}}catch(e){{}}"})
        c.call('Page.navigate', {'url': url})
        c.wait_event('Page.loadEventFired', timeout=45)
        time.sleep(SETTLE)
        if full:
            # 逐屏滚动触发懒加载图片，再回到顶部
            c.eval("""(async()=>{const h=document.documentElement.scrollHeight;
                for(let y=0;y<h;y+=innerHeight){scrollTo(0,y);await new Promise(r=>setTimeout(r,80));}
                scrollTo(0,0);})()""", timeout=60)
        c.eval("""(async()=>{const t=new Promise(r=>setTimeout(r,10000));
            const imgs=Promise.all([...document.images].filter(i=>!i.complete)
              .map(i=>new Promise(r=>{i.onload=i.onerror=r})));
            await Promise.race([Promise.all([imgs,document.fonts.ready]),t]);})()""", timeout=20)
        time.sleep(0.3)
        m = c.eval("({h:Math.max(document.documentElement.scrollHeight,document.body.scrollHeight),"
                   "w:document.documentElement.scrollWidth,"
                   "dark:document.documentElement.classList.contains('dark')})")
        height = m['h'] if full else vh
        scale = min(1.0, MAX_PX / (height * dsf))
        shot = c.call('Page.captureScreenshot', {
            'format': 'png', 'captureBeyondViewport': bool(full),
            'clip': {'x': 0, 'y': 0, 'width': width, 'height': height, 'scale': scale}}, timeout=120)
        with open(png, 'wb') as f:
            f.write(base64.b64decode(shot['data']))
        notes = [f'{width}x{height}css', 'dark' if m['dark'] else 'light']
        if scale < 1:
            notes.append(f'scaled {scale:.2f} to fit {MAX_PX}px')
        print(f'{png}  ({", ".join(notes)})')
        if m['w'] > width:
            print(f'WARN horizontal overflow: scrollWidth={m["w"]} > {width}')
    finally:
        c.close()
        try:
            http_json(port, f'/json/close/{target["id"]}')
        except Exception:
            pass


def main():
    argv = sys.argv[1:]
    args = [a for a in argv if not a.startswith('--')]
    if len(args) < 2:
        print(__doc__)
        sys.exit(2)
    mobile = '--mobile' in argv
    theme = 'dark' if '--dark' in argv else ('light' if '--light' in argv else None)
    full = '--viewport' not in argv
    out = os.path.abspath(args[0])
    os.makedirs(out, exist_ok=True)
    proc, profile, port = launch_edge()
    failed = 0
    try:
        for spec in args[1:]:
            path, _, name = spec.partition(':')
            name = name or (path.strip('/').replace('/', '_') or 'home')
            name += ('-m' if mobile else '') + (f'-{theme}' if theme else '')
            png = os.path.join(out, name + '.png')
            try:
                shoot(port, BASE + path.lstrip('/'), png, mobile, theme, full)
            except Exception as e:
                failed += 1
                print(f'FAILED {png}: {e}')
    finally:
        kill_edge(proc, profile, port)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
