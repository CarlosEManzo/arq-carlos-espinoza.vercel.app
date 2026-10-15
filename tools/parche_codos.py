"""Instalaciones del visor 3D: tramos con sus ejes reales y codos en las esquinas.

Antes cada tubo era un cilindro sobre el eje más largo de su caja envolvente: los tramos en diagonal salían
torcidos y, en cada giro de 90°, quedaba un hueco que hacía ver un circuito como dos líneas.
Ahora cada tramo usa el eje real (centro de sus dos anillos de vértices); los extremos cercanos del mismo
sistema y diámetro se prolongan hasta la esquina y llevan una esfera de codo; si no se cruzan, un tramo los une.

Uso:  python tools/parche_codos.py   (idempotente)
"""
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "dashboard" / "modelo.html"
s = p.read_text(encoding="utf-8")
if "/*codos*/" in s:
    raise SystemExit("modelo.html ya tiene los codos")

i = s.index("infra.forEach(function(e){var g=geoDe(e),b=g.boundingBox")
fin = "infraMeshes.push(sp);});});"
j = s.index(fin, i) + len(fin)

nuevo = r"""/*codos*/
(function(){
  var SG=[];
  infra.forEach(function(e){var v=e.v,n=v.length/3,h=n>>1,a=new T.Vector3(),b=new T.Vector3(),k;
    for(k=0;k<h;k++)a.add(new T.Vector3(v[k*3]/1000,v[k*3+2]/1000,-v[k*3+1]/1000));
    for(k=h;k<n;k++)b.add(new T.Vector3(v[k*3]/1000,v[k*3+2]/1000,-v[k*3+1]/1000));
    a.divideScalar(h);b.divideScalar(n-h);
    SG.push({e:e,a:a,b:b,r:Math.min(Math.max((e.diam||13)/2000*(e.cat==='Conduit'?2.2:3.6),0.012),0.06),g:grupoInfra(e),col:colorInfra(e),fit:[]});});
  var TOL=0.3,puentes=[];
  function esquina(x,ex,y,ey){ /* punto donde se cruzan los ejes de x e y */
    var p=ex?x.b:x.a,q=ey?y.b:y.a,da=x.b.clone().sub(x.a),db=y.b.clone().sub(y.a),w=p.clone().sub(q);
    var A=da.dot(da),B=da.dot(db),C=db.dot(db),D=da.dot(w),E=db.dot(w),den=A*C-B*B;if(Math.abs(den)<1e-9*A*C||A<1e-9||C<1e-9)return null;
    var t1=(B*E-C*D)/den,t2=(A*E-B*D)/den,c1=p.clone().addScaledVector(da,t1),c2=q.clone().addScaledVector(db,t2);
    if(c1.distanceTo(c2)>0.06||c1.distanceTo(p)>TOL||c2.distanceTo(q)>TOL)return null;return c1.add(c2).multiplyScalar(0.5);}
  SG.forEach(function(x,i){[0,1].forEach(function(ex){
    if(x.fit[ex])return;var p=ex?x.b:x.a,best=null;
    SG.forEach(function(y,k){if(k===i||y.g!==x.g||y.e.diam!==x.e.diam)return;[0,1].forEach(function(ey){if(y.fit[ey])return;var q=ey?y.b:y.a,d=p.distanceTo(q);if(d<TOL&&(!best||d<best.d))best={y:y,ey:ey,d:d};});});
    if(!best)return;var y=best.y,ey=best.ey,q=ey?y.b:y.a;
    if(best.d<0.004){x.fit[ex]=y.fit[ey]=true;return;}
    var c=esquina(x,ex,y,ey);
    if(c){(ex?x.b:x.a).copy(c);(ey?y.b:y.a).copy(c);x.fit[ex]=y.fit[ey]=true;}
    else{puentes.push({a:p.clone(),b:q.clone(),r:x.r,g:x.g,col:x.col});x.fit[ex]=y.fit[ey]=true;}});});
  var Y=new T.Vector3(0,1,0);
  function tubo(a,b,r,g,col,esfA,esfB){var d=b.clone().sub(a),len=d.length();if(len<1e-4)return;
    var mat=new T.MeshBasicMaterial({color:col,transparent:true,opacity:.95}),m=new T.Mesh(new T.CylinderGeometry(r,r,len,8),mat);
    m.position.copy(a).add(b).multiplyScalar(0.5);m.quaternion.setFromUnitVectors(Y,d.normalize());m.userData={grupo:g,rol:'infra'};m.visible=false;root.add(m);infraMeshes.push(m);
    [[a,esfA],[b,esfB]].forEach(function(q){var sp=new T.Mesh(new T.SphereGeometry(r*q[1],10,8),mat);sp.position.copy(q[0]);sp.userData=m.userData;sp.visible=false;root.add(sp);infraMeshes.push(sp);});}
  SG.forEach(function(x){tubo(x.a,x.b,x.r,x.g,x.col,x.fit[0]?1.18:1.05,x.fit[1]?1.18:1.05);});
  puentes.forEach(function(q){tubo(q.a,q.b,q.r,q.g,q.col,1.18,1.18);});
})();"""

s = s[:i] + nuevo + s[j:]
p.write_text(s, encoding="utf-8")
print("ok")
