"""Rehace el demo «Muro de block» del panel DEMOS: muro armado con cimentación corrida, castillos y dalas de cerramiento.
Se ejecuta una sola vez sobre src/pagina.html (queda como registro del cambio)."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")


def cambia(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)


# ---------- HTML: vista «Probar» ----------
i0 = s.index('            <h4>Muro de block</h4>')
i1 = s.index('          <div class="vista" data-v="como" hidden>', i0)
probar = '''            <h4>Muro de block armado</h4>
            <div><div class="big num" id="pu-total">$44,890</div><span class="mono muted">sin IVA</span></div>
            <svg class="dib" id="pu-svg" viewBox="0 0 400 200" role="img" aria-label="Elevación del muro con su cimentación, castillos y dalas de cerramiento, junto a una persona"></svg>
            <div class="legend"><span><i style="background:#555"></i>Cimentación</span><span><i style="background:#fff"></i>Castillos</span><span><i style="background:#aaa"></i>Dalas</span></div>
            <label class="rng" for="pu-l"><span class="lbl">Longitud <output id="pu-lo">12 m</output></span><input id="pu-l" type="range" min="2" max="40" step="0.5" value="12"></label>
            <label class="rng" for="pu-h"><span class="lbl">Altura <output id="pu-ho">3 m</output></span><input id="pu-h" type="range" min="2" max="6" step="0.1" value="3"></label>
            <div class="chips" role="group" aria-label="Muros de ejemplo"><button type="button" data-m="3,3">3 × 3 m</button><button type="button" data-m="6,3">6 × 3 m</button><button type="button" data-m="12,3">12 × 3 m</button><button type="button" data-m="30,3">30 × 3 m</button><button type="button" data-m="12,5">12 × 5 m</button></div>
            <div class="stats3 stats4"><div><b id="pu-block">1,418</b><span>Blocks</span></div><div><b id="pu-cast">6</b><span>Castillos</span></div><div><b id="pu-jor">12</b><span>Jornadas</span></div><div><b id="pu-hh">190</b><span>Horas-hombre</span></div></div>
            <div class="desg" id="pu-desg"></div>
            <div class="split" id="pu-split" role="img" aria-label="Reparto del costo directo"><i id="pu-sm" style="width:50%;background:#E6E6E6"></i><i id="pu-so" style="width:48%;background:#888"></i><i id="pu-sh" style="width:2%;background:#444"></i></div>
            <div class="legend"><span><i style="background:#E6E6E6"></i>Material</span><span><i style="background:#888"></i>Mano de obra</span><span><i style="background:#444"></i>Herramienta</span></div>
          </div>
'''
s = s[:i0] + probar + s[i1:]

# ---------- HTML: vista «Cómo funciona» ----------
j0 = s.index('              <li>Muro de 15 cm de block de concreto de 15×20×40 cm asentado')
j1 = s.index('            </ul>', j0)
como = '''              <li>Es un muro de block de 15 cm (15×20×40 cm, mortero 1:5, escalerilla cada 2 hiladas) con sus elementos de refuerzo. Cada concepto sale de una tarjeta de precio unitario de Metric.arq (en revisión), sin IVA y con indirectos, financiamiento y utilidad.</li>
              <li><b>Muro:</b> longitud × altura, a $450.48 por m² (E04.02.0033). No descuenta puertas ni ventanas.</li>
              <li><b>Castillos:</b> de 15×15 cm con armex (E04.04.0008, $382.29 por m), uno en cada extremo y uno como máximo cada 2.8 m. Cantidad = ⌈longitud ÷ 2.8⌉ + 1, cada uno de la altura del muro.</li>
              <li><b>Dalas de cerramiento:</b> de 15×20 cm (E04.03.0003, $457.45 por m), una por cada 3 m de altura a lo largo de todo el muro; a 3 m de altura es la de remate. Cantidad = ⌈altura ÷ 3⌉.</li>
              <li><b>Cimentación corrida:</b> de mampostería de piedra, 60 cm de base, 60 de alto y 30 de corona (E02.01.0152, $801.30 por m), con excavación de cepa (0.42 m³ por m), relleno compactado (0.15 m³ por m) y dala de desplante de 15×20 cm (I04.03.0001, $431.59 por m). Las medidas son las típicas de una vivienda de un nivel; en un proyecto real las da el cálculo estructural.</li>
              <li>Cada m² de muro lleva 13.1 blocks (con 5 % de desperdicio). Jornadas y horas-hombre suman las de cada concepto; la barra reparte el costo directo entre material, mano de obra y herramienta.</li>
'''
s = s[:j0] + como + s[j1:]

# ---------- CSS ----------
cambia(".stats3 span{", """.stats4{grid-template-columns:repeat(4,minmax(0,1fr))}
@media (max-width:520px){.stats4{grid-template-columns:repeat(2,minmax(0,1fr))}}
.desg{display:grid;gap:1px;background:var(--border-color);border:1px solid var(--border-color)}
.desg div{display:flex;justify-content:space-between;align-items:baseline;gap:12px;background:var(--bg-dark);padding:8px 12px;font-size:14px;min-width:0}
.desg span{min-width:0}
.desg em{font-style:normal;color:var(--text-muted);font-family:var(--mono);font-size:11px;margin-left:8px}
.desg b{font-variant-numeric:tabular-nums;white-space:nowrap}
.stats3 span{""")

# ---------- JS ----------
k0 = s.index("var PU=450.48, BLK=13.125")
k1 = s.index("function ps(){", k0)
js = r'''/* Tarjetas de Metric.arq (sin IVA): pu, reparto del costo directo (m material, o mano de obra, h herramienta), jornadas y horas-hombre por unidad */
var TM={exc:{pu:229.13,m:0,o:.9709,h:.0291,jor:.25,hh:2},cim:{pu:801.3,m:.4687,o:.5158,h:.0155,jor:.122699,hh:2.9448},rel:{pu:196.01,m:.0648,o:.9079,h:.0273,jor:.2,hh:1.6},des:{pu:431.59,m:.4622,o:.5221,h:.0157,jor:.090909,hh:1.4545},
  blk:{pu:450.48,m:.5952,o:.393,h:.0118,jor:.071429,hh:1.1429},cas:{pu:382.29,m:.3322,o:.6484,h:.0194,jor:.1,hh:1.6},dal:{pu:457.45,m:.4419,o:.5419,h:.0162,jor:.1,hh:1.6}};
var BLK=13.125, SEP_CAST=2.8, SEP_DALA=3, animPU={l:12,h:3,tl:12,th:3,raf:0};
function muro(L,H){
  var nc=Math.ceil(L/SEP_CAST-1e-9)+1, nd=Math.ceil(H/SEP_DALA-1e-9);
  var q={exc:.42*L,cim:L,rel:.15*L,des:L,blk:L*H,cas:nc*H,dal:nd*L}, r={tot:0,m:0,o:0,h:0,jor:0,hh:0,g:{cim:0,blk:0,cas:0,dal:0},nc:nc,nd:nd,L:L,H:H,blocks:Math.ceil(L*H*BLK)};
  Object.keys(q).forEach(function(k){ var t=TM[k], c=t.pu*q[k], gk=(k==='blk'||k==='cas'||k==='dal')?k:'cim';
    r.tot+=c; r.g[gk]+=c; r.m+=c*t.m; r.o+=c*t.o; r.h+=c*t.h; r.jor+=t.jor*q[k]; r.hh+=t.hh*q[k]; });
  return r;
}
function pintaMuro(L,H){
  var r=muro(L,H), pc=function(v){return (v/r.tot*100).toFixed(1)};
  $('#pu-total').textContent=money.format(r.tot); $('#pu-block').textContent=nf0.format(r.blocks); $('#pu-cast').textContent=r.nc; $('#pu-jor').textContent=nf1.format(r.jor).replace(/\.0$/,''); $('#pu-hh').textContent=nf0.format(r.hh);
  $('#pu-desg').innerHTML=
   '<div><span>Cimentación corrida<em>'+nf1.format(L)+' m</em></span><b>'+money.format(r.g.cim)+'</b></div>'+
   '<div><span>Muro de block<em>'+nf1.format(L*H)+' m²</em></span><b>'+money.format(r.g.blk)+'</b></div>'+
   '<div><span>Castillos<em>'+r.nc+' × '+nf1.format(H)+' m</em></span><b>'+money.format(r.g.cas)+'</b></div>'+
   '<div><span>Dalas de cerramiento<em>'+r.nd+' × '+nf1.format(L)+' m</em></span><b>'+money.format(r.g.dal)+'</b></div>';
  var pm=r.m/(r.m+r.o+r.h)*100, po=r.o/(r.m+r.o+r.h)*100, ph=100-pm-po;
  $('#pu-sm').style.width=pm+'%'; $('#pu-so').style.width=po+'%'; $('#pu-sh').style.width=ph+'%';
  $('#pu-split').setAttribute('aria-label','Costo directo: material '+nf1.format(pm)+' por ciento, mano de obra '+nf1.format(po)+' por ciento, herramienta '+nf1.format(ph)+' por ciento');
  /* elevación a escala: cimiento (0.6 m bajo el terreno), dala de desplante (0.2), muro de altura libre H y dalas de cerramiento (0.2) */
  var s=Math.min(330/L,132/(H+1)), w=L*s, x0=24, gy=178-.6*s, wb=gy-.2*s, wt=wb-H*s, bw=.4*s, bh=.2*s, o='';
  if(s>=10) o+='<defs><pattern id="blk" width="'+bw+'" height="'+(2*bh)+'" patternUnits="userSpaceOnUse" x="'+x0+'" y="'+wt+'"><path d="M0 0H'+bw+'M0 '+bh+'H'+bw+'M0 0V'+bh+'M'+(bw/2)+' '+bh+'V'+(2*bh)+'" stroke="rgba(230,230,230,.3)" stroke-width=".6" fill="none"/></pattern></defs>';
  o+='<rect x="'+x0+'" y="'+gy+'" width="'+w+'" height="'+(.6*s)+'" fill="#555" stroke="#888" stroke-width=".8"/>';
  o+='<rect x="'+x0+'" y="'+wb+'" width="'+w+'" height="'+(.2*s)+'" fill="#aaa"/>';
  o+='<rect x="'+x0+'" y="'+wt+'" width="'+w+'" height="'+(H*s)+'" fill="'+(s>=10?'url(#blk)':'rgba(230,230,230,.12)')+'" stroke="#E6E6E6" stroke-width="1"/>';
  var cw=Math.max(.15*s,2.4), i, cx;
  for(i=0;i<r.nc;i++){ cx=x0+i*(w-cw)/(r.nc-1); o+='<rect x="'+cx+'" y="'+(wt-.2*s)+'" width="'+cw+'" height="'+(H*s+.2*s)+'" fill="#fff"/>'; }
  var dh=Math.max(.2*s,2.4); o+='<rect x="'+x0+'" y="'+(wt-.2*s)+'" width="'+w+'" height="'+dh+'" fill="#aaa"/>';
  for(i=1;i*SEP_DALA<H-.05;i++) o+='<rect x="'+x0+'" y="'+(wb-i*SEP_DALA*s-dh/2)+'" width="'+w+'" height="'+dh+'" fill="#aaa"/>';
  o+='<line x1="8" y1="'+gy+'" x2="392" y2="'+gy+'" stroke="#888" stroke-width="1" stroke-dasharray="5 3"/>';
  var px=x0+w+22, ps=1.75*s; if(px+16<392){ o+='<g fill="none" stroke="#888" stroke-width="1.2"><circle cx="'+(px+8)+'" cy="'+(gy-ps+.13*ps)+'" r="'+(.11*ps)+'"/><path d="M'+(px+8)+' '+(gy-ps+.24*ps)+'V'+(gy-.45*ps)+'M'+(px+8)+' '+(gy-.45*ps)+'L'+(px+2)+' '+gy+'M'+(px+8)+' '+(gy-.45*ps)+'L'+(px+14)+' '+gy+'M'+px+' '+(gy-.72*ps)+'H'+(px+16)+'"/></g>'; }
  o+='<text x="'+(x0+w/2)+'" y="196" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#888">'+nf1.format(L)+' × '+nf1.format(H)+' m</text>';
  $('#pu-svg').innerHTML=o;
}
function stepPU(){ var a=animPU, dl=a.tl-a.l, dh=a.th-a.h; if(Math.abs(dl)<.02&&Math.abs(dh)<.02){a.l=a.tl;a.h=a.th;a.raf=0;pintaMuro(a.l,a.h);return} a.l+=dl*.2; a.h+=dh*.2; pintaMuro(a.l,a.h); a.raf=requestAnimationFrame(stepPU); }
function pu(){ var L=parseFloat($('#pu-l').value)||2, H=parseFloat($('#pu-h').value)||2; $('#pu-lo').textContent=nf1.format(L)+' m'; $('#pu-ho').textContent=nf1.format(H)+' m'; animPU.tl=L; animPU.th=H; if(reduce){animPU.l=L;animPU.h=H;pintaMuro(L,H);return} if(!animPU.raf) animPU.raf=requestAnimationFrame(stepPU); }
'''
s = s[:k0] + js + s[k1:]

cambia("function pintaDemos(){ calcActual(); animPU.v=animPU.t=parseFloat($('#pu-m2').value)||120; $('#pu-o').textContent=nf0.format(animPU.t)+' m²'; pintaMuro(animPU.v); ps(); }",
       "function pintaDemos(){ calcActual(); animPU.l=animPU.tl=parseFloat($('#pu-l').value)||12; animPU.h=animPU.th=parseFloat($('#pu-h').value)||3; $('#pu-lo').textContent=nf1.format(animPU.l)+' m'; $('#pu-ho').textContent=nf1.format(animPU.h)+' m'; pintaMuro(animPU.l,animPU.h); ps(); }")
cambia("$('#pu-m2').addEventListener('input',pu);", "$('#pu-l').addEventListener('input',pu); $('#pu-h').addEventListener('input',pu);")
cambia("$$('[data-m]').forEach(function(b){b.addEventListener('click',function(){$('#pu-m2').value=b.dataset.m; pu()})});",
       "$$('[data-m]').forEach(function(b){b.addEventListener('click',function(){var v=b.dataset.m.split(','); $('#pu-l').value=v[0]; $('#pu-h').value=v[1]; pu()})});")
p.write_text(s, encoding="utf-8")
print("ok")
