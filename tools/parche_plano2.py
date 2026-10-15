"""Planta baja del visor 3D: auto en la cochera y árboles y arbustos del jardín, solo en contorno.

Los árboles y arbustos salen del modelo (los grupos del jardín y de la cochera que miden más de 0.5 m de alto).
El modelo no trae auto, así que se dibuja un símbolo de sedán de 4.1 × 1.8 m centrado en el portón.

Uso:  python tools/parche_plano2.py   (idempotente)
"""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "dashboard" / "modelo.html"
s = p.read_text(encoding="utf-8")
if "/*auto-arboles*/" in s:
    raise SystemExit("modelo.html ya tiene el auto y los árboles")

a = "  /* escalera */"
assert s.count(a) == 1
bloque = r"""  /*auto-arboles*/
  if(nivel===0){
    ['jardin','cochera'].forEach(function(id){var g=mobil[id];if(!g)return;g.children.forEach(function(ch){if(ch.type!=='Group')return;var b=new T.Box3().setFromObject(ch),w=b.max.x-b.min.x,d=b.max.z-b.min.z,h=b.max.y-b.min.y;if(h<0.5||Math.max(w,d)<0.5)return;
      var cx=(b.min.x+b.max.x)/2,cyh=-(b.min.z+b.max.z)/2-OFF,q=fp(cx,cyh).split(','),X=parseFloat(q[0]),Yq=parseFloat(q[1]),r=Math.max(w,d)/2,tree=h>2;
      body+='<circle cx="'+X.toFixed(3)+'" cy="'+Yq.toFixed(3)+'" r="'+r.toFixed(3)+'" fill="'+(tree?'rgba(120,170,100,.28)':'rgba(120,170,100,.18)')+'" stroke="#4f7a43" stroke-width="0.025" '+(tree?'stroke-dasharray="0.12 0.07"':'')+'/>';
      if(tree)body+='<circle cx="'+X.toFixed(3)+'" cy="'+Yq.toFixed(3)+'" r="0.07" fill="#6b4a2f"/><path d="M'+(X-r*0.55).toFixed(3)+' '+Yq.toFixed(3)+'H'+(X+r*0.55).toFixed(3)+'M'+X.toFixed(3)+' '+(Yq-r*0.55).toFixed(3)+'V'+(Yq+r*0.55).toFixed(3)+'" stroke="#4f7a43" stroke-width="0.012"/>';
      else for(var k=0;k<8;k++){var an=k*Math.PI/4;body+='<line x1="'+X.toFixed(3)+'" y1="'+Yq.toFixed(3)+'" x2="'+(X+Math.cos(an)*r*0.85).toFixed(3)+'" y2="'+(Yq+Math.sin(an)*r*0.85).toFixed(3)+'" stroke="#4f7a43" stroke-width="0.012"/>';}});});
    var ax=fp(1.8,0).split(',')[0],A=parseFloat(ax),Y0=11.45,st='fill="#fbfaf6" fill-opacity="0.9" stroke="#8b8780" stroke-width="0.02"';
    body+='<g data-auto="1"><rect x="'+(A-0.0).toFixed(3)+'" y="'+Y0+'" width="1.8" height="4.1" rx="0.38" '+st+'/>'
      +'<path d="M'+(A+0.22)+' '+(Y0+1.15)+'L'+(A+0.32)+' '+(Y0+0.8)+'H'+(A+1.48)+'L'+(A+1.58)+' '+(Y0+1.15)+'Z" '+st+'/>'
      +'<rect x="'+(A+0.2)+'" y="'+(Y0+1.15)+'" width="1.4" height="1.5" rx="0.12" fill="none" stroke="#8b8780" stroke-width="0.02"/>'
      +'<path d="M'+(A+0.28)+' '+(Y0+2.65)+'L'+(A+0.38)+' '+(Y0+3.0)+'H'+(A+1.42)+'L'+(A+1.52)+' '+(Y0+2.65)+'" fill="none" stroke="#8b8780" stroke-width="0.02"/>'
      +[[-0.1,0.55],[1.68,0.55],[-0.1,3.0],[1.68,3.0]].map(function(w){return '<rect x="'+(A+w[0]).toFixed(3)+'" y="'+(Y0+w[1]).toFixed(3)+'" width="0.22" height="0.55" rx="0.05" fill="#bdb9b0" stroke="#8b8780" stroke-width="0.015"/>';}).join('')
      +'<ellipse cx="'+(A-0.02)+'" cy="'+(Y0+1.2)+'" rx="0.07" ry="0.12" '+st+'/><ellipse cx="'+(A+1.82)+'" cy="'+(Y0+1.2)+'" rx="0.07" ry="0.12" '+st+'/></g>';
  }
"""
s = s.replace(a, bloque + a)
p.write_text(s, encoding="utf-8")
print("ok")
