"""Esquinas redondeadas en toda la página: botones, chips, tarjetas, paneles flotantes, fotos del carrusel, planos y demos.
Se ejecuta una sola vez sobre src/pagina.html."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")


def cambia(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:90])
    s = s.replace(a, b)


css = """
/* esquinas redondeadas: un solo radio por tamaño de elemento */
:root{--r:18px;--r-m:14px;--r-s:10px}
.btn,.tabs button,.horas button,.plsel button,.chip-s,.chips button,.tg,.wbtns .btn,.stg .nav-f,.cin select,.field input,.toggle{border-radius:var(--r-s)}
.seg{border-radius:var(--r-s);overflow:hidden}
.thumbs button{border-radius:8px}
.demos,.calc,.ckp,.stats3,.desg,.dib,.plan,.p2d svg{border-radius:var(--r-m);overflow:hidden}
.split,.bar5{border-radius:8px;overflow:hidden}
.calc-tabs{border-radius:var(--r-m) var(--r-m) 0 0}
.calc-pie{border-radius:0 0 var(--r-m) var(--r-m)}
.ap{border:1px solid var(--border-color);border-radius:var(--r-m);padding:0 20px;margin-bottom:10px;background:rgba(255,255,255,.015)}
.ap:last-child{border-bottom:1px solid var(--border-color)}
.ap[open]{background:rgba(255,255,255,.03)}
.stg .fr{position:absolute;inset:auto;width:auto;height:auto;padding:0;object-fit:fill;border-radius:var(--r-m);box-shadow:0 24px 70px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.06)}
.slide .info .wbtns .btn{border-radius:var(--r-s)}
@media (min-width:901px){
 .info-p,.ctl{left:12px;top:12px;bottom:12px;width:calc(var(--pw) - 12px);border-radius:var(--r);border:1px solid var(--border-color);box-shadow:0 20px 60px rgba(0,0,0,.45)}
 .info-p{padding-top:24px}
 .ctl>div:first-child,.ctl>p:first-child{border-radius:var(--r) var(--r) 0 0}
 .stg .barra-i{left:calc(var(--pw) + 4px);right:12px;bottom:0;border-radius:0}
 .stg .nav-f.a{left:calc(var(--pw) + 12px)}
 .stg .nav-f.s{right:20px}
}
@media (max-width:900px){.info-p,.ctl{border-radius:var(--r-m) var(--r-m) 0 0}}
"""
cambia("</style>", css + "</style>") if s.count("</style>") == 1 else None
if "esquinas redondeadas" not in s:
    i = s.index("</style>")
    s = s[:i] + css + s[i:]

# la foto del carrusel se dimensiona a su tamaño real para que el redondeo siga el borde de la imagen
cambia("function foto(k){\n    fotoK=(k+N3)%N3;",
       """function ajustaFr(im){ var sg=$('#stg'); if(!sg||!im||!im.naturalWidth) return; var ip=$('.info-p',$('#pn3')), pw=innerWidth>900&&ip?ip.offsetWidth+12:0, aw=sg.clientWidth-pw-36, ah=sg.clientHeight-(innerWidth>900?112:100)-18, k=Math.min(aw/im.naturalWidth,ah/im.naturalHeight,1), w=im.naturalWidth*k, h=im.naturalHeight*k; im.style.width=w+'px'; im.style.height=h+'px'; im.style.left=(pw+18+(aw-w)/2)+'px'; im.style.top=(18+(ah-h)/2)+'px'; }
  function foto(k){
    fotoK=(k+N3)%N3;""")
cambia("a.onload=function(){ a.onload=null; a.classList.add('on');", "a.onload=function(){ a.onload=null; ajustaFr(a); a.classList.add('on');")
cambia("$('#stg-a0').src='photos/'+o.fotos[0][0]+'.jpg';", "$('#stg-a0').onload=function(){ ajustaFr(this); }; $('#stg-a0').src='photos/'+o.fotos[0][0]+'.jpg';")
cambia("nav3=N3>1?foto:null; nav3k=function(){return fotoK};",
       "nav3=N3>1?foto:null; nav3k=function(){return fotoK}; nav3aj=function(){ $$('.stg .fr',$('#pn3')).forEach(ajustaFr); };")
cambia("nav3=null, nav3k=null;", "nav3=null, nav3k=null, nav3aj=null;")
cambia("$('#v-cerrar').addEventListener('click',cierraVisor);", "$('#v-cerrar').addEventListener('click',cierraVisor);\naddEventListener('resize',function(){ if(nav3aj&&estado.visor&&panelActual==='3') nav3aj(); });")
p.write_text(s, encoding="utf-8")
print("ok")
