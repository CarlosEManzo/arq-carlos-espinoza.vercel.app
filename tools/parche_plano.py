"""Hace legible la vista «Planta» de dashboard/modelo.html: estilo plano técnico sobre papel claro.

Muros en negro, recintos en tonos suaves, mobiliario solo en contorno, sin ruido del jardín ni de la cochera,
rótulos oscuros, escalera con peldaños, puertas con abatimiento y acotaciones.

Uso:  python tools/parche_plano.py   (idempotente)
"""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "dashboard" / "modelo.html"
s = p.read_text(encoding="utf-8")
if "/*plano-claro*/" in s:
    raise SystemExit("modelo.html ya tiene el plano claro")


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)


# --- hoja y títulos
rep("#plano2d{position:absolute;inset:0;z-index:1;background:#0f0f0f}#plano2d svg{width:100%;height:100%;display:block}",
    "#plano2d{position:absolute;inset:0;z-index:1;background:#e9e6df;color:#111}#plano2d svg{width:100%;height:100%;display:block;box-sizing:border-box;padding:64px 12px 120px}#plano2d .ptit,#plano2d .ptit span{color:#222}/*plano-claro*/")

# --- recintos: tono suave a partir del acabado elegido
a = s.index("  function relleno(id){")
b = s.index("  /* lote y calle */")
s = s[:a] + """  function relleno(id){var base={cochera:'#dcd9d2',jardin:'#d5e2cb'},sl=slotDe[id];if(!sl)return base[id]||'#eee';return new T.Color(OPC[sl].o[ELEC[sl]][1]).lerp(new T.Color('#ffffff'),0.72).getStyle();}
""" + s[b:]

# --- lote y calle
rep('fill="#141414"/><rect x="1.4" y="\'+(11.3-10.5)+\'" width="6" height="15" fill="#1c1c1c" stroke="#555"',
    'fill="#e9e6df"/><rect x="1.4" y="\'+(11.3-10.5)+\'" width="6" height="15" fill="#f7f5f0" stroke="#8a867e"')
rep('height="0.8" fill="#2a2a2c"/><text x="6.4" y="\'+(11.3+4.98)+\'" fill="#777"', 'height="0.8" fill="#cfcbc3"/><text x="6.4" y="\'+(11.3+4.98)+\'" fill="#6b675f"')
rep('stroke="\'+(r.id===selId?\'#fff\':\'none\')+\'" stroke-width="0.07"', 'stroke="\'+(r.id===selId?\'#c2185b\':\'none\')+\'" stroke-width="0.07"')
rep('fill="rgba(255,255,255,.04)" stroke="#888"', 'fill="rgba(0,0,0,.05)" stroke="#888"')
rep('<text x="\'+fp(2.4,2.0).split(\',\')[0]+\'" y="\'+fp(2.4,2.0).split(\',\')[1]+\'" fill="#999"', '<text x="\'+fp(2.4,2.0).split(\',\')[0]+\'" y="\'+fp(2.4,2.0).split(\',\')[1]+\'" fill="#555"')

# --- mobiliario: solo interiores, solo piezas con tamaño, solo contorno
rep("ids.forEach(function(id){var g=mobil[id];if(!g)return;g.children.forEach(", "ids.forEach(function(id){var g=mobil[id];if(!g||id==='jardin'||id==='cochera'||id==='patio')return;g.children.forEach(")
rep("if(w<0.03&&d<0.03)return;var lv=", "if(w<0.03&&d<0.03)return;if(w*d<0.1)return;var lv=")
rep("""var f=col?'fill="'+col+'" fill-opacity="0.92"':'fill="none"';""", """var f='fill="#fbfaf6" fill-opacity="0.85"';""")
rep('stroke="rgba(0,0,0,.45)" stroke-width="0.012"/>', 'stroke="#8b8780" stroke-width="0.02"/>', 2)

rep("if(w*d<0.1)return;var lv=", "if(w*d<0.1)return;var yc=-(b.min.z+b.max.z)/2;if(yc<4.5||yc>12.1)return;var lv=")
rep("if(!o.e||o.e.cat!=='PlumbingFixtures')return;", "if(!o.e||o.e.cat!=='PlumbingFixtures'||o.y0<4.4||o.y1>12.1)return;")

# el mobiliario se dibujaba corrido hacia el fondo una profundidad completa (y=borde-d): el borde superior ya es p2[1]
rep("(parseFloat(p2[1])-d).toFixed(3)", "parseFloat(p2[1]).toFixed(3)")
# --- escalera con peldaños
rep("""fill="'+(nivel===0?'#8a5d3a':'none')+'" fill-opacity="0.9" stroke="'+(nivel===0?'#2b1d12':'#8a8a8a')+'" stroke-width="0.016" '+(nivel===1?'stroke-dasharray="0.08 0.06"':'')+'/>';}});""",
    """fill="'+(nivel===0?'#e1cfb3':'none')+'" fill-opacity="0.95" stroke="'+(nivel===0?'#555':'#8a8a8a')+'" stroke-width="0.02" '+(nivel===1?'stroke-dasharray="0.08 0.06"':'')+'/>';if(nivel===0){var nq=Math.max(2,Math.round((o.y1-o.y0)/0.28)),px=parseFloat(p[0]),py=parseFloat(p[1]),hh=o.y1-o.y0;for(var q=1;q<nq;q++)body+='<line x1="'+px+'" x2="'+(px+o.x1-o.x0).toFixed(3)+'" y1="'+(py+q*hh/nq).toFixed(3)+'" y2="'+(py+q*hh/nq).toFixed(3)+'" stroke="#8a7a62" stroke-width="0.012"/>';}}});""")
rep('stroke="#fff" stroke-width="0.03"/><path d="M\'+a2[0]', 'stroke="#222" stroke-width="0.03"/><path d="M\'+a2[0]')
rep('l-0.1 0.2 l0.2 0 z" fill="#fff"/><text x="\'+a1[0]+\'" y="\'+(parseFloat(a1[1])+0.28)+\'" fill="#fff"', 'l-0.1 0.2 l0.2 0 z" fill="#222"/><text x="\'+a1[0]+\'" y="\'+(parseFloat(a1[1])+0.28)+\'" fill="#222"')

# --- muros, puertas y ventanas
rep("fill=\"'+(ext?'#8a4a38':'#efebe1')+'\" stroke=\"#0d0d0d\"", "fill=\"'+(ext?'#4a4a4a':'#161616')+'\" stroke=\"#0d0d0d\"")
rep('fill="#8fc4ee" fill-opacity="0.8" stroke="#dff1ff"', 'fill="#8fc4ee" fill-opacity="0.9" stroke="#222"')
rep('fill="#1c1c1c" stroke="#e8e4da" stroke-width="0.012"/><path d="M', 'fill="#fff" stroke="#222" stroke-width="0.02"/><path d="M')
rep('fill="none" stroke="#e8e4da" stroke-width="0.012" stroke-dasharray="0.05 0.04"', 'fill="none" stroke="#222" stroke-width="0.016" stroke-dasharray="0.05 0.04"')

# --- rótulos, cotas y norte
rep('fill="#fff" stroke="#000" stroke-width="0.07" paint-order="stroke"', 'fill="#111" stroke="#fff" stroke-width="0.09" paint-order="stroke"')
rep('fill="#ddd" stroke="#000" stroke-width="0.06" paint-order="stroke"', 'fill="#444" stroke="#fff" stroke-width="0.07" paint-order="stroke"')
rep('<g stroke="#aaa" stroke-width="0.02" fill="#aaa"', '<g stroke="#333" stroke-width="0.02" fill="#333"')
rep('<circle r="0.55" fill="none" stroke="#aaa" stroke-width="0.03"/><path d="M0 -0.8 L0.18 0 L0 -0.12 L-0.18 0 Z" fill="#fff"/></g><text x="11.3" y="1.15" fill="#fff"',
    '<circle r="0.55" fill="none" stroke="#333" stroke-width="0.03"/><path d="M0 -0.8 L0.18 0 L0 -0.12 L-0.18 0 Z" fill="#111"/></g><text x="11.3" y="1.15" fill="#111"')

p.write_text(s, encoding="utf-8")
print("ok")
