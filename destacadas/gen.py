from PIL import Image, ImageDraw, ImageFont
import math
F="C:/Users/arqca/Documents/Obsidian/Contenido/Marca/Generador/fuentes/JetBrainsMono.ttf"
BG=(14,15,16); FG=(236,236,234); GR=(126,128,131); MG=(194,24,91)
K=3; W,H=1080,1920
def base():
    im=Image.new('RGB',(W*K,H*K),BG); d=ImageDraw.Draw(im)
    cx,cy=W*K//2,H*K//2
    for r in range(460*K,0,-6*K):
        c=int(14+(1-r/(460*K))**2*26); d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(c,c+1,c+2))
    d.ellipse((cx-400*K,cy-400*K,cx+400*K,cy+400*K),outline=FG,width=6*K)
    return im,d,cx,cy
def line(d,pts,w=10,col=FG,close=False):
    p=[(x*K,y*K) for x,y in pts]
    if close:p.append(p[0])
    d.line(p,fill=col,width=w*K,joint='curve')
    for x,y in p: d.ellipse((x-w*K/2,y-w*K/2,x+w*K/2,y+w*K/2),fill=col)
def label(d,t):
    f=ImageFont.truetype(F,60*K); t=" ".join(t)
    w=d.textlength(t,font=f); d.text(((W*K-w)/2,(H*K//2)+470*K),t,font=f,fill=GR)
def save(im,n): im.resize((W,H),Image.LANCZOS).save(n)

# PLANOS: plan view with walls, door arc, dimension line
im,d,cx,cy=base(); x0,y0=cx//K-190,cy//K-150
line(d,[(x0,y0),(x0+380,y0),(x0+380,y0+300),(x0,y0+300)],12,FG,True)
line(d,[(x0+190,y0),(x0+190,y0+170)],10)
line(d,[(x0,y0+170),(x0+120,y0+170)],10)
line(d,[(x0+190,y0+170),(x0+380,y0+170)],10)
d.arc(((x0+120)*K,(y0+50)*K,(x0+190)*K+70*K,(y0+170)*K+70*K),0,0,fill=FG)  # noop
d.arc(((x0+120)*K,(y0+100)*K,(x0+190)*K,(y0+240)*K),270,360,fill=GR,width=6*K)
line(d,[(x0,y0+350),(x0+380,y0+350)],6,MG); line(d,[(x0,y0+335),(x0,y0+365)],6,MG); line(d,[(x0+380,y0+335),(x0+380,y0+365)],6,MG)
label(d,"PLANOS"); save(im,"destacada-1-planos.png")

# 3D: isometric cube wireframe + hidden edges
im,d,cx,cy=base(); c=(cx//K,cy//K-10); s=170
def iso(x,y,z): return (c[0]+(x-y)*s*0.866, c[1]+(x+y)*s*0.5 - z*s)
V={(a,b,z):iso(a-.5,b-.5,z-.5) for a in(0,1) for b in(0,1) for z in(0,1)}
vis=[((0,0,1),(1,0,1)),((1,0,1),(1,1,1)),((1,1,1),(0,1,1)),((0,1,1),(0,0,1)),((1,0,0),(1,0,1)),((1,1,0),(1,1,1)),((0,1,0),(0,1,1)),((1,0,0),(1,1,0)),((1,1,0),(0,1,0))]
for a,b in vis: line(d,[V[a],V[b]],12)
for a,b in [((0,0,0),(1,0,0)),((0,0,0),(0,1,0)),((0,0,0),(0,0,1))]: line(d,[V[a],V[b]],6,GR)
d.ellipse((V[(0,0,1)][0]*K-14*K,V[(0,0,1)][1]*K-14*K,V[(0,0,1)][0]*K+14*K,V[(0,0,1)][1]*K+14*K),fill=MG)
label(d,"3D"); save(im,"destacada-2-3d.png")

# OBRA: tower crane + frame structure
im,d,cx,cy=base(); X,Y=cx//K,cy//K
line(d,[(X-120,Y+200),(X-120,Y-210)],12)            # mast
line(d,[(X-120,Y-210),(X+190,Y-210)],12); line(d,[(X-120,Y-210),(X-210,Y-210)],12)  # jib/counter
line(d,[(X-120,Y-260),(X-120,Y-210)],12); line(d,[(X-120,Y-260),(X+100,Y-210)],6,GR); line(d,[(X-120,Y-260),(X-210,Y-210)],6,GR)
line(d,[(X+130,Y-210),(X+130,Y-90)],6); d.rectangle(((X+110)*K,(Y-90)*K,(X+150)*K,(Y-60)*K),fill=MG)
for i in range(4): yy=Y-130+i*0+0
line(d,[(X-60,Y+200),(X+230,Y+200)],12)
for x in (X-40,X+90,X+220):
    line(d,[(x,Y+200),(x,Y+30)],10)
line(d,[(X-40,Y+30),(X+220,Y+30)],10); line(d,[(X-40,Y+115),(X+220,Y+115)],8,GR)
label(d,"OBRA"); save(im,"destacada-3-obra.png")

# 360: ellipse orbit with arrowhead + panorama sphere + text
im,d,cx,cy=base(); X,Y=cx//K,cy//K
d.ellipse(((X-260)*K,(Y-110)*K,(X+260)*K,(Y+110)*K),outline=FG,width=12*K)
d.ellipse(((X-150)*K,(Y-150)*K,(X+150)*K,(Y+150)*K),outline=GR,width=6*K)
d.arc(((X-150)*K,(Y-60)*K,(X+150)*K,(Y+60)*K),0,360,fill=GR,width=4*K)
d.line([(X*K,(Y-150)*K),(X*K,(Y+150)*K)],fill=GR,width=4*K)
ax,ay=X+255,Y+18
d.polygon([((ax-34)*K,(ay-34)*K),((ax+30)*K,(ay-6)*K),((ax-26)*K,(ay+44)*K)],fill=MG)
f=ImageFont.truetype(F,120*K); t="360°"; w=d.textlength(t,font=f); d.text((X*K-w/2,(Y+170)*K),t,font=f,fill=FG)
label(d,"RECORRIDO 360"); save(im,"destacada-4-360.png")

# contact sheet
ims=[Image.open(f"destacada-{i}.png").resize((270,480)) for i in ("1-planos","2-3d","3-obra","4-360")]
sh=Image.new('RGB',(270*4+50,480+20),(30,30,30))
for i,m in enumerate(ims): sh.paste(m,(10+i*280,10))
sh.save("vista-previa.png")
