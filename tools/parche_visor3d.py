"""Ventana «Maqueta 3D»: pantalla completa con los controles encima (panel de vidrio a la izquierda, igual que Información),
modo de luz con iconos (mañana, mediodía y atardecer) y una escena con más profundidad (cielo con degradado, suelo con luz, sombra de contacto,
luz de relleno y niebla del color del horizonte). Se ejecuta una sola vez sobre src/pagina.html."""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "src" / "pagina.html"
s = p.read_text(encoding="utf-8")


def cambia(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90])
    s = s.replace(a, b)


def quita_linea(inicio):
    global s
    i = s.index(inicio)
    j = s.index("\n", i)
    s = s[:i] + s[j + 1:]


# ---------------- CSS: se retiran las reglas del panel inferior ----------------
for ini in [".tri .ctl{grid-template-columns:1fr 1fr}", ".tri .p3d{grid-template-rows", ".tri .ctl input[type=range]{height:22px}", ".tri .horas button{min-height:32px", ".tri .chip-s{min-height:30px",
            ".tri .ctl>div:first-child{grid-column:1/-1}", ".tri .ctl>div{padding:8px 14px;gap:4px}", ".tri .ctl .muted{display:none}", ".tri .esq{left:14px;max-width:34ch}",
            " .tri .ctl{grid-template-columns:repeat(3,minmax(0,1fr))}", " .tri .ctl>div:first-child{grid-column:auto}", " .tri .ctl .muted{display:inline}",
            ".p3d{display:grid;grid-template-rows:minmax(0,1fr) auto}", ".ctl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))",
            ".ctl>div{background:var(--card-bg);padding:12px var(--gut)", ".ctl label,.ctl .lbl{font-family", ".ctl label output{color", ".ctl input[type=range]{width:100%",
            ".horas{display:flex;gap:6px;flex-wrap:wrap}", ".horas button{font-family", ".horas button[aria-pressed=\"true\"]{background", ".ctl>div.sis{grid-column:1/-1"]:
    quita_linea(ini)
cambia("@media (max-width:900px){.tri .esq{display:none}.vhead .tabs", "@media (max-width:900px){.vhead .tabs")
cambia("@media (max-width:820px){.ctl{grid-template-columns:1fr 1fr}.ctl>div:first-child{grid-column:1/-1}.ctl>div{padding:8px var(--gut);gap:4px}.ctl .muted{display:none}.esq{display:none}.ctl{max-height:36vh;overflow-y:auto}.ctl>div.sis{flex-wrap:nowrap}.chips-s{flex-wrap:nowrap;overflow-x:auto;padding-bottom:4px}.chip-s{flex:none}.vhead{padding:8px var(--gut);gap:8px}",
       "@media (max-width:820px){.vhead{padding:8px var(--gut);gap:8px}")
cambia(".canvasbox{position:relative;min-height:0;overflow:hidden}", ".canvasbox{position:absolute;inset:0;overflow:hidden}")
cambia(".esq{position:absolute;left:var(--gut);top:12px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);max-width:60ch;pointer-events:none}",
       """.p3d{position:relative;overflow:hidden;--pw:min(430px,40%)}
.esq{margin:0;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);line-height:1.6}
.ctl{position:absolute;left:0;top:0;bottom:0;width:var(--pw);overflow:auto;background:rgba(13,13,13,.74);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-right:1px solid var(--border-color);display:flex;flex-direction:column;z-index:2}
.ctl>div,.ctl>p{margin:0;padding:18px 24px 18px var(--gut);border-bottom:1px solid var(--border-color);display:flex;flex-direction:column;gap:10px}
.ctl label,.ctl .lbl{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);display:flex;justify-content:space-between;gap:8px}
.ctl label output{color:var(--text-main)}
.ctl input[type=range]{width:100%;accent-color:#fff;height:28px;background:transparent}
.horas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.horas button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;background:rgba(13,13,13,.5);border:1px solid var(--border-color);color:var(--text-muted);padding:10px 4px;min-height:68px;transition:all .5s var(--ease)}
.horas button .ic{width:28px;height:28px;stroke-width:1.5}
.horas button:hover{color:var(--text-main);border-color:var(--text-muted)}
.horas button[aria-pressed="true"]{background:var(--accent);color:var(--bg-dark);border-color:var(--accent)}
.ctl .nota{font-size:12px;color:var(--text-muted)}
@media (max-width:900px){
 .p3d{--pw:0px;display:flex;flex-direction:column;overflow-y:auto}
 .canvasbox{position:relative;inset:auto;flex:none;height:min(58vh,460px)}
 .ctl{position:static;width:auto;overflow:visible;background:var(--bg-dark);border-right:0;border-top:1px solid var(--border-color)}
 .ctl>div,.ctl>p{padding:14px var(--gut)}
}""")

# ---------------- HTML: panel de controles ----------------
i0 = s.index('    <section class="pane" role="region" aria-label="Maqueta 3D">')
i1 = s.index('    <section class="pane" role="region" aria-label="Planos e instalaciones">')
nuevo = '''    <section class="pane" role="region" aria-label="Maqueta 3D"><header class="plab"><svg class="ic" aria-hidden="true"><use href="#i-cubo"/></svg>02 · Maqueta 3D</header><div class="p3d" id="pn1">
      <div class="canvasbox" id="cbox">
        <div class="sin3d" id="sin3d"><p>No se pudo iniciar el visor 3D en este navegador.<br>La información y los planos siguen disponibles.</p></div>
      </div>
      <div class="ctl">
        <p class="esq">Maqueta esquemática ilustrativa. No es el modelo del proyecto. Arrastra para rotar, rueda o pellizco para acercar.</p>
        <div><span class="lbl"><svg class="ic" aria-hidden="true"><use href="#i-sol"/></svg>Luz del día</span>
          <div class="horas" role="group" aria-label="Momento del día">
            <button type="button" data-h="8" aria-pressed="false"><svg class="ic" aria-hidden="true"><use href="#i-amanecer"/></svg>Mañana</button>
            <button type="button" data-h="12" aria-pressed="true"><svg class="ic" aria-hidden="true"><use href="#i-sol"/></svg>Mediodía</button>
            <button type="button" data-h="17" aria-pressed="false"><svg class="ic" aria-hidden="true"><use href="#i-atardecer"/></svg>Atardecer</button>
          </div>
          <label for="hora">Hora <output id="hora-o">12:00 h · elev. 65°</output></label><input type="range" id="hora" min="6.5" max="17.5" step="0.25" value="12">
        </div>
        <div><label for="despiece"><span><svg class="ic" aria-hidden="true"><use href="#i-despiece"/></svg>Despiece</span> <output id="despiece-o">0 %</output></label><input type="range" id="despiece" min="0" max="100" step="1" value="0"><span class="nota">Separa los componentes por capas constructivas.</span></div>
        <div><label for="corte"><span><svg class="ic" aria-hidden="true"><use href="#i-corte"/></svg>Corte</span> <output id="corte-o">sin corte</output></label><input type="range" id="corte" min="0" max="100" step="1" value="0"><span class="nota">Rebana el volumen para ver su interior.</span></div>
        <div class="sis"><span class="lbl"><svg class="ic" aria-hidden="true"><use href="#i-gota"/></svg>Instalaciones</span><div class="chips-s" id="sis-chips" role="group" aria-label="Instalaciones visibles"></div></div>
      </div>
    </div></section>
'''
s = s[:i0] + nuevo + s[i1:]

# iconos nuevos
cambia('<symbol id="i-despiece"', '<symbol id="i-amanecer" viewBox="0 0 24 24"><path d="M3 19h18 M6.2 19a5.8 5.8 0 0 1 11.6 0 M12 6.5v3 M4.6 11.6l2 2 M19.4 11.6l-2 2 M9.5 5.5L12 3l2.5 2.5"/></symbol>\n<symbol id="i-atardecer" viewBox="0 0 24 24"><path d="M3 19h18 M6.2 19a5.8 5.8 0 0 1 11.6 0 M12 3v3.5 M4.6 11.6l2 2 M19.4 11.6l-2 2 M9.5 5L12 7.5 14.5 5"/></symbol>\n<symbol id="i-despiece"')

# ---------------- JS: escena con profundidad ----------------
cambia("V.scene=new THREE.Scene(); V.scene.background=new THREE.Color(0x0d0d0d); V.scene.fog=new THREE.Fog(0x0d0d0d,45,130);",
       "V.scene=new THREE.Scene(); V.scene.background=new THREE.Color(0x0d0d0d); V.scene.fog=new THREE.Fog(0x0d0d0d,45,130); V.skyC=document.createElement('canvas'); V.skyC.width=4; V.skyC.height=256; V.skyT=new THREE.CanvasTexture(V.skyC); V.skyT.encoding=THREE.sRGBEncoding;")
cambia("V.scene.add(new THREE.HemisphereLight(0x8a90a0,0x0d0d0d,.22));",
       "V.hemi=new THREE.HemisphereLight(0x8a90a0,0x1a1a1a,.4); V.scene.add(V.hemi); V.fill=new THREE.DirectionalLight(0x8fa6d8,.3); V.scene.add(V.fill,V.fill.target);")
cambia("var ground=new THREE.Mesh(new THREE.PlaneGeometry(500,500),new THREE.MeshStandardMaterial({color:0x0b0b0b,roughness:1})); ground.rotation.x=-Math.PI/2; ground.position.y=-.02; ground.receiveShadow=true; V.scene.add(ground);",
       """var gc=document.createElement('canvas'); gc.width=gc.height=256; var gg=gc.getContext('2d'), gr=gg.createRadialGradient(128,128,10,128,128,128); gr.addColorStop(0,'#3a3a3b'); gr.addColorStop(.45,'#232324'); gr.addColorStop(1,'#101011'); gg.fillStyle=gr; gg.fillRect(0,0,256,256);
    var gt=new THREE.CanvasTexture(gc); gt.encoding=THREE.sRGBEncoding;
    V.ground=new THREE.Mesh(new THREE.PlaneGeometry(1,1),new THREE.MeshStandardMaterial({map:gt,roughness:1,metalness:0})); V.ground.rotation.x=-Math.PI/2; V.ground.position.y=-.02; V.ground.receiveShadow=true; V.scene.add(V.ground);
    var bc=document.createElement('canvas'); bc.width=bc.height=128; var bg=bc.getContext('2d'), br=bg.createRadialGradient(64,64,4,64,64,64); br.addColorStop(0,'rgba(0,0,0,.65)'); br.addColorStop(.6,'rgba(0,0,0,.28)'); br.addColorStop(1,'rgba(0,0,0,0)'); bg.fillStyle=br; bg.fillRect(0,0,128,128);
    V.blob=new THREE.Mesh(new THREE.PlaneGeometry(1,1),new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(bc),transparent:true,depthWrite:false})); V.blob.rotation.x=-Math.PI/2; V.blob.position.y=.01; V.scene.add(V.blob);""")
cambia("V.ren.toneMappingExposure=.8;", "V.ren.toneMappingExposure=.95;")
cambia("V.edgeMat=new THREE.LineBasicMaterial({color:0xffffff,transparent:true,opacity:.16,", "V.edgeMat=new THREE.LineBasicMaterial({color:0xffffff,transparent:true,opacity:.22,")
cambia("var grid=new THREE.GridHelper(160,80,0x2c2c2c,0x191919); grid.position.y=0; V.scene.add(grid);", "var grid=new THREE.GridHelper(160,80,0x2f2f30,0x1c1c1d); grid.position.y=0; grid.material.transparent=true; grid.material.opacity=.55; V.scene.add(grid);")

# tam(): el modelo queda centrado en el área libre a la derecha del panel
cambia("V.ren.setSize(w,h,false); V.cam.aspect=w/h; V.cam.updateProjectionMatrix(); }",
       "V.ren.setSize(w,h,false); V.cam.aspect=w/h; var pn=$('#pn1 .ctl'), d=(innerWidth>900&&pn)?pn.offsetWidth/2:0; if(d) V.cam.setViewOffset(w,h,-d,0,w,h); else V.cam.clearViewOffset(); V.cam.updateProjectionMatrix(); }")
# suelo y sombra de contacto a la medida del modelo
cambia("  V.tyBase=V.orb.t.y; V.maxOff=Math.max(0,m.ey(b.mx[1])); V.tPrev=0;",
       "  V.ground.scale.set(size*6,size*6,1); V.ground.position.x=V.orb.t.x; V.ground.position.z=V.orb.t.z; var fx0=b.mx[0]-b.mn[0], fz0=b.mx[2]-b.mn[2]; V.blob.scale.set(fx0*1.5+6,fz0*1.5+6,1); V.blob.position.x=V.orb.t.x; V.blob.position.z=V.orb.t.z;\n  V.tyBase=V.orb.t.y; V.maxOff=Math.max(0,m.ey(b.mx[1])); V.tPrev=0;")

# ponHora: color del cielo, del sol, de la niebla y de las luces según la hora
i0 = s.index("function ponHora(h){")
i1 = s.index("function aplicaDespiece(){")
nuevo_js = r'''var CIELO=[[8,{top:'#26324a',hor:'#b9825e',sol:0xffd2a1,si:.95,hs:0x8b93a8,hg:0x2a211c,hi:.4,fill:0x9fb4dc}],[12,{top:'#22375a',hor:'#7f95b6',sol:0xfff3e0,si:1.5,hs:0xa9bbd6,hg:0x2d2d2f,hi:.5,fill:0x8fa6d8}],[17,{top:'#1f2238',hor:'#cf774a',sol:0xff9a5c,si:1.0,hs:0x8a7f9a,hg:0x2a1e1a,hi:.36,fill:0x7d86c4}]];
function mezcla(a,b,t){ var A=new THREE.Color(a),B=new THREE.Color(b); return A.lerp(B,t); }
function estiloHora(h){
  var k0=CIELO[0],k1=CIELO[1],t; if(h<=8){k1=k0;t=0} else if(h<=12){t=(h-8)/4} else if(h<17){k0=CIELO[1];k1=CIELO[2];t=(h-12)/5} else {k0=k1=CIELO[2];t=0}
  var a=k0[1], b=k1[1]; if(h>12&&h<17){ }
  var top=mezcla(a.top,b.top,t), hor=mezcla(a.hor,b.hor,t), sol=new THREE.Color(a.sol).lerp(new THREE.Color(b.sol),t), hs=new THREE.Color(a.hs).lerp(new THREE.Color(b.hs),t), hg=new THREE.Color(a.hg).lerp(new THREE.Color(b.hg),t), fl=new THREE.Color(a.fill).lerp(new THREE.Color(b.fill),t);
  return {top:top,hor:hor,sol:sol,si:a.si+(b.si-a.si)*t,hs:hs,hg:hg,hi:a.hi+(b.hi-a.hi)*t,fill:fl};
}
function ponHora(h){
  V.hora=h; var t=(h-6)/12, el=Math.max(.1,Math.sin(Math.PI*t))*(65*Math.PI/180), az=Math.PI*t, R=(V.size||30)*3, st=estiloHora(h);
  if(V.sun&&V.orb.t){ V.sun.position.set(V.orb.t.x+Math.cos(az)*Math.cos(el)*R,V.orb.t.y+Math.sin(el)*R,V.orb.t.z+Math.sin(az)*Math.cos(el)*R); V.sun.target.position.copy(V.orb.t); V.sun.color.copy(st.sol); V.sun.intensity=(.35+Math.sin(el)*.9)*st.si/1.2;
    V.fill.position.set(V.orb.t.x-Math.cos(az)*R*.8,V.orb.t.y+R*.35,V.orb.t.z-Math.sin(az)*R*.8+R*.3); V.fill.target.position.copy(V.orb.t); V.fill.color.copy(st.fill); }
  if(V.hemi){ V.hemi.color.copy(st.hs); V.hemi.groundColor.copy(st.hg); V.hemi.intensity=st.hi; }
  if(V.skyC){ var cx=V.skyC.getContext('2d'), gr=cx.createLinearGradient(0,0,0,256); gr.addColorStop(0,'#'+st.top.getHexString()); gr.addColorStop(.62,'#'+st.hor.clone().lerp(st.top,.25).getHexString()); gr.addColorStop(1,'#'+st.hor.getHexString()); cx.fillStyle=gr; cx.fillRect(0,0,4,256); V.skyT.needsUpdate=true; V.scene.background=V.skyT; if(V.scene.fog) V.scene.fog.color.copy(st.hor).multiplyScalar(.7); }
  var hh=Math.floor(h), mm=Math.round((h-hh)*60); $('#hora-o').textContent=('0'+hh).slice(-2)+':'+('0'+mm).slice(-2)+' h · elev. '+Math.round(el*180/Math.PI)+'°';
  $('#hora').value=h; $$('.horas button').forEach(function(b){b.setAttribute('aria-pressed',Math.abs(parseFloat(b.dataset.h)-h)<.01?'true':'false')});
}
'''
s = s[:i0] + nuevo_js + s[i1:]
p.write_text(s, encoding="utf-8")
print("ok")
