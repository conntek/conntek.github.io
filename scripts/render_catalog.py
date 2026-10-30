"""Supplement source inventory using the site's single native model renderer."""
import copy, html, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def read(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def first_table(body):
    m=re.search(r'(?m)^\|[^\n]*\n(?:\|[^\n]*\n)+',body)
    fields={}
    if m:
        for line in m[0].splitlines()[2:]:
            cells=re.split(r'(?<!\\)\|',line.strip())[1:-1]
            if len(cells)==2:
                k,v=[re.sub(r'[*`]', '',x.strip().replace('\\|','|')) for x in cells]
                if k not in ('产品名称','型号'): fields[k]=v
    return fields

def render_catalog(api, matrices=None, foreign=None):
    entries=read('content/catalog-20261030.json')['entries']
    inventory=read('content/selector-20261030.json')['entries']
    product_copy=read('content/catalog-site-copy-20261030.json')
    exact={e['model']:e for e in entries}
    key_specs=read('content/catalog-key-specs-20261030.json')
    def new_family(slug,category,model,name,lead,icon):
        p=copy.deepcopy(api.PRODUCTS['ktax33'])
        p.update(slug=slug,category=category,kind=model,title=name,route=f'/products/{category}/{"kth468n" if slug=="kth468" else slug}',
                 intro=[lead],highlights=[],specs=[],figures=[],docs=[],videos=[],extra=[])
        api.PRODUCTS[slug]=p
        api.COPY['products'][slug]=dict(model=model,name=name,lead=lead,overview=[lead],chips=[],highlights=[],applications=[],selection_note='')
        if icon: api.IMG['hero/'+slug]=icon
        api.render_product(slug)
    new_family('kth26','switch','KTH26 系列','高压霍尔开关','宽电压磁场状态检测，提供单极与双极锁存型号。',api.icon('kth25'))
    new_family('kth468','switch','KTH468N','霍尔磁开关','磁场状态检测，采用 SOT-23-5L 封装。',api.icon('cat-switch'))
    new_family('ktp112','other','KTP112','数字温度传感器','低功耗数字温度检测，1.8～5.5 V 供电，DFN2×2-6L 封装。',api.icon('cat-other'))

    def family(m):
        if m in ('KTAx333','KTH31xx'):return {'KTAx333':'ktax33','KTH31xx':'kth31'}[m]
        if m=='KTH468N':return 'kth468'
        if m.startswith('KTH26'):return 'kth26'
        if m=='KTP112':return 'ktp112'
        if m in exact:return exact[m]['family']
        for pre,sl in [('KTH13','kth16'),('KTH16','kth16'),('KTH17','kth16'),('KTH25','kth25'),('KTH46','kth460'),('KTH55','kth55'),('KTH57','kth57'),('KTH71','kth71'),('KTH78','kth78'),('KTM13','ktm13'),('KTM28','ktm28'),('KTM58','ktm58'),('KTM59','ktm59')]:
            if m.startswith(pre):return sl
        raise ValueError(m)

    kinds={'1d-x-axis-switch':'X轴全极霍尔开关','omni-polar-switch':'全极磁开关','dual-output-unipolar-switch':'双输出单极霍尔开关','unipolar-south-switch':'南极单极霍尔开关','unipolar-north-switch':'北极单极霍尔开关','latch-switch':'双极锁存磁开关','automotive-latch-hall-switch':'高压双极锁存霍尔开关','industrial-latch-hall-switch':'高压双极锁存霍尔开关','industrial-unipolar-hall-switch':'高压单极霍尔开关','3d-omnipolar-hall-switch':'三维全极霍尔开关','2d-latched-hall-switch':'锁存霍尔开关','angle-sensor':'磁角度传感器','angle-encoder':'磁角度编码器','angle-interpolator':'正余弦角度细分器','unipolar-switch':'单极 TMR 磁开关','npn-open-drain':'NPN输出 AMR 气缸位置传感器','pnp-open-drain':'PNP输出 AMR 气缸位置传感器','digital-temperature-sensor':'数字温度传感器'}
    names={'KTH5762':'三维角度传感器','KTH5763':'三维角度传感器','KTH7111':'离轴磁角度编码器','KTH7112':'在轴磁角度编码器','KTH468N':'霍尔磁开关'}
    groups={}; models=[]
    for e in inventory:
        m=e['model']
        if m=='KTH4603X':continue
        sl=family(m);p=api.PRODUCTS[sl];d=e['directory_values']
        route=e.get('conntek_route') or p['route']+'/'+api.model_slug(m)
        # New single-product families use the same model layout at their public entry.
        if sl in ('kth468','ktp112'):route=p['route'] if sl=='ktp112' else '/products/switch/kth468n'
        api.MODEL_ROUTE_OVERRIDES[m]=route
        fields={'供电电压':d['supply_V']+' V','工作温度':d['temperature_C']+' °C','封装':d['package']}
        if '\ufffd' not in d['current_typ']:fields['典型工作电流']=d['current_typ']
        if '\ufffd' not in d['interface']:fields['输出接口']=d['interface']
        # Pins in this directory conflict with the named six-lead package.
        if m not in ('KTM2802N','KTM2802P'):fields['引脚数']=d['pins']
        if m in exact:
            rich=first_table(exact[m]['body'])
            aliases={'供电':'供电电压','供电范围':'供电电压','输出':'输出接口','输出选项':'输出接口','温度范围':'工作温度','平均电流':'典型工作电流'}
            rich={aliases.get(k,k):v for k,v in rich.items()}
            fields.update(rich)
            lead=product_copy[m]['overview'][0]
        else:
            label=names.get(m) or kinds.get(d['subcategory']) or api.pc(sl)['name']
            fields={'器件类型':label,**fields}
            lead=f'{m} 为{label}，供电范围 {d["supply_V"]} V，工作温度 {d["temperature_C"]} °C，采用 {d["package"]} 封装。'
        if m=='KTH468N':
            fields={'供电电压':d['supply_V']+' V','工作温度':d['temperature_C']+' °C','封装':d['package'],'感应维度':'选型表标注2D，产品目录标注3D；按具体订货手册确认'}
            lead='KTH468N 为霍尔磁开关，采用 SOT-23-5L 封装。供电范围 2.5～5.5 V，工作温度 −40～125 °C。'
        if m=='KTH2562L':
            fields=first_table((ROOT/'../blog/content/models/kth2562l/_index.md').read_text(encoding='utf-8'))
            fields.update({'供电电压':'3.8～60 V（推荐工作范围）','输出接口':'NMOS 开漏','工作温度':'−40～150 °C'})
            lead='KTH2562L 是宽电压数字双极锁存霍尔开关，3.8～60 V 供电，NMOS 开漏输出。提供 A/C 两档磁阈值与 ST3、SS3、TO3 三种封装，适用于转动、换向和位置状态检测。'
        # External source PDFs stay links; existing downloads are retained as well.
        docs=[copy.deepcopy(x) for x in p['docs'] if api.doc_matches(x['series'],m)]
        urls=list(dict.fromkeys((exact.get(m,{}).get('pdfs') or [])+[x['url'] for x in e['pdf_links']]))
        if m=='KTH4603':urls+= [x['url'] for x in next(x for x in inventory if x['model']=='KTH4603X')['pdf_links']]
        for url in dict.fromkeys(urls):
            en=bool(re.search(r'(?:[_/-]EN[_/.]|datasheet\.pdf$)',url,re.I))
            docs.append(dict(scene='产品手册',series=m,type='应用资料' if re.search('off-axis|AN00|Schematic|FAQ',url,re.I) else '数据手册',cn='' if en else url,en=url if en else ''))
        chips=api.model_chips(fields)
        for key in ('典型工作电流','输出形式','器件类型','引脚数','感应维度'):
            if len(chips)<4 and key in fields and key not in [x['label'] for x in chips]:chips.append(dict(label=key,value=fields[key]))
        if m in key_specs:chips=[dict(label=k,value=v) for k,v in key_specs[m]]
        override=dict(lead=lead,docs=docs,chips=chips[:4],official=exact.get(m,{}).get('meta',{}).get('official_url') or e.get('source_page') or e['selector_url'])
        groups.setdefault(sl,[]).append((m,fields,override))
        models.append(dict(model=m,route=route,family=sl,lead=lead,fields=fields,pdfs=urls))

    # Enrich native matrices with source-specific base parts, keeping every native SKU.
    matrices=matrices or {};foreign=foreign or {}
    for sl,additions in groups.items():
        original=copy.deepcopy(matrices.get(sl) or foreign.get(sl) or {'cols':['型号'],'rows':[],'grade':None,'conflicts':[]})
        cols=list(original['cols']);gi=original['grade']
        for m,fields,o in additions:
            for k in fields:
                if k not in cols:cols.append(k)
        rows=[r+['']*(len(cols)-len(r)) for r in original['rows']]
        overrides={}
        for m,fields,o in additions:
            rows=[r for r in rows if r[0]!=m]
            rows.append([m]+[fields.get(k,'') for k in cols[1:]])
            overrides[m]=o
        matrix=dict(cols=cols,rows=rows,grade=gi,conflicts=original.get('conflicts',[]),overrides=overrides)
        api.MODEL_INDEX[sl]=[]
        api.render_model_pages(sl,matrix)
        api.MODEL_INDEX[sl]=list(dict.fromkeys(api.MODEL_INDEX[sl]))

    # Native product cards share precisely the same proportions and visual treatment.
    out=api.fm(title='产品型号',description='昆泰芯传感器、编码器与信号调理产品。',aside=False,pageClass='c-page')
    out+=api.header([api.HOME,(api.SEC['products'],'/products/'),('产品型号',None)],'产品型号','磁场、角度、位置与温度检测产品。',kicker=api.BRAND)
    for cat in api.CATS:
        items=[x for x in models if api.PRODUCTS[x['family']]['category']==cat['key']]
        if not items:continue
        out+=api.section(cat['name'])
        cards=[]
        for x in items:
            m=x['model'];sl=x['family']
            media='/img/icons-web/'+m.lower()+'.webp'
            if not (ROOT/'docs/public'/media.lstrip('/')).exists():media=api.product_visual(sl)
            cards.append(api.card(x['route'],media,m,x['lead'],kicker=api.pc(sl)['model'],media_kind='icon',more='查看详情 →'))
        out+=api.grid(cards,4)
    out+=api.cta();api.write('products/catalog.md',out)
    # Native regeneration supplies the only category/series/model navigation.
    api.render_nav()
    api.render_llms()
    llms=ROOT/'docs/public/llms.txt'
    text=llms.read_text(encoding='utf-8')+'\n## 产品型号\n'+''.join(f'- [{x["model"]}]({api.abs_url(x["route"])}): {x["lead"]}\n' for x in models)
    llms.write_text(text,encoding='utf-8')
    (ROOT/'content/catalog-routes-20261030.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Native model template:',len(models),'product entries; KTH4603X is a document version of KTH4603')

if __name__=='__main__':
    import render as api
    api.main()
