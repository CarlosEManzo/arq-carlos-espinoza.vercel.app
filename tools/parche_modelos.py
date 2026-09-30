"""Modelos del teleférico y la casa rehechos con congruencia constructiva, y planos por planta.
Toma los modelos de tools/modelos_v3/*.js y los planos nuevos, y los inserta en src/pagina.html. Se ejecuta una sola vez."""
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
p = raiz / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")
est = (raiz / "tools" / "modelos_v3" / "estacion.js").read_text(encoding="utf-8")
cas = (raiz / "tools" / "modelos_v3" / "casa.js").read_text(encoding="utf-8")


def cambia(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:90])
    s = s.replace(a, b)


# ---------- ayudantes para muros con vanos ----------
ayud = r'''/* muros con vanos reales: ab = [[desde, hasta, alféizar, dintel, hoja]] (hoja = 'vidrio' o 'madera'); segmentos macizos, antepecho y dintel alrededor de cada vano */
function paredX(P,g,x0,x1,z,t,y0,h,ab,m){ m=m||'hormigon'; var c=x0; (ab||[]).slice().sort(function(a,b){return a[0]-b[0]}).forEach(function(a){ seg(c,a[0],y0,y0+h); seg(a[0],a[1],y0,a[2]); seg(a[0],a[1],a[3],y0+h); if(a[4]) P.push(box(g,a[1]-a[0]-.06,a[3]-a[2]-.06,a[4]==='vidrio'?.04:.06,(a[0]+a[1])/2,a[2]+.03,z,a[4])); c=a[1]; }); seg(c,x1,y0,y0+h);
  function seg(a,b,ya,yb){ if(b-a>.001&&yb-ya>.001) P.push(box(g,b-a,yb-ya,t,(a+b)/2,ya,z,m)); } }
function paredZ(P,g,z0,z1,x,t,y0,h,ab,m){ m=m||'hormigon'; var c=z0; (ab||[]).slice().sort(function(a,b){return a[0]-b[0]}).forEach(function(a){ seg(c,a[0],y0,y0+h); seg(a[0],a[1],y0,a[2]); seg(a[0],a[1],a[3],y0+h); if(a[4]) P.push(box(g,a[4]==='vidrio'?.04:.06,a[3]-a[2]-.06,a[1]-a[0]-.06,x,a[2]+.03,(a[0]+a[1])/2,a[4])); c=a[1]; }); seg(c,z1,y0,y0+h);
  function seg(a,b,ya,yb){ if(b-a>.001&&yb-ya>.001) P.push(box(g,t,yb-ya,b-a,x,ya,(a+b)/2,m)); } }
'''
cambia("var MODELOS={", ayud + "\nvar MODELOS={")

# ---------- reemplazo de los modelos ----------
a0 = s.index(" /* ---- Teleférico:")
a1 = s.index(" /* ---- Naves:")
s = s[:a0] + est + s[a1:]
b0 = s.index(" /* ---- Casa:")
b1 = s.index(" /* ---- BIM:")
s = s[:b0] + cas + s[b1:]

# plantas para naves y BIM
cambia("niveles:[[.4,'PISO'],[6.4,'ALERO'],[7.6,'CUMBRERA']],grupos:['Losa','Muros','Marcos de acero','Cubierta']};",
       "niveles:[[.4,'PISO'],[6.4,'ALERO'],[7.6,'CUMBRERA']],plantas:[{n:'Planta · corte +2 m',cut:2,ylo:.4,yhi:6.6,ctx:['losa']}],grupos:['Losa','Muros','Marcos de acero','Cubierta']};")
cambia("niveles:[[.4,'N1'],[4.0,'N2'],[7.6,'N3'],[11.2,'AZOTEA']],grupos:",
       "niveles:[[.4,'N1'],[4.0,'N2'],[7.6,'N3'],[11.2,'AZOTEA']],plantas:[{n:'Nivel 1 · corte +1.8 m',cut:1.8,ylo:.4,yhi:3.6,ctx:['losas']},{n:'Nivel 2 · corte +5.4 m',cut:5.4,ylo:4,yhi:7.2,ctx:['losas']},{n:'Nivel 3 · corte +9 m',cut:9,ylo:7.6,yhi:10.8,ctx:['losas']}],grupos:")

# ---------- planos por planta ----------
cambia("function planosSVG(o,modelo,act){\n  act=act||{};", "function planosSVG(o,modelo,act,ip){\n  act=act||{}; var pl=modelo.plantas?modelo.plantas[ip||0]:null, dentro=function(y0,y1){return !pl||(y0<=pl.cut+1e-6&&y1>=pl.cut-1e-6)}, banda=function(y){return !pl||(y>=pl.ylo-1e-6&&y<=pl.yhi+1e-6)};")
cambia("""<text x="40" y="52" fill="#888" font-size="11" letter-spacing="1.5">PLANTA E INSTALACIONES</text>""",
       """<text x="40" y="52" fill="#888" font-size="11" letter-spacing="1.5">'+(pl?'PLANTA · '+esc(pl.n.toUpperCase()):'PLANTA E INSTALACIONES')+'</text>""")
# elementos de la planta: solo los que corta el plano (más un contorno tenue de lo que queda debajo)
cambia("""  parts.forEach(function(q){ if(q.m==='vidrio'){ out+='<rect x="'+X1(q.p[0]-q.s[0]/2)""",
       """  parts.forEach(function(q){ var yq0=q.p[1], yq1=q.p[1]+(q.cyl&&q.r?q.s[0]:q.s[1]);
    if(pl&&!dentro(yq0,yq1)){ if(yq1<pl.cut&&(pl.ctx||[]).indexOf(q.g)>=0&&!q.cyl) out+='<rect x="'+X1(q.p[0]-q.s[0]/2)+'" y="'+Z1(q.p[2]-q.s[2]/2)+'" width="'+(q.s[0]*s1)+'" height="'+(q.s[2]*s1)+'" fill="none" stroke="#3d3d3d" stroke-width=".7"/>'; return; }
    if(q.m==='vidrio'){ out+='<rect x="'+X1(q.p[0]-q.s[0]/2)""")
cambia("""    out+='<rect x="'+X1(q.p[0]-w/2)+'" y="'+Z1(q.p[2]-d/2)+'" width="'+(w*s1)+'" height="'+(d*s1)+'" fill="rgba(255,255,255,.03)" stroke="#bdbdbd" stroke-width=".8"/>'; });""",
       """    out+='<rect x="'+X1(q.p[0]-w/2)+'" y="'+Z1(q.p[2]-d/2)+'" width="'+(w*s1)+'" height="'+(d*s1)+'" fill="'+(pl?'rgba(230,230,230,.2)':'rgba(255,255,255,.03)')+'" stroke="'+(pl?'#E6E6E6':'#bdbdbd')+'" stroke-width="'+(pl?1:.8)+'"/>'; });""")
# instalaciones en planta: tramos que caen en la franja del nivel y montantes que la atraviesan
cambia("""  (modelo.tubos||[]).forEach(function(t){ if(!act[t.s])return; var d=''; t.pts.forEach(function(p,i){ d+=(i?'L':'M')+X1(p[0]).toFixed(1)+' '+Z1(p[2]).toFixed(1)+' '; });
    out+='<path d="'+d+'" fill="none" stroke="'+SIS[t.s].h+'" stroke-width="'+(t.s==='SAN'||t.s==='PLU'?2.2:1.6)+'" stroke-linejoin="round" stroke-linecap="round" opacity=".95"/>'+
      '<circle cx="'+X1(t.pts[0][0])+'" cy="'+Z1(t.pts[0][2])+'" r="2.2" fill="'+SIS[t.s].h+'"/>'; });
  (modelo.equipos||[]).forEach(function(e){ if(!act[e.s])return; out+=""",
       """  (modelo.tubos||[]).forEach(function(t){ if(!act[t.s])return; var col=SIS[t.s].h, sw=(t.s==='SAN'||t.s==='PLU'?2.2:1.6), i, a, b;
    for(i=0;i<t.pts.length-1;i++){ a=t.pts[i]; b=t.pts[i+1]; if(!pl){ out+='<line x1="'+X1(a[0]).toFixed(1)+'" y1="'+Z1(a[2]).toFixed(1)+'" x2="'+X1(b[0]).toFixed(1)+'" y2="'+Z1(b[2]).toFixed(1)+'" stroke="'+col+'" stroke-width="'+sw+'" stroke-linecap="round" opacity=".95"/>'; continue; }
      var y0=Math.min(a[1],b[1]), y1=Math.max(a[1],b[1]), vert=Math.abs(a[0]-b[0])<.02&&Math.abs(a[2]-b[2])<.02;
      if(vert){ if(y0<=pl.yhi&&y1>=pl.ylo) out+='<circle cx="'+X1(a[0]).toFixed(1)+'" cy="'+Z1(a[2]).toFixed(1)+'" r="3.2" fill="none" stroke="'+col+'" stroke-width="1.6"/><circle cx="'+X1(a[0]).toFixed(1)+'" cy="'+Z1(a[2]).toFixed(1)+'" r="1.2" fill="'+col+'"/>'; }
      else if(y1>=pl.ylo&&y0<=pl.yhi) out+='<line x1="'+X1(a[0]).toFixed(1)+'" y1="'+Z1(a[2]).toFixed(1)+'" x2="'+X1(b[0]).toFixed(1)+'" y2="'+Z1(b[2]).toFixed(1)+'" stroke="'+col+'" stroke-width="'+sw+'" stroke-linecap="round" opacity=".95"/>'; } });
  (modelo.equipos||[]).forEach(function(e){ if(!act[e.s]||(pl&&!(e.p[1]+e.sz[1]>=pl.ylo&&e.p[1]<=pl.yhi)))return; out+=""")

# ---------- selector de planta y pintado ----------
cambia("var slideAbierta=null;\nfunction abreVisor(i,w){",
       """function pintaPlanos(){
  var m=V.plan.modelo, ip=V.plan.ip||0, sel='';
  if(m.plantas&&m.plantas.length>1) sel='<div class="plsel" role="group" aria-label="Planta a mostrar">'+m.plantas.map(function(q,k){return '<button type="button" data-p="'+k+'" aria-pressed="'+(k===ip?'true':'false')+'">'+esc(q.n)+'</button>'}).join('')+'</div>';
  $('#pn2').innerHTML=sel+planosSVG(V.plan.o,m,V.act,ip);
  $$('.plsel button',$('#pn2')).forEach(function(b){ b.addEventListener('click',function(){ V.plan.ip=+b.dataset.p; pintaPlanos(); }); });
}
var slideAbierta=null;
function abreVisor(i,w){""")
cambia("V.plan={o:o,modelo:modelo}; V.act={}; sistemasDe(modelo).forEach(function(k){V.act[k]=true}); pintaChips(modelo); $('#v-ico').innerHTML=ic(o.icono); $('#pn2').innerHTML=planosSVG(o,modelo,V.act);",
       "V.plan={o:o,modelo:modelo,ip:0}; V.act={}; sistemasDe(modelo).forEach(function(k){V.act[k]=true}); pintaChips(modelo); $('#v-ico').innerHTML=ic(o.icono); pintaPlanos();")
cambia("$('#pn2').innerHTML=planosSVG(V.plan.o,V.plan.modelo,V.act); }); }); }", "pintaPlanos(); }); }); }")
cambia(".p2d{display:grid;overflow:auto;padding:14px;place-items:center}",
       ".p2d{display:flex;flex-direction:column;align-items:center;overflow:auto;padding:14px;gap:12px}\n.plsel{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}\n.plsel button{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;background:transparent;border:1px solid var(--border-color);padding:8px 14px;min-height:38px;color:var(--text-muted);transition:all .5s var(--ease)}\n.plsel button:hover{color:var(--text-main)}\n.plsel button[aria-pressed=\"true\"]{background:var(--accent);color:var(--bg-dark);border-color:var(--accent)}")
p.write_text(s, encoding="utf-8")
print("ok")
