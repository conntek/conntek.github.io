"""把「技术文章」里链到的微信公众号文章下载到本地，转成博客数据。

输出：
  cache/blog/<slug>.html          原始网页（留档，可重复解析不必重下）
  docs/public/blog/<slug>/N.webp   正文图片（压缩到最长边 1600，webp q82）
  content/blog/<slug>.json         {title, date, author, source, summary, cover, body}  body 为 Markdown

用法：python scripts/blog_fetch.py [--refetch]   默认已下载过的网页不再重下
"""
import io, json, os, re, sys, time, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from markdownify import markdownify
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = json.load(io.open(os.path.join(ROOT, 'cache', 'site.json'), encoding='utf-8'))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
REFETCH = '--refetch' in sys.argv

# 按 site.json 里 techtalks 的顺序给每篇一个可读的 slug（URL 用）
SLUGS = [
    'kth78-multipole-calibration',
    'kth78-high-torque-motor',
    'kth7812-e-motorcycle',
    'kth78-accuracy-and-low-latency',
    'kth7811-bldc-drill',
    'how-to-evaluate-magnetic-encoder-accuracy',
    'kth1601-smart-trash-can',
    'kth1601-door-sensor',
    'kth1601-wireless-earbuds',
    'crc-in-kth78',
    'hall-sensor-automotive-switch',
    'kth5701-off-axis',
    'what-is-abz',
    'kth78-coreless-motor',
    'hall-effect-explained',
    'kth78-launch-wing-servo',
]


# 源站「技术文章」列表之外、王超另给的公众号文章（2026-09-18）：(slug, 原文链接)
EXTRA = [
    ('kto9348-launch-ciif-2026', 'https://mp.weixin.qq.com/s/N6ezUwoT0D_4lsOcgNrAeg'),
    ('microduck-sensor-teardown', 'https://mp.weixin.qq.com/s/L3z812seoZr7qN7-_261bA'),
    ('wrc-2026-observations', 'https://mp.weixin.qq.com/s/KaVKipwl7OFOcz926m1zbg'),
    ('kth7113-launch-dexterous-hand', 'https://mp.weixin.qq.com/s/riHabO7WWRj1_vTSF9OLBA'),
    ('3d-hall-knob-joystick-valve-encoder', 'https://mp.weixin.qq.com/s/fo3AxdP0dOwxVMYysE-JpQ'),
    ('electronica-china-2026-recap', 'https://mp.weixin.qq.com/s/LesGO8ZEh8LazjeX1zl8XQ'),
    ('physical-ai-sensing-foundation', 'https://mp.weixin.qq.com/s/VeDXCT61tYP_KSKDDTCCOw'),
    ('electronica-china-2026-day1', 'https://mp.weixin.qq.com/s?__biz=MzI5NzAxMTAyMg==&mid=2247489859&idx=1&sn=d6e9f8579967929ea1176eff66fb97dd'),
    ('ktm52-53-amr-launch', 'https://mp.weixin.qq.com/s?__biz=MzI5NzAxMTAyMg==&mid=2247489773&idx=1&sn=de5a1a71ddabeadad7f988dc76724f81&chksm=ed4233d3d5d13b4e10c32bf27fd1d8da48714c535d619e9892deaa9aa66c863d7d73e3e226b2&scene=0&xtrack=1&subscene=90'),
    ('tsinghua-industrial-design-talk', 'https://mp.weixin.qq.com/s?__biz=MzI5NzAxMTAyMg==&mid=2247489757&idx=1&sn=b1ca5f2892d8b597399ad3b67d8b7d32&chksm=ede826b1509ba26eaf101de1e8023f222b0ca7cabc7f72fd9664ebfb9dd0c1cfe43be6d464e6&scene=0&xtrack=1&subscene=90'),
    ('sensor-expo-shenzhen-2026-recap', 'https://mp.weixin.qq.com/s?__biz=MzI5NzAxMTAyMg==&mid=2247489718&idx=1&sn=95fec1af3c2dc5d3826c5267e73fc36b&chksm=ed97d29b3d17c9df92d434517d0a03593c3564223183553d9508087b345c5dcb1c393946e1c5&scene=0&xtrack=1&subscene=90'),
    ('sensor-expo-shenzhen-2026-forums', 'https://mp.weixin.qq.com/s/l4AcqziSF-fN0HAmrzRSaA'),
    ('ktm13-dishwasher-level', 'https://mp.weixin.qq.com/s/WhXOaZhHKw0PzLDQSq-_cg'),
    ('kth57-smart-irrigation-valve', 'https://mp.weixin.qq.com/s/IaBAP2516J3KxElgTpdI1A'),
    ('ktm59-gaming-peripherals', 'https://mp.weixin.qq.com/s/CHzybg4FGmyDrfM8v6CjFw'),
    ('kth1701-ab-roller', 'https://mp.weixin.qq.com/s/7prET3DnByCYZDsnWQf7Nw'),
    ('kth5701-injection-pump', 'https://mp.weixin.qq.com/s/RRaXBIyZF5v2bnanxxyqMQ'),
    ('first-european-patent', 'https://mp.weixin.qq.com/s/O4MFLkIpxcaXHixSDXEFfw'),
    ('sps-nuremberg-2025', 'https://mp.weixin.qq.com/s/tBKbqM37kcsbIwx7hbRUNQ'),
]


def get(url, binary=False, referer=None):
    req = urllib.request.Request(url, headers={'User-Agent': UA, **({'Referer': referer} if referer else {})})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
            return data if binary else data.decode('utf-8', 'replace')
        except Exception as e:
            if i == 2:
                raise
            time.sleep(2)


def save_image(url, out_dir, n):
    raw = get(url, binary=True, referer='https://mp.weixin.qq.com/')
    im = Image.open(io.BytesIO(raw))
    if getattr(im, 'is_animated', False):
        # 动图原样保存为 gif，不转 webp 以免只剩第一帧
        fn = f'{n}.gif'
        open(os.path.join(out_dir, fn), 'wb').write(raw)
        return fn, im.size
    im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
    im.thumbnail((1600, 1600))
    fn = f'{n}.webp'
    im.save(os.path.join(out_dir, fn), 'WEBP', quality=82, method=6)
    return fn, im.size


def parse(html, slug, src_url):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('#js_content')
    if content is None:
        raise RuntimeError('没有找到正文 #js_content（文章可能已删除或触发了验证）')
    title = (soup.select_one('#activity-name') or soup.find('meta', property='og:title'))
    title = title.get_text(strip=True) if hasattr(title, 'get_text') and title.get_text(strip=True) else (title.get('content') if title else '')
    author = soup.select_one('#js_name')
    author = author.get_text(strip=True) if author else ''
    m = re.search(r'var ct = "(\d+)"', html)
    date = time.strftime('%Y-%m-%d', time.localtime(int(m.group(1)))) if m else ''

    out_dir = os.path.join(ROOT, 'docs', 'public', 'blog', slug)
    os.makedirs(out_dir, exist_ok=True)
    jobs = []
    for img in content.find_all('img'):
        url = img.get('data-src') or img.get('src') or ''
        if not url.startswith('http'):
            img.decompose()
            continue
        jobs.append((len(jobs) + 1, img, url))
    from concurrent.futures import ThreadPoolExecutor
    def work(job):
        k, _, url = job
        try:
            return save_image(url, out_dir, k)
        except Exception as e:
            print('  图片下载失败', slug, k, e)
            return None
    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(work, jobs))
    n = 0
    for (k, img, _), res in zip(jobs, results):
        if not res:
            img.decompose()
            continue
        fn, (w, h) = res
        n += 1
        img.attrs = {'src': f'/blog/{slug}/{fn}', 'alt': '', 'loading': 'lazy', 'width': str(w), 'height': str(h)}
    videos = 0
    for v in content.select('iframe, mpvideosnap, mp-common-videosnap, .video_iframe, mpvoice, mp-common-mpaudio'):
        videos += 1
        note = soup.new_tag('p')
        note.string = f'（此处为视频，请在原文中观看：{src_url}）'
        v.replace_with(note)
    for t in content.find_all(['script', 'style']):
        t.decompose()
    body = markdownify(str(content), heading_style='ATX', strip=['span', 'section', 'strong_placeholder'])
    body = re.sub(r'[ \t ]+\n', '\n', body)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    return {'title': title, 'author': author, 'date': date, 'body': body, 'images': n, 'videos': videos}


def main():
    os.makedirs(os.path.join(ROOT, 'cache', 'blog'), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'content', 'blog'), exist_ok=True)
    arts = SITE['techtalks']
    assert len(arts) == len(SLUGS), (len(arts), len(SLUGS))
    items = list(zip(arts, SLUGS)) + [({'href': url}, slug) for slug, url in EXTRA]
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    if only:
        items = [(a, s) for a, s in items if s in only]
    ok = 0
    for a, slug in items:
        target = os.path.join(ROOT, 'content', 'blog', slug + '.json')
        if os.path.exists(target) and 'body_raw' in json.load(io.open(target, encoding='utf-8')) and not REFETCH:
            # 已排版过的文章不再覆盖（上一轮就是被残留进程这样冲掉的）
            print('skip (已排版)', slug)
            continue
        cache = os.path.join(ROOT, 'cache', 'blog', slug + '.html')
        if REFETCH or not os.path.exists(cache):
            html = get(a['href'])
            io.open(cache, 'w', encoding='utf-8').write(html)
            time.sleep(1.5)
        html = io.open(cache, encoding='utf-8').read()
        try:
            d = parse(html, slug, a['href'])
        except Exception as e:
            print('FAIL', slug, e)
            continue
        cover = a.get('image', '')
        if not cover:
            # 源站列表之外的文章没有封面，取公众号分享图 og:image
            m = re.search(r'property="og:image" content="([^"]+)"', html)
            if m:
                try:
                    fn, _ = save_image(m.group(1), os.path.join(ROOT, 'docs', 'public', 'blog', slug), 'cover')
                    cover = f'/blog/{slug}/{fn}'
                except Exception as e:
                    print('  封面下载失败', slug, e)
        rec = {
            'slug': slug,
            'title': d['title'] or a.get('title', ''),
            'date': d['date'] or a.get('date', ''),
            'author': d['author'],
            'source': a['href'],
            'summary': a.get('summary', ''),
            'cover': cover,
            'images': d['images'],
            'videos': d['videos'],
            'body': d['body'],
        }
        io.open(os.path.join(ROOT, 'content', 'blog', slug + '.json'), 'w', encoding='utf-8').write(
            json.dumps(rec, ensure_ascii=False, indent=1) + '\n')
        ok += 1
        print(f'ok  {rec["date"]}  {len(rec["body"]):6d} 字符  图 {d["images"]:2d}  视频 {d["videos"]}  {slug}')
    print('完成', ok, '/', len(arts))


if __name__ == '__main__':
    main()
