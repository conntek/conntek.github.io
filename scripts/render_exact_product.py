"""Exact product pages in the site's established Feature-page structure."""
import re,html,urllib.parse
E=html.escape
STATS={
 'KTH5502':[('角度输出','16 bit'),('测量范围','360°'),('输出选择','数字／增量'),('感知技术','Hall')],
 'KTH5701':[('磁场感知','XYZ'),('ADC','16 bit'),('通信','SPI / I²C'),('测量模式','多模式')],
 'KTH5702':[('感知平面','X / Y'),('角度输出','16 bit'),('供电','2.8–5.5 V'),('通信','SPI / I²C')],
 'KTH5721':[('场强感知','XYZ'),('ADC','16 bit'),('角度平面','XY / XZ / YZ'),('等级选择','AQ2 / AQ3')],
 'KTH5761':[('场强感知','XYZ'),('ADC','16 bit'),('数字接口','I²C'),('封装','DFN-8L')],
 'KTH5771':[('感知技术','3D Hall'),('输出','双路模拟'),('供电','2.8–5.5 V'),('温度','−40–85°C')],
 'KTH5772':[('数字接口','UART / I²C'),('内部ADC','16 bit'),('I²C快速模式','400 kHz'),('温度','−40–85°C')],
 'KTH5774':[('输出','数字＋双模拟'),('内部ADC','16 bit'),('I²C快速模式','400 kHz'),('温度','−40–85°C')],
 'KTH5791':[('应用','鼠标滚轮'),('旧版格数配置','24–128 格'),('旧版接口','AB / I²C'),('资料版本','2024-05')],
 'KTH7101':[('角度输出','16 bit'),('校准','ANLC'),('输出','SPI / ABZ'),('封装','SOP-8')],
 'KTH7801':[('角度输出','16 bit'),('技术','Hall'),('供电模式','3.3 / 5 V'),('封装','SOP8 / QFN16')],
 'KTM5800':[('位置字','最高30 bit'),('单周期细分','18 bit'),('输入','外部正余弦'),('输入周期数','最高4096')],
 'KTM5900':[('角度字','24 bit'),('感知技术','TMR'),('ADC采样','2 MSPS'),('安装','在轴／离轴')],
 'KTH1601':[('磁性逻辑','全极性'),('输出','CMOS推挽'),('供电','1.6–5.5 V'),('采样版本','5 / 20 Hz')],
 'KTH2502':[('磁性逻辑','双极锁存'),('供电','2.7–32 V'),('开漏灌电流','30 mA'),('Q级温度','−40–150°C')],
 'KTH462N':[('感知','二维Hall'),('逻辑','锁存'),('输出','NMOS开漏'),('供电','2.5–5.5 V')],
 'KTH468N':[('检测','三维磁场'),('逻辑','全极性'),('输出','开关量'),('封装目录','SOT-23-5L')],
 'KTM1301':[('感知','TMR'),('50Hz / 3V档','160 nA'),('输出','CMOS推挽'),('门限档','5组')],
 'KTM2802N':[('感知','AMR'),('应用','气缸检测'),('输出用途','位置事件'),('接法目录','二线／三线')],
 'KTH31xx':[('输出','比例模拟'),('灵敏度选择','6档'),('供电','3–5.5 V'),('典型带宽','30 kHz')],
 'KTAx333':[('通道','单／双通道'),('供电','1.8–5.5 V'),('典型失调','2 µV'),('输入输出','轨到轨')]
}
def param_table(body):
 match=re.search(r'(?m)^\|[^\n]*\n(?:\|[^\n]*\n)+',body)
 if not match:return ''
 rows=[]
 for line in match[0].splitlines()[2:]:
  cells=re.split(r'(?<!\\)\|',line.strip())[1:-1]
  if len(cells)==2:rows.append((cells[0].strip().replace('\\|','|'),cells[1].strip().replace('\\|','|')))
 return '<div class="c-table c-kv"><table><tbody>'+''.join('<tr><th>'+E(k)+'</th><td>'+E(v)+'</td></tr>' for k,v in rows)+'</tbody></table></div>\n\n'
def render_exact_product(api,e,copy,members,peers):
 model=e['model'];family=api.PRODUCTS[e['family']];category=api.CAT_BY_KEY[family['category']]
 lead=copy['overview'][0]
 out=api.fm(title=model+' · '+e['directory_values']['说明'],description=lead,aside=False,pageClass='c-page c-page--product catalog-product',ld={'@context':'https://schema.org','@type':'Product','name':model,'mpn':model,'description':lead,'brand':{'@type':'Brand','name':'CONNTEK 昆泰芯'},'manufacturer':api.ORG_LD,'url':api.abs_url(e['dev_route'])})
 out+=api.eyebrow(api.HOME,(api.SEC['products'],'/products/'),(category['name'],'/products/'+category['key']+'/'),(model,None))
 title={'KTH5702':'二维旋转角度 Hall 传感器','KTH2502':'高压双极锁存霍尔开关','KTH1601':'微功耗全极性霍尔开关','KTM1301':'微功耗全极性 TMR 开关','KTM5800':'高分辨率正余弦角度细分器','KTAx333':'零漂移微功耗运算放大器'}.get(model,e['directory_values']['说明'].split('·')[0])
 out+='<div class="c-product-hero"><div class="c-product-hero__text">\n\n<p class="c-kicker">'+E(model)+'</p>\n\n# '+E(title)+'\n\n<p class="c-lead">'+E(lead)+'</p>\n\n'
 out+=api.chips_block([{'label':label,'value':value} for label,value in STATS[model]])
 out+='<div class="c-actions">'
 out+=('<a class="c-btn c-btn--brand" href="#技术文档">产品手册<small>'+str(len(e['pdfs']))+'</small></a>' if e['pdfs'] and model!='KTM2802N' else '<a class="c-btn c-btn--brand" href="/contact">索取产品资料</a>')
 out+='<a class="c-btn" href="/contact">申请样品 / 咨询</a></div>\n\n'
 hero=api.icon(e['family']) or api.product_visual(e['family'])
 out+='</div><div class="c-product-hero__media"><img src="'+hero+'" alt="'+E(model)+' 产品示意"></div></div>\n\n'
 out+=api.section('产品概述')
 photo=api.IMG.get('photo/'+e['family']) or api.IMG.get('hero/'+e['family'])
 text='\n\n'.join(copy['overview'])
 if photo and e.get('family_confirmed',True):out+='<div class="c-split c-split--overview"><div class="c-split__text">\n\n'+text+'\n\n</div><div class="c-split__media c-split__media--frame"><img src="'+photo+'" alt="'+E(api.pc(e['family'])['model'])+' 系列应用示意" loading="lazy"></div></div>\n\n'
 else:out+=text+'\n\n'
 out+=api.section('核心特点')+'<div class="c-features">'
 for n,f in enumerate(copy['features'],1):out+='<div class="c-feature"><span class="c-feature__no">'+f'{n:02d}'+'</span><div><h3>'+E(f['title'])+'</h3><p>'+E(f['body'])+'</p></div></div>'
 out+='</div>\n\n'+api.section('规格参数')+'<p class="c-sec-lead">'+E(copy['selection_note'])+'</p>\n\n'+param_table(e['body'])
 apps=copy.get('applications',[])
 if apps:
  out+=api.section('典型应用')+'<div class="c-features">'
  for n,a in enumerate(apps,1):out+='<div class="c-feature"><span class="c-feature__no">'+f'{n:02d}'+'</span><div><h3>'+E(a['title'])+'</h3><p>'+E(a['body'])+'</p></div></div>'
  out+='</div>\n\n'
 out+=api.section('技术文档')
 if e['pdfs'] and model!='KTM2802N':
  out+='<div class="c-table c-docs"><table><thead><tr><th>型号</th><th>文档</th><th>资料入口</th></tr></thead><tbody>'
  for url in e['pdfs']:
   name=urllib.parse.unquote(url.split('/')[-1]);kind='应用资料' if any(x in name for x in ['AN00','Schematic','FAQ']) else '产品手册'
   out+='<tr><td class="c-mono">'+E(model)+'</td><td><span class="c-badge">'+kind+'</span></td><td><a class="c-file" href="'+E(url)+'" target="_blank" rel="noopener"><em>PDF</em>'+E(name)+'</a></td></tr>'
  out+='</tbody></table></div>\n\n'
 else:out+='<p>本型号公开手册正在补充，请联系技术支持确认完整订货规格。</p>\n\n'
 if members and family['route']==e['dev_route']:out+=api.section('型号选择')+'<div class="catalog-quicklinks">'+''.join('<a href="'+u+'">'+E(n)+'</a>' for n,u in members)+'</div>\n\n'
 if peers:
  out+=api.section('同系列产品')+'<div class="catalog-quicklinks">'+''.join('<a href="'+p['dev_route']+'">'+E(p['model'])+'</a>' for p in peers)+'</div>\n\n'
 out+=api.cta();return out
