from PIL import Image, ImageDraw, ImageFont
FD="C:/Users/arqca/Documents/Obsidian/Contenido/Marca/Generador/fuentes/"
BG=(14,15,16); FG=(236,236,234); GR=(126,128,131); LN=(52,54,57); MG=(194,24,91)
W,H=1080,1920
mono=lambda s: ImageFont.truetype(FD+"JetBrainsMono.ttf",s)
def inter(s):
    f=ImageFont.truetype(FD+"Inter.ttf",s)
    try: f.set_variation_by_axes([32,800])
    except Exception: pass
    return f
logo=Image.open("C:/Users/arqca/Documents/Obsidian/Contenido/Marca/Logos/metricarq-blanco-punto-magenta.png").convert('RGBA')
def base(kicker,t1,t2):
    s=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(s)
    for r in range(700,0,-6):
        c=int(14+(1-r/700)**2*22); d.ellipse((W//2-r,420-r,W//2+r,420+r),fill=(c,c+1,c+2))
    d.text((80,110),kicker,font=mono(28),fill=GR)
    d.text((80,200),t1,font=inter(110),fill=FG); d.text((80,322),t2,font=inter(110),fill=GR)
    lw=300; lg=logo.resize((lw,int(logo.height*lw/logo.width)),Image.LANCZOS); s.paste(lg,(80,H-170),lg)
    d.text((W-480,H-140),"COTIZA POR MENSAJE →",font=mono(26),fill=FG)
    return s,d
def rows(d,items,y0,step):
    for i,(t,sub) in enumerate(items):
        y=y0+i*step
        d.line([(80,y-30),(W-80,y-30)],fill=LN,width=2)
        d.text((80,y),f"0{i+1}",font=mono(34),fill=MG)
        d.text((200,y-14),t,font=inter(58),fill=FG)
        yy=y+66
        for ln in sub: d.text((200,yy),ln,font=mono(30),fill=GR); yy+=44
s,d=base("SERVICIOS · METRIC.ARQ","LO QUE","HACEMOS.")
rows(d,[("Renders",["Fotorrealismo y ambientación."]),
        ("Modelo BIM y planos",["Planos arquitectónicos en Revit.","Levantamiento de lo existente."]),
        ("Control de obra",["Avance físico y financiero","en un solo tablero."]),
        ("Recorrido virtual",["Animación del proyecto","para redes y preventa."])],560,290)
s.save("historias/06-servicios.png")
s,d=base("PROCESO · METRIC.ARQ","CÓMO","TRABAJAMOS.")
rows(d,[("Me cuentas tu proyecto",["Por WhatsApp."]),
        ("Cotización y tiempos",["En 24 horas."]),
        ("Anticipo del 50 %",["Para iniciar."]),
        ("Entrega y saldo",["Entrega del proyecto y","pago del saldo restante."])],560,290)
s.save("historias/07-como-trabajamos.png")
sh=Image.new('RGB',(2*300+30,540+20),(30,30,30))
for i,n in enumerate(("06-servicios","07-como-trabajamos")): sh.paste(Image.open(f"historias/{n}.png").resize((300,533)),(10+i*310,10))
sh.save("vista-previa-3.png")
