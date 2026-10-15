from PIL import Image, ImageDraw, ImageFont, ImageOps
import math, os
FD="C:/Users/arqca/Documents/Obsidian/Contenido/Marca/Generador/fuentes/"
IMG="C:/Users/arqca/Desktop/ingresos-arq/landing/img/"
BG=(14,15,16); FG=(236,236,234); GR=(126,128,131); MG=(194,24,91)
K=3; W,H=1080,1920
mono=lambda s: ImageFont.truetype(FD+"JetBrainsMono.ttf",s)
def inter(s):
    f=ImageFont.truetype(FD+"Inter.ttf",s)
    try: f.set_variation_by_axes([32,800])
    except Exception: pass
    return f
def halo(im,cx,cy,R,amp=26):
    d=ImageDraw.Draw(im)
    for r in range(R,0,-6):
        c=int(14+(1-r/R)**2*amp); d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(c,c+1,c+2))
# ---------- portada PLANOS técnica (reemplaza la anterior)
im=Image.new('RGB',(W*K,H*K),BG); halo(im,W*K//2,H*K//2,460*K)
d=ImageDraw.Draw(im); cx,cy=W*K//2,H*K//2
d.ellipse((cx-400*K,cy-400*K,cx+400*K,cy+400*K),outline=FG,width=6*K)
def L(p,w=3,c=FG):
    d.line([(x*K,y*K) for x,y in p],fill=c,width=int(w*K))
def R(x1,y1,x2,y2,fill=None,out=None,w=3):
    d.rectangle((x1*K,y1*K,x2*K,y2*K),fill=fill,outline=out,width=int(w*K))
X,Y=cx//K,cy//K-15
x0,y0,x1,y1=X-200,Y-150,X+200,Y+150
t=14  # espesor de muro
# muros exteriores con poché (relleno) y línea doble
R(x0,y0,x1,y1,out=FG,w=3); R(x0+t,y0+t,x1-t,y1-t,fill=BG,out=FG,w=3)
for i in range(-300,420,9):  # achurado diagonal de muros
    pass
# poché sólido gris en muros
mask=Image.new('L',im.size,0); md=ImageDraw.Draw(mask)
md.rectangle((x0*K,y0*K,x1*K,y1*K),fill=255); md.rectangle(((x0+t)*K,(y0+t)*K,(x1-t)*K,(y1-t)*K),fill=0)
poche=Image.new('RGB',im.size,(70,72,75)); im.paste(poche,(0,0),mask); d=ImageDraw.Draw(im)
R(x0,y0,x1,y1,out=FG,w=3); R(x0+t,y0+t,x1-t,y1-t,out=FG,w=3)
# muro interior vertical y horizontal con poché
def wall(a,b,c,e):
    R(a,b,c,e,fill=(70,72,75),out=FG,w=3)
wall(X-8,y0+t,X+8,Y+10); wall(x0+t,Y+10,X-50,Y+26); wall(X+40,Y+10,x1-t,Y+26)
# vanos: puerta (hueco + arco) y ventanas
R(X-50,Y+8,X+40,Y+28,fill=BG); L([(X-50,Y+10),(X-50,Y+26)],3); L([(X+40,Y+10),(X+40,Y+26)],3)
L([(X-50,Y+18),(X+10,Y+18)],4); d.arc(((X-50-60)*K,(Y+18-60)*K,(X-50+60)*K,(Y+18+60)*K),270,360,fill=GR,width=3*K)
for (a,b,c,e) in [(X-140,y0,X-60,y0+t),(X+60,y0,X+140,y0+t),(x1-t,Y-70,x1,Y+0),(x0,Y-70,x0+t,Y+0)]:
    R(a,b,c,e,fill=BG,out=FG,w=2)
    if c-a>t: L([(a,(b+e)//2),(c,(b+e)//2)],2)
    else: L([((a+c)//2,b),((a+c)//2,e)],2)
# cotas con ticks (magenta) abajo y a la derecha
yy=y1+38
L([(x0,yy),(x1,yy)],3,MG)
for xx in (x0,X,x1): L([(xx-9,yy+9),(xx+9,yy-9)],3,MG)
L([(x0,y1+4),(x0,yy+14)],2,GR); L([(X,y1+4),(X,yy+14)],2,GR); L([(x1,y1+4),(x1,yy+14)],2,GR)
xx=x1+38
L([(xx,y0),(xx,y1)],3,MG)
for yv in (y0,y1): L([(xx-9,yv+9),(xx+9,yv-9)],3,MG)
# ejes con burbujas
for k,(ax) in enumerate((x0,x1)):
    L([(ax,y0-10),(ax,y0-45)],2,GR); d.ellipse(((ax-17)*K,(y0-80)*K,(ax+17)*K,(y0-46)*K),outline=FG,width=3*K)
    f=mono(26*K); tx="AB"[k]; w=d.textlength(tx,font=f); d.text((ax*K-w/2,(y0-63)*K-14*K),tx,font=f,fill=FG)
f=mono(60*K); tt=" ".join("PLANOS"); w=d.textlength(tt,font=f); d.text(((W*K-w)/2,H*K//2+470*K),tt,font=f,fill=GR)
im.resize((W,H),Image.LANCZOS).save("destacada-1-planos.png")

# ---------- historias con los materiales reales de la landing
logo=Image.open("C:/Users/arqca/Documents/Obsidian/Contenido/Marca/Logos/metricarq-blanco-punto-magenta.png").convert('RGBA')
def story(fn,kicker,t1,t2,sub,imgname,mode="fit",card=(80,360,1000,1260),white=False,fs=92):
    s=Image.new('RGB',(W,H),BG); halo(s,W//2,520,700,22); d=ImageDraw.Draw(s)
    d.text((80,110),kicker,font=mono(28),fill=GR)
    d.rounded_rectangle((card[0],card[1],card[2],card[3]),radius=28,fill=(245,245,243) if white else (24,25,27))
    cw,ch=card[2]-card[0],card[3]-card[1]
    pic=Image.open(IMG+imgname).convert('RGB')
    if mode=="cover": pic=ImageOps.fit(pic,(cw,ch),Image.LANCZOS)
    else:
        pic.thumbnail((cw-40,ch-40),Image.LANCZOS)
    m=Image.new('L',(cw,ch),0); ImageDraw.Draw(m).rounded_rectangle((0,0,cw-1,ch-1),radius=28,fill=255)
    canvas=Image.new('RGB',(cw,ch),(245,245,243) if white else (24,25,27))
    canvas.paste(pic,((cw-pic.width)//2,(ch-pic.height)//2)); s.paste(canvas,(card[0],card[1]),m)
    d.text((80,card[3]+70),t1,font=inter(fs),fill=FG)
    d.text((80,card[3]+70+int(fs*1.15)),t2,font=inter(fs),fill=GR)
    y=card[3]+310
    for ln in sub: d.text((80,y),ln,font=mono(30),fill=GR); y+=46
    lw=300; lg=logo.resize((lw,int(logo.height*lw/logo.width)),Image.LANCZOS)
    s.paste(lg,(80,H-170),lg)
    d.text((W-480,H-140),"COTIZA POR MENSAJE →",font=mono(26),fill=FG)
    s.save(fn)
os.makedirs("historias",exist_ok=True)
story("historias/01-planos.png","PLANO ARQUITECTÓNICO · LOFT 6×15","PLANO","ARQUITECTÓNICO.",["Distribución, áreas","y mobiliario."],"d-2d.jpg",card=(190,330,890,1290),fs=84)
story("historias/02-3d.png","MODELO 3D · BIM","MODELO","3D BIM.",["La casa completa en 3D,","modelada en Revit."],"d-3d.jpg",white=True,card=(80,360,1000,1100))
story("historias/03-obra.png","OBRA · AVANCE Y PRESUPUESTO","CONTROL","DE OBRA.",["Avance por semana","y presupuesto ejercido (ejemplo)."],"d-4d5d.jpg",card=(80,380,1000,1000))
story("historias/04-recorrido-360.png","RECORRIDO VIRTUAL 360°","RECORRIDO","360°.",["Entra al espacio","antes de construirlo."],"d-360.jpg",card=(80,420,1000,900))
story("historias/05-render.png","RENDER INTERIOR","RENDER","INTERIOR.",["Luz, materiales y ambiente","antes de la obra."],"d-render.jpg",mode="cover",card=(80,360,1000,1100))
# hoja de vista previa
names=["destacada-1-planos.png"]+["historias/"+n for n in sorted(os.listdir("historias"))]
ims=[Image.open(n).resize((216,384)) for n in names]
sh=Image.new('RGB',(226*len(ims)+10,404),(30,30,30))
for i,m in enumerate(ims): sh.paste(m,(10+i*226,10))
sh.save("vista-previa-2.png")
