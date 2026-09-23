"""IndexNow：把本次更新的页面地址主动推送给 Bing（Yandex、Naver、Seznam 等同一套协议，百度不支持）。

密钥文件放在站点根目录 docs/public/<key>.txt，内容就是密钥本身（Bing 生成）。
提交后通常几小时内抓取，不必等爬虫自己发现。

用法：
  python scripts/indexnow.py --changed [基准提交]   只推本次提交改动的页面（默认 HEAD~1，部署流程用这个）
  python scripts/indexnow.py --all                 推 sitemap 里的全部地址（首次接入、或站点大改后用）
  python scripts/indexnow.py /blog/ /products/     手工指定路径
  加 --dry 只打印不提交
"""
import glob, json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'docs', 'public')
SITE = os.environ.get('SITE_URL', 'https://conntek.github.io').rstrip('/')
HOST = SITE.split('//', 1)[1]
ENDPOINT = 'https://api.indexnow.org/IndexNow'
DRY = '--dry' in sys.argv


def find_key():
    for p in sorted(glob.glob(os.path.join(PUB, '*.txt'))):
        name = os.path.basename(p)[:-4]
        if re.fullmatch(r'[0-9a-fA-F]{8,128}', name):
            body = open(p, encoding='utf-8').read().strip()
            if body == name:
                return name
            print(f'警告：{name}.txt 的内容与文件名不一致，IndexNow 会拒绝')
    return None


def md_to_url(path):
    """docs/xxx/yyy.md → https://站点/xxx/yyy（cleanUrls，index.md 去掉文件名）"""
    rel = path.replace('\\', '/')
    if not rel.startswith('docs/') or not rel.endswith('.md') or '.vitepress' in rel:
        return None
    rel = rel[len('docs/'):-len('.md')]
    if rel == 'index':
        return SITE + '/'
    if rel.endswith('/index'):
        return SITE + '/' + rel[:-len('index')]
    return SITE + '/' + rel


def changed_urls(base):
    out = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=ACMR', base, 'HEAD'],
                         cwd=ROOT, capture_output=True, text=True)
    urls = [u for u in (md_to_url(f) for f in out.stdout.split('\n') if f.strip()) if u]
    return sorted(set(urls))


def sitemap_urls():
    p = os.path.join(ROOT, 'docs', '.vitepress', 'dist', 'sitemap.xml')
    if not os.path.exists(p):
        print('没有 dist/sitemap.xml，请先 npx vitepress build docs')
        return []
    return sorted(set(re.findall(r'<loc>([^<]+)</loc>', open(p, encoding='utf-8').read())))


def submit(urls, key):
    payload = {'host': HOST, 'key': key, 'keyLocation': f'{SITE}/{key}.txt', 'urlList': urls[:10000]}
    if DRY:
        print(json.dumps(payload, ensure_ascii=False, indent=1)[:2000])
        return 0
    req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                                 headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print('IndexNow 返回', r.status, r.reason)
            return 0 if r.status in (200, 202) else 1
    except urllib.error.HTTPError as e:
        # 422 = 地址与密钥不属于同一站点；403 = 密钥文件取不到
        print('IndexNow 失败', e.code, e.reason, e.read()[:300].decode('utf-8', 'replace'))
        return 1


def main():
    key = find_key()
    if not key:
        print('没找到 IndexNow 密钥文件（docs/public/<key>.txt）')
        return 1
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--all' in sys.argv:
        urls = sitemap_urls()
    elif '--changed' in sys.argv:
        urls = changed_urls(args[0] if args else 'HEAD~1')
    else:
        urls = [a if a.startswith('http') else SITE + '/' + a.lstrip('/') for a in args]
    if not urls:
        print('本次没有需要推送的页面')
        return 0
    print(f'推送 {len(urls)} 个地址给 IndexNow（key {key[:8]}…）')
    for u in urls[:10]:
        print('  ', u)
    if len(urls) > 10:
        print(f'   … 其余 {len(urls) - 10} 个')
    return submit(urls, key)


if __name__ == '__main__':
    sys.exit(main())
