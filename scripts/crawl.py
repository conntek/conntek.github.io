import re, os, time, urllib.parse, urllib.request, json, hashlib
from bs4 import BeautifulSoup
BASE='https://www.conntek.com.cn'
OUT='html'; os.makedirs(OUT, exist_ok=True)
seen=set(); q=['/']; pages={}; assets=set()
def norm(u, cur):
    u=urllib.parse.urljoin(BASE+cur, u.strip())
    p=urllib.parse.urlparse(u)
    if p.netloc not in ('www.conntek.com.cn','conntek.com.cn'): return None
    path=p.path or '/'
    if re.search(r'\.(css|js|ico|png|jpe?g|gif|svg|webp|pdf|zip|rar|docx?|xlsx?|mp4)$', path, re.I):
        assets.add(p._replace(fragment='').geturl()); return None
    return path + (('?'+p.query) if p.query else '')
def fetch(path):
    req=urllib.request.Request(BASE+path, headers={'User-Agent':'Mozilla/5.0'})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode('utf-8','replace')
        except Exception as e: err=e; time.sleep(1)
    print('FAIL', path, err); return None
while q:
    path=q.pop(0)
    if path in seen: continue
    seen.add(path)
    h=fetch(path)
    if h is None: continue
    fn=OUT+'/'+hashlib.md5(path.encode()).hexdigest()+'.html'
    open(fn,'w',encoding='utf-8').write(h); pages[path]=fn
    s=BeautifulSoup(h,'html.parser')
    for tag,attr in (('a','href'),('img','src'),('iframe','src')):
        for t in s.find_all(tag):
            v=t.get(attr) or t.get('data-src') or t.get('data-original')
            if not v or v.startswith(('javascript','mailto','tel','#')): continue
            n=norm(v, path)
            if n and n not in seen: q.append(n)
    print(len(pages), path, flush=True)
json.dump({'pages':pages,'assets':sorted(assets)}, open('index.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
