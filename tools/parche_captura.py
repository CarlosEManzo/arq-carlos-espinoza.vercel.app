"""Permite capturar fotogramas del visor 3D: con ?pdb en la URL el lienzo WebGL conserva su búfer.

Uso:  python tools/parche_captura.py   (idempotente)
"""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "dashboard" / "modelo.html"
s = p.read_text(encoding="utf-8")
if "/*pdb*/" in s:
    raise SystemExit("ya tiene el gancho de captura")
a = "\n(function(){\n'use strict';"
assert s.count(a) == 1
hook = "\n/*pdb*/if(/[?&]pdb/.test(location.search)){var __gc=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(t,o){if(/webgl/.test(t))o=Object.assign({},o,{preserveDrawingBuffer:true});return __gc.call(this,t,o);};}"
s = s.replace(a, hook + a)
p.write_text(s, encoding="utf-8")
print("ok")
