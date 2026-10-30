"""Render the audited public product catalog without copying PDF assets.

The content file contains preserved blog engineering notes, model-specific
edits, original image provenance, and external document URLs. This is called
after the legacy renderer so subsequent regeneration preserves the updates.
"""
import json,re,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def render_catalog(api):
 data=json.loads((ROOT/'content/catalog-20261030.json').read_text(encoding='utf-8'))
 site_copy=json.loads((ROOT/'content/catalog-site-copy-20261030.json').read_text(encoding='utf-8'))
 entries=data['entries']; routes={e['slug']:e['dev_route'] for e in entries}
 E=html.escape
 def rewrite(body):
  body=re.sub(r'\]\(/models/([^/)]+)/?\)',lambda m:']('+routes.get(m[1],'https://sensor.fans/models/'+m[1]+'/')+')',body)
  body=body.replace('](/wiki/?vendor=昆泰芯)','](/products/catalog)')
  body=re.sub(r'\]\((/wiki/[^)]+)\)',r'](https://sensor.fans\1)',body)
  return body
 def card(e):
  picture=e.get('image'); im=f'<div class="catalog-card-image"><img src="{picture["path"]}" alt="{E(e["model"])} 原厂技术图" loading="lazy"></div>' if picture else '<div class="catalog-card-placeholder"><span>IC</span><small>型号资料</small></div>'
  return f'<a class="catalog-model-card" href="{e["dev_route"]}">{im}<div><small>{E(" / ".join(e["categories"]))}</small><h3>{E(e["model"])}</h3><p>{E(e["description"])}</p><span>参数 · 应用 · 资料 →</span></div></a>'
 groups={}
 for e in entries:
  groups.setdefault(e['categories'][0],[]).append(e)
  members=[]
  family=api.PRODUCTS[e['family']]['route']
  for p in (ROOT/'docs'/family.lstrip('/')).glob('*.md'):
   route='/'+p.relative_to(ROOT/'docs').with_suffix('').as_posix()
   if p.stem in routes and route!=routes[p.stem]:continue
   if route!=e['dev_route']:members.append((p.stem.upper(),route))
  peers=[x for x in entries if x['family']==e['family'] and x is not e and x.get('family_confirmed',True)] if e.get('family_confirmed',True) else []
  from render_exact_product import render_exact_product
  api.write(e['dev_route'].lstrip('/')+'.md',render_exact_product(api,e,site_copy[e['model']],members,peers))
 overview=api.fm(title='具体型号与技术资料',description='按测量对象、输出和应用查找21个去重型号，核对条件、差异、原厂图片与PDF原始链接。',aside=False,pageClass='c-page catalog-index')
 overview+='\n<p class="c-kicker">产品选型 · MODEL CATALOG</p>\n\n# 具体型号与技术资料\n\n<p class="c-lead">先明确测什么，再比较输出与参数条件。每个型号连接工程说明、可确认的原厂技术图和数据手册原链接；系列与具体订货后缀分开阅读。</p>\n\n'
 overview+='<div class="c-stats"><div class="c-stat"><b>21</b><span>去重型号与系列入口</span></div><div class="c-stat"><b>6</b><span>测量与信号链类别</span></div><div class="c-stat"><b>PDF ↗</b><span>直接打开原始资料</span></div></div>\n\n'
 overview+='<p class="c-note">网页目录与详情存在的参数冲突已在型号页说明。未找到准确产品图或可用手册的项目保留缺口，不套用相邻型号资料。</p>\n\n'
 for name,items in groups.items():overview+='## '+name+'\n\n<div class="catalog-model-grid">'+''.join(card(e) for e in items)+'</div>\n\n'
 preview=data.get('supplementary',{}).get('KTP112',{})
 if preview:overview+='## 目录预告\n\n**KTP112**：'+preview['description']+' 尚无独立详情、可核验手册或产品图，不计入上述21个型号。\n\n'
 api.write('products/catalog.md',overview)
 # Add entry points to the current product landing, category and series pages.
 targets={'products/index.md':entries}
 for e in entries:
  p=api.PRODUCTS[e['family']]
  targets.setdefault('products/'+p['category']+'/index.md',[]).append(e)
  if p['route']!=e['dev_route'] and e.get('family_confirmed',True):targets.setdefault(p['route'].lstrip('/')+'.md',[]).append(e)
 marker='<!-- audited-model-catalog -->'
 for rel,items in targets.items():
  path=ROOT/'docs'/rel
  if not path.exists():continue
  text=path.read_text(encoding='utf-8').split(marker)[0].rstrip()
  unique=list({e['model']:e for e in items}.values())
  text+='\n\n'+marker+'\n\n## 按具体型号查资料\n\n[完整型号目录：21个去重入口](/products/catalog)\n\n<div class="catalog-quicklinks">'+''.join(f'<a href="{e["dev_route"]}">{E(e["model"])}</a>' for e in unique)+'</div>\n'
  api.write(rel,text)
 path=ROOT/'docs/.vitepress/sidebar.json';nav=json.loads(path.read_text(encoding='utf-8'))
 group={'text':'具体型号与资料','collapsed':True,'items':[{'text':'全部具体型号','link':'/products/catalog'}]+[{'text':e['model'],'link':e['dev_route']} for e in entries]}
 nav['products']=[g for g in nav['products'] if g.get('text')!='具体型号与资料'];nav['products'].insert(1,group)
 product_nav=next(n for n in nav['nav'] if n.get('activeMatch')=='^/products/')
 product_nav['items']=[g for g in product_nav['items'] if g.get('link')!='/products/catalog'];product_nav['items'].insert(1,{'text':'具体型号与技术资料','link':'/products/catalog'})
 path.write_text(json.dumps(nav,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 # Keep the existing plain text machine index useful for the new exact models.
 llms=ROOT/'docs/public/llms.txt'
 if llms.exists():
  text=llms.read_text(encoding='utf-8').split('\n## 具体型号与资料（2026-10-30）')[0]
  text+='\n## 具体型号与资料（2026-10-30）\n'+''.join(f'- [{e["model"]}]({api.abs_url(e["dev_route"])}): {e["description"]}\n' for e in entries)
  llms.write_text(text,encoding='utf-8')
 print('audited catalog:',len(entries),'unique models; PDFs remain external links')
if __name__=='__main__':
 import render as api
 render_catalog(api)
