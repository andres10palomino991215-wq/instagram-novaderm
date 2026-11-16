#!/usr/bin/env python3
"""Integration test using abstract technical fixtures, never a real brand post."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageChops


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace',required=True,help='Carpeta de pruebas; no usa el proyecto de publicaciones real')
    args=p.parse_args()
    sandbox=Path(args.workspace).resolve()/('novaderm-qa-'+uuid.uuid4().hex[:8])
    sandbox.mkdir(parents=True)
    source=Path(__file__).resolve().parents[1]
    package=sandbox/'paquete reubicado'
    shutil.copytree(source,package,ignore=shutil.ignore_patterns('__pycache__'))
    tool=package/'scripts/novaderm.py'
    results=[]
    def run(*arguments,ok=True):
        result=subprocess.run([sys.executable,str(tool),*map(str,arguments)],cwd=sandbox,
                              capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'})
        if (result.returncode==0)!=ok:
            raise AssertionError(f'{arguments[0]} unexpected exit {result.returncode}: {result.stdout} {result.stderr}')
        return result.stdout.strip()
    def record(name): results.append({'test':name,'result':'PASS'})

    run('verify-package'); record('Resources valid after relocation and from a different cwd')
    project=sandbox/'proyecto de prueba'; project.mkdir()
    job=Path(run('new','--project',project,'--topic','PRUEBA TÉCNICA — sin publicación'))
    brief=json.loads((job/'brief.json').read_text(encoding='utf-8'))
    assert brief['fecha_publicacion'] is None and brief['programar'] is False
    assert not job.name.startswith('2026-')
    record('No publication date or schedule required or created')
    run('build','--job',job,ok=False)
    copy_file=sandbox/'technical-copy.md'; copy_file.write_text('PRUEBA TÉCNICA. No es contenido de publicación.\n',encoding='utf-8')
    run('copy','--job',job,'--file',copy_file,'--mode','sequential-unavailable','--evidence','Fixture de prueba','--review','No aplicar a producción',ok=False)
    record('Build and final copy rejected before base selection')
    for idx,base in enumerate(['A','B','C']):
        im=Image.new('RGB',(600,750),(20+idx*10,25+idx*6,30+idx*2))
        ImageDraw.Draw(im).rectangle((400,500,599,749),fill=(50,60+idx*10,70))
        f=sandbox/(base+'.png'); im.save(f)
        run('option','--job',job,'--id',base,'--image',f,'--description','Abstract technical fixture '+base,
            '--source','Generated locally by self_test.py','--rights','Technical fixture, not a real photograph','--synthetic')
        if idx==1:
            run('select','--job',job,'--choice','A','--evidence','QA simulated selection',ok=False)
    record('Cannot select with fewer than three bases')
    run('option','--job',job,'--id','D','--image',sandbox/'A.png','--description','Duplicate',
        '--source','Test','--rights','Test',ok=False)
    record('Duplicate pixel bases rejected')
    run('select','--job',job,'--choice','A','--evidence','QA SIMULATED choice only; no user selection occurred')
    run('copy','--job',job,'--file',copy_file,'--mode','sequential-unavailable','--evidence','Test harness has no agent invocation',
        '--review','Technical test, not a copy or medical approval')
    layout=json.loads((job/'layout.json').read_text(encoding='utf-8'))
    layout['text']=[{'role':'title','lines':['PRUEBA TÉCNICA'],'x':90,'y':200,'size':90,'weight':400},
                    {'role':'subtitle','lines':['¿Texto editable? Sí.'],'x':90,'y':270,'size':42,'weight':600}]
    layout['protected']=[{'label':'technical empty area','x':800,'y':400,'width':200,'height':200}]
    product=job/'recursos/producto.png'
    Image.new('RGB',(100,100),'white').save(product)
    layout['product']={'file':'recursos/producto.png','x':700,'y':700,'width':180}
    (job/'layout.json').write_text(json.dumps(layout),encoding='utf-8')
    run('build','--job',job,ok=False); record('Opaque product photograph rejected')
    cutout=Image.new('RGBA',(100,100),(0,0,0,0))
    ImageDraw.Draw(cutout).ellipse((10,10,90,90),fill=(0,180,190,255)); cutout.save(product)
    run('build','--job',job)
    run('render','--job',job)
    run('check','--job',job)
    svg=job/'03_diseno/post.svg'; tree=ET.parse(svg); root=tree.getroot()
    ns={'s':'http://www.w3.org/2000/svg'}
    assert len(root.findall('s:g',ns))==9
    assert root.find('.//s:text',ns).text=='PRUEBA TÉCNICA'
    assert root.find(".//s:g[@id='08_ISOTIPO']//s:path",ns) is not None
    assert all(e.get('href','').startswith('data:') for e in root.findall('.//s:image',ns))
    record('Native editable text, nine layer groups, embedded photo, and separate vector logo')
    baseline=sandbox/'baseline.png'; shutil.copy2(job/'05_entrega/post.png',baseline)
    state=json.loads((job/'estado.json').read_text(encoding='utf-8'))
    assert (job/'05_entrega/caption.txt').read_text(encoding='utf-8')==copy_file.read_text(encoding='utf-8')
    handoff_args=['handoff','--job',job,'--status','ready_for_user','--account','grupo_novaderm',
                  '--evidence','QA SYNTHETIC evidence; no live Instagram UI', '--tab-id','QA-ONLY',
                  '--screenshot',baseline,'--content-verified']
    run(*handoff_args,ok=False)
    record('Cannot declare Instagram ready without visual and clinical records')
    png_hash=hashlib.sha256((job/'05_entrega/post.png').read_bytes()).hexdigest()
    caption_hash=hashlib.sha256((job/'05_entrega/caption.txt').read_bytes()).hexdigest()
    hashes={'png_sha256':png_hash,'caption_sha256':caption_hash}
    (job/'04_revision/revision.md').write_text('QA fixture visual check; not real clinical content',encoding='utf-8')
    (job/'04_revision/aprobacion-visual.json').write_text(json.dumps({'estado':'aprobada','responsable':'QA fixture reviewer',
            'fecha':'2026-11-16',**hashes}),encoding='utf-8')
    medical={'afirmaciones':[],'revision_profesional':{'estado':'no_aplica','observaciones':'QA abstract shapes only',**hashes}}
    (job/'04_revision/afirmaciones.json').write_text(json.dumps(medical),encoding='utf-8')
    wrong_account=handoff_args.copy(); wrong_account[wrong_account.index('grupo_novaderm')]='personal-qa'
    run(*wrong_account,ok=False)
    record('Different active Instagram account rejected')
    medical['afirmaciones']=[{'texto':'QA synthetic claim, no medical statement'}]
    (job/'04_revision/afirmaciones.json').write_text(json.dumps(medical),encoding='utf-8')
    run(*handoff_args,ok=False)
    medical['afirmaciones']=[]
    (job/'04_revision/afirmaciones.json').write_text(json.dumps(medical),encoding='utf-8')
    run(*handoff_args)
    state=json.loads((job/'estado.json').read_text(encoding='utf-8'))
    assert state['instagram']['published'] is False and state['instagram']['scheduled'] is False
    record('Ready record is version-bound and never denotes publication or scheduling')
    run('handoff','--job',job,'--status','blocked','--account','grupo_novaderm','--evidence','QA composer no longer available')
    state=json.loads((job/'estado.json').read_text(encoding='utf-8'))
    assert state['status']!='ready_for_user' and state['instagram']['status']=='blocked'
    run(*handoff_args)
    record('Loss of composer resets both workflow and Instagram ready statuses')
    root.find('.//s:text',ns).text='EDICIÓN REAL'
    nested=root.find(".//s:g[@id='08_ISOTIPO']/s:svg",ns); nested.set('x','200')
    tree.write(svg,encoding='utf-8',xml_declaration=True)
    run('render','--job',job,ok=False)
    run('render','--job',job,'--accept-edited-svg')
    run('check','--job',job)
    run(*handoff_args,ok=False)
    record('A changed native SVG invalidates prior Instagram-ready evidence and review')
    with Image.open(baseline) as a, Image.open(job/'05_entrega/post.png') as b:
        diff=ImageChops.difference(a.convert('RGB'),b.convert('RGB'))
        assert diff.crop((80,100,900,300)).getbbox(), 'Native text edit did not alter pixels'
        assert diff.crop((150,1100,650,1300)).getbbox(), 'Logo move did not alter pixels'
        assert not diff.crop((800,400,1000,600)).getbbox(), 'Protected photo pixels changed'
    record('Editing native text and moving logo changes only their rendered areas')
    report=json.loads((job/'04_revision/render-check.json').read_text(encoding='utf-8'))
    assert not report['warnings'], report['warnings']
    assert all(t['contrast']['minimum']>=4.5 for t in report['text'])
    record('Loaded embedded font, dimensions, and actual background contrast pass technical fixture')
    edited=ET.parse(svg); nested=edited.getroot().find(".//s:g[@id='08_ISOTIPO']/s:svg",ns)
    nested.set('x','850'); nested.set('y','420')
    edited.write(svg,encoding='utf-8',xml_declaration=True)
    run('render','--job',job,'--accept-edited-svg')
    report=json.loads((job/'04_revision/render-check.json').read_text(encoding='utf-8'))
    assert any('Isotipo invade zona protegida' in warning for warning in report['warnings'])
    record('Manual vector logo movement measured from rendered SVG detects protected-zone collision')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as browser_tool:
        browser=browser_tool.chromium.launch(headless=True)
        page=browser.new_page(viewport={'width':600,'height':600},device_scale_factor=1)
        logo_svg=(package/'assets/logos/isotipo-blanco.svg').read_text(encoding='utf-8')
        page.set_content('<style>html,body{margin:0;background:transparent}svg{width:600px;height:600px}</style>'+logo_svg)
        page.screenshot(path=str(sandbox/'logo-alpha.png'),omit_background=True)
        browser.close()
    with Image.open(sandbox/'logo-alpha.png') as logo:
        alpha=logo.getchannel('A')
        assert alpha.getextrema()[0]==0 and 208<=alpha.getextrema()[1]<=210
        assert alpha.getpixel((0,0))==0 and alpha.crop(alpha.getbbox()).getextrema()[0]==0
        bg=Image.new('RGB',(600,600),'#222222')
        draw=ImageDraw.Draw(bg)
        for y in range(0,600,30):
            for x in range(0,600,30):
                if (x//30+y//30)%2: draw.rectangle((x,y,x+29,y+29),fill='#888888')
        bg.paste(logo,(0,0),logo)
        bg.save(sandbox/'logo-comprobacion.png')
    record('White logo renders real alpha-zero exterior/gaps and intrinsic 82 percent opacity')
    run('select','--job',job,'--choice','B','--evidence','QA simulated change of base')
    run('build','--job',job,ok=False)
    assert not (job/'05_entrega/post.png').exists()
    assert any((job/'versiones').iterdir())
    record('New base invalidates copy/export and preserves archived versions')
    write={'scope':'Abstract integration fixtures only; no real post or medical review', 'tests':results,
           'sandbox':str(sandbox),'visual_fixture':str(baseline)}
    (sandbox/'resultados.json').write_text(json.dumps(write,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(write,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
