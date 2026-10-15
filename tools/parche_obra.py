"""Inserta en dashboard/modelo.html la secuencia constructiva real del Loft (4D).

Uso:  python tools/parche_obra.py
Es idempotente: si el bloque ya está, no hace nada.
"""
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
p = raiz / "dashboard" / "modelo.html"
s = p.read_text(encoding="utf-8")
if "var OBRA=new T.Group()" in s:
    raise SystemExit("modelo.html ya tiene la secuencia de obra")
bloque = (raiz / "tools" / "obra_block.js").read_text(encoding="utf-8")

a = "var struct=[], ghostables=[], infra=[], pisosPorSlot=[], pend=[];"
assert s.count(a) == 1
s = s.replace(a, a + bloque)

nueva = """function cortaFase(p){if(p<0.17)return null;if(p<0.24)return 2.8*sm(0.17,0.24,p);if(p<0.27)return 2.8;if(p<0.31)return 2.8+2.7*sm(0.27,0.31,p);if(p<0.335)return 5.5;if(p<0.355)return 5.5+0.6*sm(0.335,0.355,p);return null;}
function aplicaFase(){var p=faseP,inf=capasAct;
  OBRA.visible=!inf;TIERRA.visible=!inf&&p<0.9;root.children.forEach(function(c){if(c.type==='Group')c.visible=p>0.6;});
  var dEx=0.8*sm(0.02,0.05,p)-0.78*sm(0.10,0.12,p);OBTR.forEach(function(m){m.scale.y=Math.max(0.01,1-dEx);m.position.y=-dEx;});
  OBP.forEach(function(e){var v=p>=e.a&&p<e.b;if(e.g){var t=sm(e.g[0],e.g[1],p);v=v&&t>0.001;e.o.scale.y=Math.max(0.001,t);}e.o.visible=v;});
  struct.forEach(function(m){var u=m.userData,r=u.rol,tp=(u.e&&u.e.tipo)||'',v=true;if(!u.base)u.base=m.material;
    if(r==='piso'){if(u.minY===undefined){m.geometry.computeBoundingBox();u.minY=m.geometry.boundingBox.clone().applyMatrix4(m.matrixWorld).min.y;}var my=u.minY;
      if(tp==='FIR_CONC_100')v=p>0.125;else if(tp.indexOf('EXT_')===0)v=p>0.9;else if(tp==='LOS_MACIZA_120')v=my<4?p>0.265:p>0.335;else v=p>0.66;}
    else if(r==='muro'){v=p>0.165;if(!inf)m.material=(p<0.6)?OBBLK:u.base;}
    else if(r==='escalera')v=p>0.31;else if(r==='plafon')v=p>0.5;else if(r==='vidrio'||r==='puerta')v=p>0.6;else if(r==='azulejo')v=p>0.66;else if(r==='aparato'||r==='equipo'||r==='disp')v=p>0.7;
    m.visible=v;});
  if(!inf){var ks=Object.keys(mobil);ks.forEach(function(k,i){mobil[k].visible=p>0.78+0.15*i/ks.length;});site.visible=p>0.92;}
  setClip(cortaFase(p));if(LIMPIO)etiquetas.forEach(function(e){e.visible=false;});dirty=true;}
"""
i = s.index("function aplicaFase(){")
j = s.index("var camPrev=null;")
s = s[:i] + nueva + s[j:]

a2 = "if(faseP!=null)aplicaFase();axoPost();dirty=true;}"
assert s.count(a2) == 1
s = s.replace(a2, "if(faseP!=null)aplicaFase();else{OBRA.visible=false;TIERRA.visible=false;root.children.forEach(function(c){if(c.type==='Group')c.visible=true;});}axoPost();dirty=true;}")
p.write_text(s, encoding="utf-8")
print("ok")
