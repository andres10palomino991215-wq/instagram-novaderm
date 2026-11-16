#!/usr/bin/env python3
"""Persistent workflow and native layered SVG authoring; never publishes."""
import argparse
import base64
import copy
import hashlib
import io
import json
import math
import re
import shutil
import sys
import unicodedata
import uuid
from datetime import date, datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image, ImageCms, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SVG = 'http://www.w3.org/2000/svg'
INK = 'http://www.inkscape.org/namespaces/inkscape'
ET.register_namespace('', SVG)
ET.register_namespace('inkscape', INK)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def job_state(args):
    job = Path(args.job).resolve()
    return job, read(job/'estado.json')


def save(job, state):
    state['updated_utc'] = now()
    write(job/'estado.json', state)


def invalidate_instagram(job, state, reason):
    state['instagram']=None
    record=job/'04_revision/instagram.json'
    if record.is_file():
        write(record,{'status':'invalidated','reason':reason,'at':now(),'published':False,'scheduled':False})


def inside(job, relative):
    result = (job/relative).resolve()
    require(result.is_relative_to(job.resolve()), 'Ruta fuera del trabajo: '+str(relative))
    return result


def slug(text):
    s = unicodedata.normalize('NFKD', text).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:55] or 'tema'


def project_path(explicit=None):
    if explicit:
        project=Path(explicit).resolve()
        require(project.is_dir(),'PROJECT_ROOT debe existir')
        return project
    for ancestor in [ROOT,*ROOT.parents]:
        candidates=[ancestor] if ancestor.name=='Grupo Novaderm' else [ancestor/'Grupo Novaderm']
        for candidate in candidates:
            if candidate.is_dir() and (candidate/'Documentación').is_dir() and (candidate/'Logos').is_dir():
                return candidate
    raise ValueError('No se detectó Grupo Novaderm; indicar --project con una carpeta persistente existente')


def cmd_paths(args):
    project=project_path(args.project)
    env_root=project/'.herramientas/novaderm-python'
    python_path=env_root/('Scripts/python.exe' if sys.platform=='win32' else 'bin/python')
    print(json.dumps({'project':str(project),'skill':str(ROOT),'runtime':str(python_path),
                      'runtime_exists':python_path.is_file(),
                      'copy_skill':str(ROOT.parent/'novaderm-copy/SKILL.md'),
                      'instagram_skill':str(ROOT.parent/'novaderm-instagram-draft/SKILL.md'),
                      'scheduling':False},ensure_ascii=False,indent=2))


def node(parent, name, attrs=None, text=None):
    el = ET.SubElement(parent, '{'+SVG+'}'+name, {k:str(v) for k,v in (attrs or {}).items()})
    if text is not None:
        el.text = text
    return el


def layer(parent, name, **attrs):
    return node(parent, 'g', {'id':name, '{'+INK+'}groupmode':'layer',
                            '{'+INK+'}label':name, **attrs})


def data_uri(path, mime):
    return 'data:'+mime+';base64,'+base64.b64encode(Path(path).read_bytes()).decode()


def finite(value, name, low=None, high=None):
    require(isinstance(value,(int,float)) and math.isfinite(value), name+' debe ser numérico finito')
    require(low is None or value>=low, name+' demasiado pequeño')
    require(high is None or value<=high, name+' demasiado grande')
    return value


def color(value):
    require(isinstance(value,str) and re.fullmatch(r'#[0-9A-Fa-f]{6}',value), 'Color requiere #RRGGBB')
    return value


def normalize_photo(source, target):
    with Image.open(source) as raw:
        img = ImageOps.exif_transpose(raw)
        icc = raw.info.get('icc_profile')
        if icc:
            img = ImageCms.profileToProfile(img, ImageCms.ImageCmsProfile(io.BytesIO(icc)),
                                           ImageCms.createProfile('sRGB'), outputMode='RGB')
        else:
            img = img.convert('RGB')
        digest = hashlib.sha256(str(img.size).encode()+img.tobytes()).hexdigest()
        profile = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
        img.save(target, icc_profile=profile)
        return digest, list(img.size), bool(icc)


def cmd_new(args):
    project = project_path(args.project)
    if args.date:
        date.fromisoformat(args.date)
    require(args.topic.strip(), 'Falta TEMA')
    prefix=args.date+'_' if args.date else ''
    job = project/'Publicaciones'/f'{prefix}{slug(args.topic)}_{uuid.uuid4().hex[:6]}'
    for directory in ['01_bases','02_copy','03_diseno','04_revision','05_entrega','recursos','versiones']:
        (job/directory).mkdir(parents=True, exist_ok=False)
    write(job/'brief.json', {'tema':args.topic, 'fecha_local':args.date, 'zona':args.timezone,
                            'fecha_publicacion':None,'programar':False,'cuenta_instagram':'grupo_novaderm',
                            'objetivo':'educar', 'publico':'personas interesadas en salud de la piel',
                            'supuestos':['objetivo y público propuestos; confirmar solo si afecta la pieza'],
                            'formato':[1080,1350], 'cta':'valoración individual', 'fuentes_clinicas':[]})
    write(job/'layout.json', {'width':1080,'height':1350,'photo_align':'xMidYMid',
                              'color_adjust':None,'contrast':None,'product':None,
                              'text':[], 'protected':[],
                              'logo':{'variant':'blanco','x':485.5,'y':1140,'width':109,'opacity':1},
                              'notes':['Fuente y geometría de logo aproximadas; ajustar al tema y base elegida.']})
    save(job, {'schema':1,'status':'awaiting_base_choice','options':[], 'selected':None,
               'copy_review':None,'instagram':None,'created_utc':now()})
    print(job)


def cmd_option(args):
    job,state=job_state(args)
    require(re.fullmatch(r'[A-Z][A-Z0-9_-]{0,15}',args.id), 'ID: A, B, C u otra etiqueta mayúscula')
    require(not any(o['id']==args.id for o in state['options']), 'ID ya existe; conserva historial y usa otro')
    source=Path(args.image).resolve()
    require(source.is_file(), 'No existe la imagen')
    folder=job/'01_bases'/args.id
    folder.mkdir()
    original=folder/('original'+source.suffix.lower())
    shutil.copy2(source,original)
    digest, size, had_icc=normalize_photo(source,folder/'base.png')
    if any(o['pixel_sha256']==digest for o in state['options']):
        (folder/'base.png').unlink()
        original.unlink()
        folder.rmdir()
        raise ValueError('Base con píxeles idénticos a otra; crea una opción visualmente distinta')
    option={'id':args.id,'file':(folder/'base.png').relative_to(job).as_posix(),
            'original':original.relative_to(job).as_posix(),'pixel_sha256':digest,
            'sha256':sha(folder/'base.png'),'size':size,'description':args.description,
            'source':args.source,'rights':args.rights,'synthetic':args.synthetic,
            'color':'converted-to-sRGB' if had_icc else 'assumed-sRGB-no-input-profile'}
    state['options'].append(option)
    save(job,state)
    print(f"{args.id}: registrada; {len(state['options'])} opciones. Debes mostrarlas y esperar elección.")


def archive(job):
    paths=[job/'03_diseno',job/'05_entrega',job/'04_revision']
    if any(any(p.iterdir()) for p in paths):
        version=job/'versiones'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'_'+uuid.uuid4().hex[:5])
        version.mkdir()
        for p in paths:
            shutil.copytree(p,version/p.name)
        for name in ['layout.json','estado.json','brief.json','02_copy']:
            src=job/name
            if src.is_dir(): shutil.copytree(src,version/name)
            elif src.exists(): shutil.copy2(src,version/name)


def cmd_select(args):
    job,state=job_state(args)
    require(len(state['options'])>=3, 'Se requieren al menos tres bases reales antes de seleccionar')
    require(args.evidence.strip(), 'Registrar elección explícita del usuario')
    choice=next((o for o in state['options'] if o['id']==args.choice),None)
    require(choice, 'Opción inexistente')
    archive(job)
    # Prevent stale exports after a new base choice; preserve the prior deliverables.
    for folder in ['03_diseno','04_revision','05_entrega']:
        for p in (job/folder).iterdir():
            require(p.is_file(), 'Subcarpeta no esperada en salida; revisar manualmente')
            p.unlink()
    state['selected']={'id':args.choice,'evidence':args.evidence,'at':now(),'sha256':choice['sha256']}
    state['copy_review']=None
    state['build']=None
    state['render']=None
    invalidate_instagram(job,state,'Nueva elección de imagen')
    state['status']='base_selected'
    save(job,state)
    print('Base elegida registrada. Ahora delegar copy mientras se prepara el diseño.')


def cmd_copy(args):
    job,state=job_state(args)
    require(state['selected'], 'No escribir copy definitivo antes de la elección')
    source=Path(args.file).resolve()
    require(source.is_file() and source.read_text(encoding='utf-8-sig').strip(), 'Copy vacío o ausente')
    target=job/'02_copy/copy.md'
    if source!=target: shutil.copy2(source,target)
    caption=target.read_text(encoding='utf-8-sig')
    (job/'02_copy/caption.txt').write_text(caption,encoding='utf-8')
    state['copy_review']={'mode':args.mode,'evidence':args.evidence,'principal_review':args.review,
                          'copy_sha256':sha(target),'caption_sha256':sha(job/'02_copy/caption.txt'),
                          'selected_sha256':state['selected']['sha256'],'at':now()}
    invalidate_instagram(job,state,'Copy revisado o modificado')
    state['build']=None
    state['render']=None
    state['status']='copy_reviewed'
    save(job,state)
    print('Copy y evaluación principal registrados; no implican aprobación médica.')


def cmd_build(args):
    job,state=job_state(args)
    require(state['selected'], 'Falta elección explícita')
    review=state.get('copy_review')
    require(review and review['selected_sha256']==state['selected']['sha256'], 'Falta copy revisado para esta base')
    require(sha(job/'02_copy/copy.md')==review['copy_sha256'], 'Copy cambió: registra revisión de nuevo')
    layout_path=Path(args.layout).resolve() if args.layout else job/'layout.json'
    layout=read(layout_path)
    w=int(finite(layout['width'],'width',320,5000)); h=int(finite(layout['height'],'height',320,5000))
    require(layout['text'] and any(b['role']=='title' and b['lines'] for b in layout['text']), 'Falta título en layout')
    selected=next(o for o in state['options'] if o['id']==state['selected']['id'])
    photo=inside(job,selected['file'])
    require(sha(photo)==state['selected']['sha256'], 'La base seleccionada fue modificada; volver a registrar elección')
    archive(job)
    for folder in ['03_diseno','04_revision','05_entrega']:
        for p in (job/folder).iterdir():
            require(p.is_file(),'Subcarpeta inesperada; revisar manualmente')
            p.unlink()
    if layout_path!=job/'layout.json': shutil.copy2(layout_path,job/'layout.json')
    resources=job/'recursos'
    font=ROOT/'assets/fonts/CormorantGaramond.ttf'
    for file in ['CormorantGaramond.ttf','OFL.txt','METADATA.pb']:
        shutil.copy2(ROOT/'assets/fonts'/file, resources/file)
    shutil.copy2(photo,resources/'base-elegida.png')
    logo_cfg=layout['logo']
    variant=logo_cfg.get('variant','blanco')
    require(variant in ['blanco','gris','color'],'Variante de logo no soportada')
    logo_file=ROOT/f'assets/logos/isotipo-{variant}.svg'
    shutil.copy2(logo_file,resources/'isotipo.svg')
    root=ET.Element('{'+SVG+'}svg', {'width':str(w),'height':str(h),'viewBox':f'0 0 {w} {h}'})
    node(root,'title',text=read(job/'brief.json')['tema'])
    node(root,'desc',text='Borrador para revisión. Capas nativas y texto editable; fuente sustituta y logo reconstruido.')
    defs=node(root,'defs')
    node(defs,'style',text="@font-face{font-family:'Cormorant Garamond';src:url('"+data_uri(font,'font/ttf')+"') format('truetype');font-weight:300 700;font-style:normal;} text{font-family:'Cormorant Garamond';}")
    photo_layer=layer(root,'01_FOTO_ORIGINAL')
    align=layout.get('photo_align','xMidYMid')
    require(align in ['xMinYMin','xMidYMin','xMaxYMin','xMinYMid','xMidYMid','xMaxYMid','xMinYMax','xMidYMax','xMaxYMax'],'photo_align inválido')
    node(photo_layer,'image',{'width':w,'height':h,'href':data_uri(photo,'image/png'),'preserveAspectRatio':align+' slice'})
    adjust=layer(root,'02_AJUSTE_COLOR')
    if layout.get('color_adjust'):
        a=layout['color_adjust']
        node(adjust,'rect',{'width':w,'height':h,'fill':color(a['color']),'opacity':finite(a['opacity'],'tinte',0,1)})
    contrast=layer(root,'03_CONTRASTE_TEXTO')
    if layout.get('contrast'):
        c=layout['contrast']; grad=node(defs,'linearGradient',{'id':'contraste','x1':'0%','y1':'0%','x2':'0%','y2':'100%'})
        for offset,key in [('0%','top'),('100%','bottom')]:
            node(grad,'stop',{'offset':offset,'stop-color':'#000000','stop-opacity':finite(c[key],key,0,1)})
        node(contrast,'rect',{'x':c.get('x',0),'y':c.get('y',0),'width':c.get('width',w),'height':c.get('height',h),'fill':'url(#contraste)'})
    product_layer=layer(root,'04_PRODUCTO')
    if layout.get('product'):
        p=layout['product']; source=inside(job,p['file'])
        with Image.open(source) as im:
            require(im.format=='PNG' and 'A' in im.getbands(),'Producto requiere PNG con alfa real')
            alpha=im.getchannel('A')
            require(alpha.getextrema()[0]==0 and alpha.getextrema()[1]>0,'Producto sin fondo transparente o completamente invisible')
            pw,ph=im.size
        pwidth=finite(p['width'],'product width',1,w)
        if source.resolve()!=(resources/'producto.png').resolve():
            shutil.copy2(source,resources/'producto.png')
        node(product_layer,'image',{'href':data_uri(source,'image/png'),'x':p['x'],'y':p['y'],'width':pwidth,'height':pwidth*ph/pw})
    role_layers={key:layer(root,name) for key,name in [('context','05_TEXTO_CONTEXTO'),('title','06_TITULO_PRINCIPAL'),('subtitle','07_SUBTITULO')]}
    for i,block in enumerate(layout['text']):
        require(block['role'] in role_layers,'role: context, title o subtitle')
        for j,line in enumerate(block['lines']):
            require(isinstance(line,str) and line.strip(), 'Línea vacía')
            size=finite(block['size'],'text size',1,500)
            x=finite(block['x'],'text x'); y=finite(block['y'],'text y')+j*finite(block.get('line_height',size),'line_height',1,600)
            anchor=block.get('anchor','start'); require(anchor in ['start','middle','end'],'anchor inválido')
            node(role_layers[block['role']],'text',{'id':f'text-{i}-{j}','x':x,'y':y,'font-size':size,
                 'font-weight':finite(block.get('weight',400),'weight',300,700),
                 'text-anchor':anchor,'fill':color(block.get('color','#FFFFFF'))},line)
    logo_layer=layer(root,'08_ISOTIPO',opacity=finite(logo_cfg.get('opacity',1),'logo opacity',0,1))
    original=ET.parse(logo_file).getroot()
    view=[float(v) for v in original.attrib['viewBox'].split()]
    lw=finite(logo_cfg['width'],'logo width',1,w)
    nested=node(logo_layer,'svg',{'x':logo_cfg['x'],'y':logo_cfg['y'],'width':lw,'height':lw*view[3]/view[2],
                                'viewBox':original.attrib['viewBox'],'preserveAspectRatio':'xMidYMid meet'})
    for child in original: nested.append(copy.deepcopy(child))
    guides=layer(root,'09_GUIAS',style='display:none')
    node(guides,'rect',{'x':80,'y':80,'width':max(0,w-160),'height':max(0,h-160),'fill':'none','stroke':'#FF00FF'})
    for rect in layout.get('protected',[]):
        node(guides,'rect',{'x':rect['x'],'y':rect['y'],'width':rect['width'],'height':rect['height'],'fill':'none','stroke':'#00FFFF'})
    svg_file=job/'03_diseno/post.svg'
    ET.ElementTree(root).write(svg_file,encoding='utf-8',xml_declaration=True)
    state['build']={'svg_sha256':sha(svg_file),'layout_sha256':sha(job/'layout.json'),
                    'copy_sha256':sha(job/'02_copy/copy.md'),'selected_sha256':sha(photo),'at':now()}
    state['render']=None
    invalidate_instagram(job,state,'Maestro reconstruido')
    state['status']='built_for_review'
    write(job/'03_diseno/procedencia.json',{'option':selected,'selection':state['selected'],'copy_review':review,
                                          'font':'Cormorant Garamond — sustituta, no verificada de marca',
                                          'logo':'Reconstrucción '+variant,'logo_layer_opacity':logo_cfg.get('opacity',1),
                                          'notes':layout.get('notes',[])})
    save(job,state)
    print(svg_file)


def fresh(job,state):
    build=state.get('build')
    require(build,'Falta build')
    for path,key in [('03_diseno/post.svg','svg_sha256'),('layout.json','layout_sha256'),('02_copy/copy.md','copy_sha256')]:
        require(sha(job/path)==build[key],path+' cambió; vuelve a build o usa un nuevo layout')


def intersects(a,b):
    return a['x']<b['x']+b['width'] and a['x']+a['width']>b['x'] and a['y']<b['y']+b['height'] and a['y']+a['height']>b['y']


def luminance(rgb):
    vals=[v/255 for v in rgb[:3]]
    linear=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in vals]
    return sum(v*w for v,w in zip(linear,[.2126,.7152,.0722]))


def contrast_stats(im,box,text_color):
    x0=max(0,math.floor(box['x'])); y0=max(0,math.floor(box['y']))
    x1=min(im.width,math.ceil(box['x']+box['width'])); y1=min(im.height,math.ceil(box['y']+box['height']))
    if x0>=x1 or y0>=y1: return None
    tc=luminance(tuple(int(text_color[i:i+2],16) for i in [1,3,5]))
    ratios=[]
    # Every pixel in the conservative text box, avoiding optimistic average sampling.
    for pixel in im.crop((x0,y0,x1,y1)).getdata():
        bg=luminance(pixel); ratios.append((max(tc,bg)+.05)/(min(tc,bg)+.05))
    ratios.sort()
    return {'minimum':round(ratios[0],2),'p10':round(ratios[int(len(ratios)*.1)],2),
            'median':round(ratios[len(ratios)//2],2),'method':'all pixels of conservative box on composited background'}


def cmd_render(args):
    from playwright.sync_api import sync_playwright
    job,state=job_state(args)
    if args.accept_edited_svg:
        require(state.get('build'),'Falta build original')
        for path,key in [('layout.json','layout_sha256'),('02_copy/copy.md','copy_sha256')]:
            require(sha(job/path)==state['build'][key],path+' cambió; requiere build')
        edited=ET.parse(job/'03_diseno/post.svg').getroot()
        require(len(edited.findall('{'+SVG+'}g'))==9 and edited.findall('.//{'+SVG+'}text'), 'Edición perdió capas/texto nativos')
        archive(job)
        state['build']['svg_sha256']=sha(job/'03_diseno/post.svg')
        state['build']['manual_svg_edit_at']=now()
        state['build']['layout_reproduces_manual_edits']=False
        save(job,state)
    fresh(job,state)
    layout=read(job/'layout.json'); w=layout['width']; h=layout['height']
    parsed=ET.parse(job/'03_diseno/post.svg').getroot()
    require(parsed.tag=='{'+SVG+'}svg','El maestro debe ser SVG nativo')
    require(parsed.attrib.get('viewBox')==f'0 0 {w} {h}','Dimensiones editadas difieren del layout')
    # Normalize namespace prefixes from external SVG editors before inline HTML parsing.
    svg=ET.tostring(parsed,encoding='unicode')
    html='<!doctype html><meta charset="utf-8"><style>html,body{margin:0;width:'+str(w)+'px;height:'+str(h)+'px;overflow:hidden}svg{display:block}</style>'+svg
    (job/'03_diseno/preview.html').write_text(html,encoding='utf-8')
    out=job/'05_entrega'
    with sync_playwright() as p:
        launch={'headless':True,'args':['--force-color-profile=srgb']}
        if args.browser: launch['executable_path']=str(Path(args.browser).resolve())
        browser=p.chromium.launch(**launch)
        try:
            page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
            page.set_content(html,wait_until='load')
            page.evaluate("async()=>{await document.fonts.load('400 80px \"Cormorant Garamond\"');await document.fonts.load('600 80px \"Cormorant Garamond\"');await document.fonts.ready;await Promise.all([...document.querySelectorAll('image')].map(e=>new Promise((resolve,reject)=>{const i=new Image();i.onload=resolve;i.onerror=reject;i.src=e.getAttribute('href')})));}")
            require(page.evaluate("[...document.fonts].some(f=>f.family.includes('Cormorant')&&f.status==='loaded')"),'Fuente embebida no cargada')
            metrics=page.evaluate("""()=>[...document.querySelectorAll('text')].map(e=>{const b=e.getBBox(), m=e.getCTM();const pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);const s=getComputedStyle(e);const c=s.fill.match(/[\\d.]+/g).slice(0,3).map(v=>Math.round(Number(v)).toString(16).padStart(2,'0')).join('');return {id:e.id,text:e.textContent,x:Math.min(...xs),y:Math.min(...ys),width:Math.max(...xs)-Math.min(...xs),height:Math.max(...ys)-Math.min(...ys),color:'#'+c,size:parseFloat(s.fontSize),role:e.parentElement.id}})""")
            logo_box=page.evaluate("""()=>{const e=document.getElementById('08_ISOTIPO');const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}}""")
            page.screenshot(path=str(out/'post.png'))
            # Hide text and logo for contrast measurement; preserve product and overlays.
            page.add_style_tag(content='text,[id="08_ISOTIPO"]{visibility:hidden!important}')
            page.screenshot(path=str(job/'04_revision/fondo-sin-texto.png'))
            version=browser.version
        finally:
            browser.close()
    with Image.open(out/'post.png') as im:
        thumb=im.convert('RGB'); thumb.thumbnail((360,round(h*360/w)))
        thumb.save(out/'miniatura-360.png')
    warnings=[]
    with Image.open(job/'04_revision/fondo-sin-texto.png') as bg:
        bg=bg.convert('RGB')
        for metric in metrics:
            metric['contrast']=contrast_stats(bg,metric,metric['color'])
            if metric['x']<0 or metric['y']<0 or metric['x']+metric['width']>w or metric['y']+metric['height']>h:
                warnings.append(metric['id']+': texto fuera del lienzo')
            if metric['size']<28: warnings.append(metric['id']+': menor de 28 px, revisar en móvil')
            threshold=3 if metric['role']=='06_TITULO_PRINCIPAL' else 4.5
            if metric['contrast'] and metric['contrast']['minimum']<threshold:
                warnings.append(metric['id']+f': mínimo de contraste menor de {threshold}:1, inspeccionar/corregir')
            for protected in layout.get('protected',[]):
                if intersects(metric,protected): warnings.append(metric['id']+': invade zona protegida '+protected.get('label',''))
    if logo_box['x']<0 or logo_box['y']<0 or logo_box['x']+logo_box['width']>w or logo_box['y']+logo_box['height']>h:
        warnings.append('Isotipo fuera del lienzo')
    for protected in layout.get('protected',[]):
        if intersects(logo_box,protected): warnings.append('Isotipo invade zona protegida '+protected.get('label',''))
    report={'browser':'Chromium '+version,'dimensions':[w,h],'text':metrics,'logo_rendered_box':logo_box,'warnings':warnings,
            'visual_review':'pending','medical_review':'pending; see afirmaciones.json','at':now()}
    write(job/'04_revision/render-check.json',report)
    shutil.copy2(job/'03_diseno/post.svg',out/'post.svg')
    shutil.copy2(job/'layout.json',out/'layout.json')
    shutil.copy2(job/'02_copy/copy.md',out/'copy.md')
    require(sha(job/'02_copy/caption.txt')==state['copy_review']['caption_sha256'],'Caption cambió; registrar copy de nuevo')
    shutil.copy2(job/'02_copy/caption.txt',out/'caption.txt')
    state['render']={'png_sha256':sha(out/'post.png'),'svg_sha256':sha(out/'post.svg'),
                     'caption_sha256':sha(out/'caption.txt'),'at':now()}
    invalidate_instagram(job,state,'Nueva exportación de imagen/caption')
    state['status']='rendered_for_review'
    save(job,state)
    print(json.dumps({'png':str(out/'post.png'),'warnings':warnings,'review':'Abrir PNG y miniatura; completar revision.md'},ensure_ascii=False))


def cmd_check(args):
    job,state=job_state(args); fresh(job,state)
    require(len(state['options'])>=3 and state['selected'], 'Faltan bases/elección')
    root=ET.parse(job/'03_diseno/post.svg').getroot()
    groups=[g.attrib.get('id') for g in root.findall('{'+SVG+'}g')]
    require(len(groups)==9 and '08_ISOTIPO' in groups,'Capas ausentes')
    require(root.findall('.//{'+SVG+'}text'),'Falta texto editable')
    require(root.find('.//{'+SVG+'}foreignObject') is None,'No se permite rasterizar texto en foreignObject')
    for image in root.findall('.//{'+SVG+'}image'):
        require(image.attrib.get('href','').startswith('data:'),'Imagen con dependencia externa')
    rendered=state.get('render'); require(rendered,'Falta render PNG')
    for path,key in [('05_entrega/post.png','png_sha256'),('05_entrega/post.svg','svg_sha256')]:
        require(sha(job/path)==rendered[key],'Exportación desactualizada: '+path)
    require(sha(job/'05_entrega/post.svg')==state['build']['svg_sha256'],'Maestro y entrega difieren')
    require(sha(job/'05_entrega/copy.md')==state['build']['copy_sha256'],'Copy de entrega desactualizado')
    require(sha(job/'05_entrega/caption.txt')==rendered['caption_sha256'],'Caption de entrega desactualizado')
    layout=read(job/'layout.json')
    with Image.open(job/'05_entrega/post.png') as im:
        require(im.size==(layout['width'],layout['height']) and im.mode in ['RGB','RGBA'],'Dimensiones/modo PNG incorrectos')
    warnings=read(job/'04_revision/render-check.json')['warnings']
    print(json.dumps({'technical':'PASS','warnings':warnings,
                      'visual_review_recorded':(job/'04_revision/revision.md').is_file(),
                      'medical_recorded':(job/'04_revision/afirmaciones.json').is_file(),
                      'note':'PASS técnico no aprueba diseño, derechos ni medicina'},ensure_ascii=False))


def cmd_handoff(args):
    """Records observed UI evidence; performs no browser operation or upload."""
    job,state=job_state(args)
    require(args.evidence.strip(),'Falta evidencia de estado observado')
    record={'status':args.status,'account':args.account.lstrip('@'),'tab_id':args.tab_id,
            'evidence':args.evidence,'at':now(),'published':False,'scheduled':False}
    if args.status=='ready_for_user':
        require(record['account']=='grupo_novaderm','La cuenta activa no coincide con Grupo Novaderm')
        require(args.content_verified,'Falta declaración de correspondencia real de imagen y caption en la UI')
        require(args.screenshot and args.tab_id,'Faltan captura real e identificador de pestaña')
        fresh(job,state)
        rendered=state.get('render')
        require(rendered,'No hay una exportación actual')
        for path,key in [('05_entrega/post.png','png_sha256'),('05_entrega/caption.txt','caption_sha256')]:
            require(sha(job/path)==rendered[key],'Archivo de entrega cambió después de render: '+path)
        visual_path=job/'04_revision/aprobacion-visual.json'
        medical_path=job/'04_revision/afirmaciones.json'
        require(visual_path.is_file() and (job/'04_revision/revision.md').is_file(),'Falta revisión visual real registrada')
        require(medical_path.is_file(),'Falta registro clínico o justificación de no aplica')
        visual=read(visual_path)
        require(visual.get('estado')=='aprobada' and visual.get('responsable') and visual.get('fecha'),'Revisión visual pendiente o incompleta')
        medical=read(medical_path)
        professional=medical.get('revision_profesional',{})
        claims=medical.get('afirmaciones',[])
        require(isinstance(claims,list),'Lista de afirmaciones inválida')
        if claims:
            require(professional.get('estado')=='aprobada' and professional.get('responsable') and professional.get('fecha'),
                    'Claims requieren aprobación profesional real con responsable y fecha')
        else:
            require(professional.get('estado') in ['no_aplica','aprobada'] and professional.get('observaciones'),
                    'Justificar ausencia de claims o registrar revisión')
        for review in [visual,professional]:
            require(review.get('png_sha256')==rendered['png_sha256'] and review.get('caption_sha256')==rendered['caption_sha256'],
                    'La revisión no corresponde a los archivos actuales')
        require(args.screenshot and Path(args.screenshot).is_file(),'Falta captura real de la previsualización')
        screenshot=job/'04_revision/instagram-previsualizacion.png'
        with Image.open(args.screenshot) as image:
            image.verify()
        if Path(args.screenshot).resolve()!=screenshot.resolve():
            with Image.open(args.screenshot) as image:
                image.save(screenshot,format='PNG')
        record.update({'png_sha256':rendered['png_sha256'],'caption_sha256':rendered['caption_sha256'],
                       'screenshot':screenshot.relative_to(job).as_posix(),'content_verified':True})
        state['status']='ready_for_user'
    elif state.get('status')=='ready_for_user':
        state['status']='rendered_for_review' if state.get('render') else 'awaiting_base_choice'
    state['instagram']=record
    write(job/'04_revision/instagram.json',record)
    save(job,state)
    print(json.dumps(record,ensure_ascii=False,indent=2))


def cmd_verify(args):
    import yaml
    skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    front=yaml.safe_load(skill.split('---',2)[1])
    require(front.get('name')=='novaderm-instagram' and front.get('description'),'Frontmatter incompleto')
    metadata=yaml.safe_load((ROOT/'agents/openai.yaml').read_text(encoding='utf-8'))
    require('$novaderm-instagram' in metadata['interface']['default_prompt'],'Invocación de UI incoherente')
    manifest=read(ROOT/'references/resource-manifest.json')
    for entry in manifest:
        file=inside(ROOT,entry['path'])
        require(file.is_file() and sha(file)==entry['sha256'],'Recurso ausente o modificado: '+entry['path'])
    for path in ['SKILL.md','agents/openai.yaml','references/motor.md','references/copy-revision.md','references/sistema-visual.md','references/procedencia.md','references/visual/contacto.jpg']:
        require((ROOT/path).is_file(),'Falta '+path)
    print(f'PASS: {len(manifest)} recursos con SHA-256 y archivos principales disponibles desde {ROOT}')


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    n=sub.add_parser('new'); n.add_argument('--project'); n.add_argument('--topic',required=True)
    n.add_argument('--date',help='Metadato opcional de creación; nunca fecha de publicación')
    n.add_argument('--timezone',default='America/Bogota'); n.set_defaults(func=cmd_new)
    for name,func in [('option',cmd_option),('select',cmd_select),('copy',cmd_copy),('build',cmd_build),('render',cmd_render),('check',cmd_check)]:
        s=sub.add_parser(name); s.add_argument('--job',required=True); s.set_defaults(func=func)
        if name=='option':
            for flag in ['id','image','description','source','rights']: s.add_argument('--'+flag,required=True)
            s.add_argument('--synthetic',action='store_true')
        if name=='select': s.add_argument('--choice',required=True); s.add_argument('--evidence',required=True)
        if name=='copy':
            s.add_argument('--file',required=True); s.add_argument('--mode',choices=['agent','sequential-unavailable'],required=True)
            s.add_argument('--evidence',required=True); s.add_argument('--review',required=True)
        if name=='build': s.add_argument('--layout')
        if name=='render':
            s.add_argument('--browser',help='Ruta opcional a Chromium/Chrome local')
            s.add_argument('--accept-edited-svg',action='store_true',help='Registrar edición nativa externa; layout no reproduce esos cambios')
    v=sub.add_parser('verify-package'); v.set_defaults(func=cmd_verify)
    paths=sub.add_parser('paths'); paths.add_argument('--project'); paths.set_defaults(func=cmd_paths)
    handoff=sub.add_parser('handoff'); handoff.add_argument('--job',required=True)
    handoff.add_argument('--status',choices=['awaiting_login','preparing','blocked','ready_for_user'],required=True)
    handoff.add_argument('--account',required=True); handoff.add_argument('--evidence',required=True)
    handoff.add_argument('--tab-id'); handoff.add_argument('--screenshot'); handoff.add_argument('--content-verified',action='store_true')
    handoff.set_defaults(func=cmd_handoff)
    return p


if __name__=='__main__':
    try:
        arguments=parser().parse_args()
        arguments.func(arguments)
    except (ValueError,KeyError,FileNotFoundError) as e:
        print('ERROR: '+str(e),file=sys.stderr)
        sys.exit(2)
