"""按 cache/assets.json 把图片/视频/技术文档下载到 docs/public（已存在的跳过）。"""
import json, os, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'docs', 'public')
ASSETS = json.load(open(os.path.join(ROOT, 'cache', 'assets.json'), encoding='utf-8'))


def get(item):
    local, url = item
    fn = os.path.join(PUB, local.lstrip('/'))
    if os.path.exists(fn) and os.path.getsize(fn) > 0:
        return 'skip', local
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=300) as r, open(fn + '.part', 'wb') as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
        os.replace(fn + '.part', fn)
        return 'ok', local
    except Exception as e:
        if os.path.exists(fn + '.part'):
            os.remove(fn + '.part')
        return 'fail', f'{local}: {e}'


def main():
    res = list(ThreadPoolExecutor(6).map(get, ASSETS.items()))
    for s, msg in res:
        if s == 'fail':
            print('FAIL', msg)
    print({k: sum(1 for s, _ in res if s == k) for k in ('ok', 'skip', 'fail')})


if __name__ == '__main__':
    main()
