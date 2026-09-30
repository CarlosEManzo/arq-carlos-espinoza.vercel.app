"""Ventana «Información» de cada proyecto: carrusel de fotos con la información encima.
Mismo lenguaje que las páginas del recorrido (fondo desenfocado y oscurecido, foto nítida al frente,
fundido entre fotos, rayitas de avance) pero con flechas, miniaturas, teclado y deslizar con el dedo.
Se ejecuta una sola vez sobre src/pagina.html."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")


def cambia(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)


# ---------------- CSS ----------------
# escritorio: la ventana era una cuadrícula con márgenes
cambia(" .tri .p3m{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:40px;align-content:start;padding:32px 40px}\n", "")
# base: el panel es ahora un escenario
cambia(".p3m{overflow:auto;padding:var(--gut);display:flex;flex-direction:column;gap:24px}\n@media (max-width:900px){.p3m{grid-template-columns:1fr}}\n.p3m .txt{display:flex;flex-direction:column;gap:20px}\n.p3m .txt p{color:var(--text-main);max-width:60ch;font-size:17px}\n",
       """.p3m{position:relative;overflow:hidden;padding:0;--pw:min(430px,40%)}
.p3m .txt{display:flex;flex-direction:column;gap:18px}
.p3m .txt p{color:var(--text-main);max-width:60ch;font-size:16px;margin:0}
.stg{position:absolute;inset:0;overflow:hidden;background:var(--bg-dark);outline:none;touch-action:pan-y}
.stg .fondo,.stg .fr{position:absolute;inset:0;width:100%;height:100%;opacity:0;transition:opacity 1.1s ease}
.stg .fondo{object-fit:cover;filter:blur(26px) grayscale(.45) contrast(1.05) brightness(.5);transform:scale(1.15)}
.stg .fr{object-fit:contain;padding:18px 18px 92px calc(var(--pw) + 18px);transition:opacity .9s ease}
.stg .on{opacity:1}
.stg .barra-i{position:absolute;left:var(--pw);right:0;bottom:0;padding:34px 16px 12px;background:linear-gradient(to top,rgba(13,13,13,.92),rgba(13,13,13,0));display:flex;flex-direction:column;gap:8px;min-width:0}
.stg .pie{display:flex;align-items:center;justify-content:space-between;gap:12px;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.stg .pie span:first-child{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.stg .pie span:last-child{color:var(--text-muted);white-space:nowrap}
.stg .rayas{display:flex;gap:3px}
.stg .rayas i{display:block;flex:1 1 0;max-width:34px;height:2px;background:rgba(255,255,255,.28);transition:background .8s}
.stg .rayas i.on{background:#fff}
.stg .nav-f{position:absolute;top:calc(50% - 46px);width:44px;height:64px;padding:0;background:rgba(13,13,13,.55);border:1px solid var(--border-color);font-family:var(--mono);font-size:18px;display:grid;place-items:center;opacity:.8;transition:opacity .4s,background .4s}
.stg .nav-f:hover{opacity:1;background:rgba(13,13,13,.85)}
.stg .nav-f.a{left:calc(var(--pw) + 8px)}
.stg .nav-f.s{right:8px}
.info-p{position:absolute;left:0;top:0;bottom:0;width:var(--pw);overflow:auto;padding:24px 24px 24px var(--gut);background:rgba(13,13,13,.78);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-right:1px solid var(--border-color);z-index:2}
.stg .thumbs{padding-bottom:0}
.stg .thumbs button{flex:0 0 64px;height:46px;background:rgba(13,13,13,.6)}
@media (max-width:900px){
 .p3m{overflow-y:auto;overflow-x:hidden;display:flex;flex-direction:column;--pw:0px}
 .stg{position:relative;inset:auto;flex:none;height:min(58vh,440px)}
 .stg .fr{padding:10px 10px 84px}
 .stg .barra-i{left:0}
 .stg .nav-f{width:38px;height:54px;top:calc(50% - 60px)}
 .stg .nav-f.a{left:6px}
 .info-p{position:static;width:auto;overflow:visible;background:var(--bg-dark);border-right:0;border-top:1px solid var(--border-color);padding:20px var(--gut) 32px}
}
""")
# la galería anterior ya no se usa
i0 = s.index(".fotos{display:flex;flex-direction:column;gap:8px;min-width:0}")
i1 = s.index(".thumbs{display:flex;gap:6px;overflow-x:auto;padding-bottom:2px}")
s = s[:i0] + s[i1:]

# ---------------- JS: construcción del panel ----------------
j0 = s.index("  $('#pn3').innerHTML='<div class=\"txt\">")
j1 = s.index("  panel(w||'3');", j0)
nuevo = r'''  var N3=o.fotos.length, fotoK=0, slot=0;
  var info='<div class="txt"><span class="mono muted">'+esc(o.tipo)+' · '+esc(o.anio)+'</span><p>'+esc(o.texto)+'</p><dl class="dl"><dt>Rol</dt><dd>'+esc(o.rol)+'</dd>'+(o.empresa?'<dt>Empresa</dt><dd>'+esc(o.empresa)+'</dd>':'')+'<dt>Tipo</dt><dd>'+esc(o.tipo)+'</dd><dt>Año</dt><dd>'+esc(o.anio)+'</dd>'+o.cifras.map(function(c){return '<dt>'+esc(c[1])+'</dt><dd class="num">'+esc(c[0])+'</dd>'}).join('')+'</dl></div>';
  var stage='<div class="stg" id="stg" tabindex="0" role="group" aria-roledescription="carrusel" aria-label="Fotos de '+esc(o.titulo)+'">'+
    '<img class="fondo on" id="stg-f0" alt="" aria-hidden="true"><img class="fondo" id="stg-f1" alt="" aria-hidden="true">'+
    '<img class="fr on" id="stg-a0" alt="'+esc(o.fotos[0][2])+'" decoding="async"><img class="fr" id="stg-a1" alt="" decoding="async">'+
    (N3>1?'<button type="button" class="nav-f a" aria-label="Foto anterior">←</button><button type="button" class="nav-f s" aria-label="Foto siguiente">→</button>':'')+
    '<div class="barra-i">'+
     (N3>1?'<div class="thumbs" role="group" aria-label="Miniaturas">'+o.fotos.map(function(f,k){return '<button type="button" data-k="'+k+'" aria-label="Foto '+(k+1)+': '+esc(f[1])+'"'+(k===0?' aria-current="true"':'')+'><img src="photos/t/'+f[0]+'.jpg" alt="" loading="lazy" decoding="async"></button>'}).join('')+'</div>':'')+
     '<div class="rayas" aria-hidden="true">'+o.fotos.map(function(f,k){return '<i'+(k===0?' class="on"':'')+'></i>'}).join('')+'</div>'+
     '<div class="pie"><span id="f-cap">'+esc(o.fotos[0][1])+'</span><span id="f-n">1 / '+N3+'</span></div></div></div>';
  $('#pn3').innerHTML=stage+'<div class="info-p">'+info+'</div>';
  $('#stg-a0').src='photos/'+o.fotos[0][0]+'.jpg'; $('#stg-f0').src='photos/'+o.fotos[0][0]+'.jpg';
  function foto(k){
    fotoK=(k+N3)%N3; var f=o.fotos[fotoK], src='photos/'+f[0]+'.jpg', nx=1-slot, a=$('#stg-a'+nx), b=$('#stg-f'+nx), a0=$('#stg-a'+slot), b0=$('#stg-f'+slot);
    a.alt=f[2]; a.onload=function(){ a.onload=null; a.classList.add('on'); b.classList.add('on'); a0.classList.remove('on'); b0.classList.remove('on'); }; b.src=src; a.src=src; slot=nx;
    $('#f-cap').textContent=f[1]; $('#f-n').textContent=(fotoK+1)+' / '+N3;
    $$('.rayas i',$('#pn3')).forEach(function(x,q){x.classList.toggle('on',q===fotoK)});
    $$('.thumbs button',$('#pn3')).forEach(function(x,q){var on=q===fotoK; x.setAttribute('aria-current',on?'true':'false'); if(on&&x.scrollIntoView){ var t=x.parentNode; t.scrollTo({left:x.offsetLeft-t.clientWidth/2+x.clientWidth/2,behavior:reduce?'auto':'smooth'}); }});
  }
  nav3=N3>1?foto:null; nav3k=function(){return fotoK};
  $$('.thumbs button',$('#pn3')).forEach(function(b){ b.addEventListener('click',function(){foto(+b.dataset.k)}) });
  var bp=$('.nav-f.a',$('#pn3')), bs=$('.nav-f.s',$('#pn3')); if(bp){ bp.addEventListener('click',function(){foto(fotoK-1)}); bs.addEventListener('click',function(){foto(fotoK+1)}); }
  var sg=$('#stg'), x0=null; sg.addEventListener('pointerdown',function(e){ if(e.target.closest('button')) return; x0=e.clientX; }); sg.addEventListener('pointerup',function(e){ if(x0===null) return; var dx=e.clientX-x0; x0=null; if(Math.abs(dx)>45&&N3>1) foto(fotoK+(dx<0?1:-1)); }); sg.addEventListener('pointercancel',function(){x0=null});
'''
s = s[:j0] + nuevo + s[j1:]

cambia("var obraActual=0, panelActual='3', visorPrev=null;", "var obraActual=0, panelActual='3', visorPrev=null, nav3=null, nav3k=null;")

# teclado: flechas cambian de foto mientras la ventana Información está abierta
cambia("$('#v-cerrar').addEventListener('click',cierraVisor);",
       "$('#v-cerrar').addEventListener('click',cierraVisor);\n$('#visor').addEventListener('keydown',function(e){ if(panelActual!=='3'||!nav3||e.altKey||e.ctrlKey||e.metaKey) return; var t=e.target; if(t&&(t.tagName==='INPUT'||t.tagName==='SELECT'||t.tagName==='TEXTAREA')) return; if(e.key==='ArrowRight'){nav3(nav3k()+1);e.preventDefault()} else if(e.key==='ArrowLeft'){nav3(nav3k()-1);e.preventDefault()} });")
p.write_text(s, encoding="utf-8")
print("ok")
