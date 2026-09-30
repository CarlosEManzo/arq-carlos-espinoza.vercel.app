"""Genera og.jpg (tarjeta que se ve al compartir el enlace) a partir de photos/tel-01.jpg."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

raiz = Path(__file__).resolve().parent.parent
im = Image.open(raiz / "photos" / "tel-01.jpg").convert("RGB")
W, H = 1200, 630
r = max(W / im.width, H / im.height)
im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
x, y = (im.width - W) // 2, (im.height - H) // 2
im = ImageEnhance.Brightness(im.crop((x, y, x + W, y + H))).enhance(.5)
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)
for i in range(H):
    d.line([(0, i), (W, i)], fill=(13, 13, 13, int(225 * (i / H) ** 1.5)))
im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
d = ImageDraw.Draw(im)
f = lambda n, s: ImageFont.truetype("C:/Windows/Fonts/" + n, s)
d.text((64, 330), "CARLOS FRANCISCO", font=f("arialbd.ttf", 76), fill=(240, 240, 240))
d.text((64, 415), "ESPINOZA MANZO", font=f("arialbd.ttf", 76), fill=(240, 240, 240))
d.text((66, 520), "ARQUITECTO · ESTRUCTURAS METÁLICAS · COORDINACIÓN BIM", font=f("consola.ttf", 26), fill=(190, 190, 190))
d.text((66, 560), "MORELIA, MICHOACÁN  ·  PORTAFOLIO", font=f("consola.ttf", 22), fill=(140, 140, 140))
im.save(raiz / "og.jpg", quality=88, optimize=True)
print("og.jpg listo")
