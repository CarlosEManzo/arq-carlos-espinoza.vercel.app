"""Panel DEMOS / CÓDIGO en dos pantallas como máximo, con Metric.arq al frente:
tarjeta principal con dos herramientas (instalaciones y muro de block) en pestañas, ejemplos con un toque,
y debajo «otros desarrollos» (Mr. Pasto con su demo plegable y Em Dental). Se ejecuta una sola vez sobre src/pagina.html."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")


def cambia(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:90])
    s = s.replace(a, b)


# ---- piezas existentes ----
c0 = s.index('      <div class="calc">')
c1 = s.index('    </section>\n    <section aria-labelledby="dm-t">')
calc = s[c0:c1].rstrip()
d0 = s.index('        <div class="demo" id="demo-pu">')
d1 = s.index('        <div class="demo" id="demo-ps">')
d2 = s.index('      </div>\n    </section>\n    <section aria-labelledby="ap-t">')
demo_pu = s[d0:d1].rstrip()
demo_ps = s[d1:d2].rstrip()

# muro: dos columnas en pantallas anchas (dibujo y controles a la izquierda, cifras a la derecha)
v0 = demo_pu.index('<div class="vista" data-v="probar">') + len('<div class="vista" data-v="probar">')
v1 = demo_pu.index('          </div>\n          <div class="vista" data-v="como"')
lineas = [l for l in demo_pu[v0:v1].split("\n") if l.strip()]
assert len(lineas) == 11, len(lineas)
demo_pu = demo_pu[:v0] + '\n            <div class="col-a">\n' + "\n".join(lineas[:7]) + '\n            </div>\n            <div class="col-b">\n' + "\n".join(lineas[7:]) + '\n            </div>\n' + demo_pu[v1:]
demo_pu = demo_pu.replace('<svg class="ic" aria-hidden="true"><use href="#i-muro"/></svg>Metric.arq</span>', '<svg class="ic" aria-hidden="true"><use href="#i-muro"/></svg>Costo de un muro armado</span>')

nuevo = f'''  <div class="labw">
    <section class="mq" aria-labelledby="mq-t">
      <div class="mq-head">
        <div><span class="mono muted">Prototipo funcional · pruébalo</span><h3 id="mq-t">Metric.arq</h3>
          <p>Del modelo de Revit al costo, el calendario y las instalaciones. Elige una herramienta, mueve un control o toca un ejemplo y el resultado cambia al instante.</p></div>
        <div class="seg mq-tabs" role="group" aria-label="Herramienta de Metric.arq">
          <button type="button" data-mq="calc" aria-pressed="true"><svg class="ic" aria-hidden="true"><use href="#i-calc"/></svg>Instalaciones</button>
          <button type="button" data-mq="muro" aria-pressed="false"><svg class="ic" aria-hidden="true"><use href="#i-muro"/></svg>Muro de block</button>
        </div>
      </div>
      <div class="mq-body" data-mq="calc">
{calc}
      </div>
      <div class="mq-body" data-mq="muro" hidden>
{demo_pu}
      </div>
      <details class="mq-que" id="mq-que"></details>
    </section>
    <section class="otros" aria-labelledby="ot-t">
      <div class="sec-t"><h3 id="ot-t"><svg class="ic" aria-hidden="true"><use href="#i-codigo"/></svg>Otros desarrollos</h3><span class="mono muted">Con código</span></div>
      <details class="dps"><summary><svg class="ic" aria-hidden="true"><use href="#i-rollo"/></svg><span>Probar el demo de Mr. Pasto: cuántos rollos de pasto comprar</span><i aria-hidden="true">+</i></summary>
{demo_ps}
      </details>
      <div id="apps"></div>
    </section>
'''
i0 = s.index('  <div class="labw">\n')
i1 = s.index('  </div>\n</aside>')
s = s[:i0] + nuevo + s[i1:]

# ---- CSS ----
css = """
/* panel de demos: Metric.arq al frente, todo en dos pantallas */
.mq{border:1px solid var(--text-muted);border-radius:var(--r);background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.015));padding:clamp(16px,2.4vw,28px);display:flex;flex-direction:column;gap:18px}
.mq-head{display:flex;justify-content:space-between;align-items:flex-end;gap:16px 28px;flex-wrap:wrap}
.mq-head h3{margin:4px 0 8px;font-size:clamp(30px,4.4vw,52px);font-weight:800;letter-spacing:-.035em;line-height:1}
.mq-head p{margin:0;max-width:56ch;color:var(--text-muted);font-size:15px}
.mq-tabs button{min-height:46px;padding:8px 18px;font-size:12px}
.mq-body[hidden]{display:none}
.mq .demo{padding:0;background:transparent}
.mq .demo>.dtop{justify-content:flex-end}
.mq .demo>.dtop .mono{display:none}
.mq .calc{border-color:var(--border-color)}
.mq-que summary{cursor:pointer;font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);min-height:40px;display:flex;align-items:center}
.mq-que summary:hover{color:var(--text-main)}
.mq-que ol{margin:8px 0 6px;padding:0;list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.mq-que li{border-left:2px solid var(--border-color);padding-left:12px;font-size:14px;color:var(--text-main)}
.mq-que .res{margin:8px 0 0;font-size:14px;color:var(--text-muted)}
@media (max-width:760px){.mq-que ol{grid-template-columns:1fr}}
.mq .vista[data-v="probar"]{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}
.mq .col-a,.mq .col-b{display:flex;flex-direction:column;gap:14px;min-width:0}
@media (min-width:901px){.mq .vista[data-v="probar"]{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:28px;align-items:start}}
.otros{display:flex;flex-direction:column;gap:14px}
.dps{border:1px solid var(--border-color);border-radius:var(--r-m);background:rgba(255,255,255,.02)}
.dps>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;padding:14px 18px;min-height:56px;font-size:15px;font-weight:700}
.dps>summary::-webkit-details-marker{display:none}
.dps>summary span{flex:1;min-width:0}
.dps>summary i{font-style:normal;font-family:var(--mono);font-size:20px;color:var(--text-muted);transition:transform .5s var(--ease)}
.dps[open]>summary i{transform:rotate(45deg)}
.dps .demo{padding:4px 18px 20px;background:transparent}
.dps .demo>.dtop .mono{display:none}
.prs{margin-bottom:2px}
.prs .lb{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);align-self:center;margin-right:2px}
.labw{gap:26px;padding-top:24px}
"""
i = s.index("</style>")
s = s[:i] + css + s[i:]

# ---- JS ----
cambia("$('#apps').innerHTML=APPS.map(function(a){", "$('#apps').innerHTML=APPS.filter(function(a){return a.nombre!=='Metric.arq'}).map(function(a){")
cambia("Incluye la calculadora de instalaciones: pruébala en el Lab.", "Incluye la calculadora de instalaciones y el costo de un muro armado: pruébalos aquí arriba.")
cambia("var PU=", "var PU=") if False else None
extra = r'''
/* Metric.arq: pestañas entre herramientas, «qué hace» y ejemplos con un toque */
(function(){
  var MQ=APPS.filter(function(a){return a.nombre==='Metric.arq'})[0];
  if(MQ) $('#mq-que').innerHTML='<summary>Qué hace Metric.arq</summary><ol>'+MQ.pasos.map(function(q){return '<li><b>'+esc(q[0])+'</b> '+esc(q[1])+'</li>'}).join('')+'</ol><p class="res">'+esc(MQ.res)+'</p>';
  $$('.mq-tabs button').forEach(function(b){ b.addEventListener('click',function(){ $$('.mq-tabs button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')}); $$('.mq-body').forEach(function(c){ c.hidden=c.dataset.mq!==b.dataset.mq; }); }); });
  function pon(ids,vals){ ids.forEach(function(id,i){ var e=$('#'+id); e.value=vals[i]; e.dispatchEvent(new Event('input',{bubbles:true})); }); }
  function ejemplos(pane,titulo,lista,ids){ var d=document.createElement('div'); d.className='chips prs'; d.setAttribute('role','group'); d.setAttribute('aria-label',titulo); d.innerHTML='<span class="lb">'+titulo+'</span>'+lista.map(function(x,k){return '<button type="button" data-k="'+k+'">'+x[0]+'</button>'}).join('');
    $$('button',d).forEach(function(b){ b.addEventListener('click',function(){ pon(ids,lista[+b.dataset.k][1]); }); }); var cin=$('.cpane[data-c="'+pane+'"] .cin'); cin.insertBefore(d,cin.firstChild); }
  ejemplos('agua','Ejemplos',[['Depa 70 m²',[70,2,1]],['Casa 160 m²',[160,3,3]],['Casa 300 m²',[300,4,4]]],['c-m2','c-rec','c-ban']);
  ejemplos('ac','Ejemplos',[['Recámara 14 m²',[14,2,2]],['Sala 30 m²',[30,5,6]]],['c-aa','c-ap','c-av']);
})();
'''
cambia("pintaDemos();\n</script>", "pintaDemos();\n" + extra + "</script>") if s.count("pintaDemos();\n</script>") == 1 else None
if "Metric.arq: pestañas entre herramientas" not in s:
    i = s.rindex("pintaDemos();")
    j = s.index("\n", i)
    s = s[:j + 1] + extra + s[j + 1:]
p.write_text(s, encoding="utf-8")
print("ok")
