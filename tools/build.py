"""Genera index.html a partir de src/pagina.html y revisa que estén todas las fotos que usa.

Uso:  python tools/build.py [URL_BASE]
URL_BASE por defecto: https://arq-carlos-espinoza.vercel.app
"""
import re
import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
base = (sys.argv[1] if len(sys.argv) > 1 else "https://arq-carlos-espinoza.vercel.app").rstrip("/")
fuente = raiz / "src" / "pagina.html"
pagina = fuente.read_text(encoding="utf-8")

# ---- fotos usadas: galerías [id, título, alt] y fondos (heroes) ----
ids = set(re.findall(r"\['([a-z0-9-]+)','[^']*','[^']*'\]", pagina))
for m in re.finditer(r"heroes:\[([^\]]*)\]", pagina):
    ids |= set(re.findall(r"'([a-z0-9-]+)'", m.group(1)))
destino = raiz / "photos"
faltan = [i for i in sorted(ids) if not (destino / f"{i}.jpg").exists()]
if faltan:
    sys.exit("Faltan fotos en photos/: " + ", ".join(faltan))
sobran = sorted(p.stem for p in destino.glob("*.jpg") if p.stem not in ids)
if sobran:
    print("Aviso: fotos sin usar en photos/:", ", ".join(sobran))

# ---- cabecera del documento (en el artifact la ponía la plataforma) ----
titulo = re.search(r"<title>(.*?)</title>", pagina).group(1)
pagina = re.sub(r"<title>.*?</title>\s*", "", pagina, count=1)
desc = ("Portafolio de Carlos Espinoza, arquitecto en Morelia: estructuras metálicas, coordinación BIM, "
        "obra industrial y renders, con maquetas 3D, planos y una calculadora de instalaciones.")
favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' fill='%230D0D0D'/%3E%3Cpath d='M14 50V14h12l12 22V14h12v36H38L26 28v22z' fill='%23fff'/%3E%3C/svg%3E")
cabecera = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0D0D0D">
<link rel="icon" href="{favicon}">
<link rel="canonical" href="{base}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}/">
<meta property="og:image" content="{base}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{titulo}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{base}/og.jpg">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
"""
# el documento original arranca con <link>/<style> sueltos y termina con scripts: se envuelve tal cual
html = cabecera + "</head>\n<body>\n" + pagina + "\n</body>\n</html>\n"
(raiz / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB ·", len(ids), "fotos usadas")
