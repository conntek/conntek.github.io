"""按 content/blog/_format.md 统一检查全部博客 JSON。字数一律按 Python len() 计，含空格。

用法：python scripts/blog_lint.py        只报告
退出码：有问题为 1
"""
import glob, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {'新品发布', '产品解读', '应用方案', '技术科普', '公司动态', '行业观察'}
BOILER = ['END', '往期推荐', '扫码', '关注我们', '点击上图', '阅读原文', '昆泰芯微电子科技有限公司是一家', 'sales@', '0755-']
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿■-◿]')

problems = 0


def bad(slug, msg):
    global problems
    problems += 1
    print(f'{slug:42s} {msg}')


for fn in sorted(glob.glob(os.path.join(ROOT, 'content', 'blog', '*.json'))):
    d = json.load(io.open(fn, encoding='utf-8'))
    slug = d.get('slug', os.path.basename(fn))
    body = d.get('body', '')
    if 'body_raw' not in d:
        bad(slug, '还没排版（缺 body_raw）')
        continue
    if d.get('category') not in CATS:
        bad(slug, f'category 不在六类里：{d.get("category")}')
    lead = d.get('lead', '')
    if not 60 <= len(lead) <= 100:
        bad(slug, f'lead {len(lead)} 字（要求 60~100）')
    tk = d.get('takeaways') or []
    if len(tk) != 3:
        bad(slug, f'takeaways {len(tk)} 条（要求 3）')
    for t in tk:
        if len(t) > 40:
            bad(slug, f'要点超 40 字（{len(t)}）：{t}')
    if not isinstance(d.get('removed'), list):
        bad(slug, '缺 removed 列表')
    h2 = re.findall(r'^## (.+)$', body, flags=re.M)
    h3 = re.findall(r'^### (.+)$', body, flags=re.M)
    short = len(d.get('body_raw', '')) < 1500
    if not (0 if short else 2) <= len(h2) <= (3 if short else 5):
        bad(slug, f'## 小节 {len(h2)} 个（要求 {"0~3" if short else "2~5"}）')
    for h in h2:
        if not 4 <= len(h) <= 14:
            bad(slug, f'## 标题 {len(h)} 字：{h}')
    for h in h3:
        if re.match(r'^[\d一二三四五六七八九十]+[.、．)）]', h):
            bad(slug, f'### 带序号：{h}')
        if not 4 <= len(h) <= 16:
            bad(slug, f'### 标题 {len(h)} 字：{h}')
    if re.search(r'^#{1}\s|^#{4,}\s', body, flags=re.M):
        bad(slug, '出现一级或四级以下标题')
    if '**' in body or re.search(r'(?<![*\w])_[^_\n]+_(?!\w)', body):
        bad(slug, '正文有加粗/斜体')
    if EMOJI.search(body):
        bad(slug, f'有 emoji/装饰符号：{EMOJI.search(body).group(0)!r}')
    for w in BOILER:
        if w in body:
            bad(slug, f'残留公众号尾巴：{w}')
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', body):
        cap, src = m.group(1), m.group(2)
        line = body[body.rfind('\n', 0, m.start()) + 1: body.find('\n', m.end()) if body.find('\n', m.end()) >= 0 else len(body)]
        if line.strip() != m.group(0):
            bad(slug, f'图片没有独占一行：{src}')
        if not 6 <= len(cap) <= 24:
            bad(slug, f'图注 {len(cap)} 字：「{cap}」 {src}')
        if not os.path.exists(os.path.join(ROOT, 'docs', 'public', src.lstrip('/'))):
            bad(slug, f'图片文件不存在：{src}')
    if d.get('hero') and not os.path.exists(os.path.join(ROOT, 'docs', 'public', d['hero'].lstrip('/'))):
        bad(slug, f'hero 文件不存在：{d["hero"]}')
    # 文字规范（抽样型检查，只报明显的）
    for pat, msg in [(r'[一-鿿][A-Za-z0-9]', '中文后紧跟英文/数字没加空格'),
                     (r'[A-Za-z0-9][一-鿿]', '英文/数字后紧跟中文没加空格'),
                     (r'\d(?:RPM|rpm|Rpm)\b', '转速单位前缺空格或大小写不统一'),
                     (r'\bRPM\b', '转速单位应为小写 rpm'),
                     (r'\d\s?[uµ]s\b', '微秒应写 μs'),
                     (r'\d(?:μs|mV|mA|μA|nA|kHz|Hz|bit|V)\b', '数字与单位之间缺空格'),
                     (r'\d\s+°', '° 与数字之间不应有空格'),
                     (r'\d\s*[-－—至到]\s*\d+\s*(?:℃|°C|V|mA|Hz)', '范围应写成 a ~ b')]:
        hits = [m.group(0) for m in re.finditer(pat, re.sub(r'!\[[^\]]*\]\([^)]*\)|`[^`]*`', '', body))]
        # 型号内部（KTH7801、KTM13xx 等）不算
        hits = [h for h in hits if not re.search(r'KT[A-Z]', h)]
        if hits:
            bad(slug, f'{msg}：{len(hits)} 处，如 {hits[:3]}')

print('问题', problems)
sys.exit(1 if problems else 0)
