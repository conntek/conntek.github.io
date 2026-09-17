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
    ok = 0
    for a, slug in zip(arts, SLUGS):
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
        rec = {
            'slug': slug,
            'title': d['title'] or a['title'],
            'date': d['date'] or a['date'],
            'author': d['author'],
            'source': a['href'],
            'summary': a.get('summary', ''),
            'cover': a.get('image', ''),
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
