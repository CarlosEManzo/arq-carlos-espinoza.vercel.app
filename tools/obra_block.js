
/* ---------------- obra: secuencia constructiva real (4D) ---------------- */
/* trazo, excavación, plantilla, zapatas con armado, cimiento, relleno, firme, castillos, muros de block, cimbra y losas */
var OBRA=new T.Group();OBRA.visible=false;scene.add(OBRA);
var TIERRA=new T.Group();TIERRA.visible=false;scene.add(TIERRA);
var OBP=[],OBTR=[],OBBLK=null;
function sm(a,b,p){return Math.max(0,Math.min(1,(p-a)/(b-a)));}
(function(){
  var P=function(x,y,z){return new T.Vector3(x,z,-y);};
  var mTierra=std('#6e5742',1),
      mPlant=std('#b3afa6',1),mPiedra=new T.MeshStandardMaterial({map:texRuido('#8a867e',70),roughness:1}),
      mCons=new T.MeshStandardMaterial({map:texRuido('#9a978f',50),roughness:.95}),mCast=std('#c9c6bd',.95),
      mCimb=std('#c9a46a',.8),mPunt=std('#a67b47',.9),mCal=std('#f2f2ee',1),mEstaca=std('#c9a23d',.8),
      mPal=std('#9b9892',1),mArena=std('#c2a878',1),mGrava=std('#8f8e8a',1),
      lRebar=new T.LineBasicMaterial({color:0xc0653a}),lHilo=new T.LineBasicMaterial({color:0xe6d34a});
  OBBLK=new T.MeshStandardMaterial({map:canvasTex(function(g,s){g.fillStyle='#7d7a74';g.fillRect(0,0,s,s);var rows=12,bh=s/rows,bw=s/6;for(var r=0;r<rows;r++)for(var k=-1;k<6;k++){var v=Math.abs(rnd(r*17+k*5))*22-11,x=k*bw+(r%2?bw/2:0);g.fillStyle=shade('#9b9892',v);g.fillRect(x+1.5,r*bh+1.5,bw-3,bh-3);}},512),roughness:1});
  function add(o,a,b,gr,grp){(grp||OBRA).add(o);o.castShadow=true;o.receiveShadow=true;OBP.push({o:o,a:a,b:b,g:gr||null});return o;}
  function box(w,h,d,x,yb,z,mat,fromBottom){var g=new T.BoxGeometry(w,h,d);g.translate(0,fromBottom?h/2:0,0);var m=new T.Mesh(g,mat);m.position.set(x,yb,z);return m;}
  function lineas(arr,mat,a,b){var g=new T.BufferGeometry();g.setAttribute('position',new T.Float32BufferAttribute(arr,3));var l=new T.LineSegments(g,mat);OBRA.add(l);OBP.push({o:l,a:a,b:b});}
  /* ejes de muros en planta (x0,y0,x1,y1,tipo): c = carga 15 cm, b = barda de block */
  var SEG=[[0,4.5,0,12,'c'],[6,4.5,6,12,'c'],[0,12,6,12,'c'],[0,4.5,1.5,4.5,'c'],[5.25,4.5,6,4.5,'c'],
    [0,0,0,4.5,'b'],[6,0,6,4.5,'b'],[0,12,0,15,'b'],[6,12,6,15,'b'],[0,15,6,15,'b'],[0,0,1.2,0,'b'],[4.2,0,6,0,'b']];
  /* ---- tierra con zanjas ---- */
  var rects=[],XB=[-4,10],YB=[-3,18];
  SEG.forEach(function(s){var c=s[4]==='c',w=c?0.9:0.7,hz=s[1]===s[3];
    rects.push(hz?[Math.min(s[0],s[2])-w/2,Math.max(s[0],s[2])+w/2,s[1]-w/2,s[1]+w/2]:[s[0]-w/2,s[0]+w/2,Math.min(s[1],s[3])-w/2,Math.max(s[1],s[3])+w/2]);});
  var xs=XB.concat([0,6]),ys=YB.concat([4.5,12]);rects.forEach(function(r){xs.push(r[0],r[1]);ys.push(r[2],r[3]);});
  var uq=function(a){return a.map(function(v){return Math.round(v*1000)/1000;}).filter(function(v,i,q){return q.indexOf(v)===i;}).sort(function(p,q){return p-q;});};xs=uq(xs);ys=uq(ys);
  function enZanja(cx,cy){return rects.some(function(r){return cx>r[0]&&cx<r[1]&&cy>r[2]&&cy<r[3];});}
  function tipoCelda(cx,cy){return enZanja(cx,cy)?0:((cx>0&&cx<6&&cy>4.5&&cy<12)?1:2);}
  function mkRun(r,k){var h=k===1?0.88:1,g=new T.BoxGeometry(r[1]-r[0],h,r[3]-r[2]);g.translate(0,-h/2,0);var m=new T.Mesh(g,mTierra);m.position.copy(P((r[0]+r[1])/2,(r[2]+r[3])/2,k===1?-0.12:0));m.receiveShadow=true;m.castShadow=false;TIERRA.add(m);}
  for(var j=0;j<ys.length-1;j++){var run=null,rk=-1;
    for(var i=0;i<xs.length-1;i++){var cx=(xs[i]+xs[i+1])/2,cy=(ys[j]+ys[j+1])/2,k=tipoCelda(cx,cy);
      if(run&&(k===0||k!==rk)){mkRun(run,rk);run=null;}
      if(k===0){var g=new T.BoxGeometry(xs[i+1]-xs[i],1,ys[j+1]-ys[j]);g.translate(0,-0.5,0);var m=new T.Mesh(g,mTierra);m.position.copy(P(cx,cy,0));m.receiveShadow=true;m.castShadow=false;TIERRA.add(m);OBTR.push(m);}
      else if(!run){run=[xs[i],xs[i+1],ys[j],ys[j+1]];rk=k;}else run[1]=xs[i+1];}
    if(run)mkRun(run,rk);}
  /* ---- trazo: cal, estacas e hilos ---- */
  SEG.forEach(function(s){var hz=s[1]===s[3],L=hz?Math.abs(s[2]-s[0]):Math.abs(s[3]-s[1]),m=hz?box(L,0.012,0.06,(s[0]+s[2])/2,0.006,-s[1],mCal):box(0.06,0.012,L,s[0],0.006,-(s[1]+s[3])/2,mCal);add(m,0,0.035);});
  var est=[[-1,3.5],[7,3.5],[-1,13],[7,13],[-1,-1],[7,-1],[-1,16],[7,16]],ls=[];
  est.forEach(function(q){add(box(0.05,0.6,0.05,q[0],0,-q[1],mEstaca,true),0,0.08);});
  [[0,1],[2,3],[0,2],[1,3],[4,5],[6,7],[4,6],[5,7]].forEach(function(k){var a=est[k[0]],b=est[k[1]];ls.push(a[0],0.5,-a[1],b[0],0.5,-b[1]);});
  lineas(ls,lHilo,0,0.08);
  /* ---- cimentación: plantilla, armado, zapata, cimiento ---- */
  var arm=[];
  SEG.forEach(function(s){var c=s[4]==='c',wz=c?0.6:0.4,sw=c?0.3:0.2,hz=s[1]===s[3],L=hz?Math.abs(s[2]-s[0]):Math.abs(s[3]-s[1]),mx=(s[0]+s[2])/2,my=(s[1]+s[3])/2,Lw=L+wz;
    function bx(len,h,yb,mat,w){return hz?box(len,h,w,mx,yb,-my,mat,true):box(w,h,len,mx,yb,-my,mat,true);}
    add(bx(Lw+0.1,0.05,-0.80,mPlant,wz+0.1),0.05,9,[0.05,0.06]);
    add(bx(Lw,0.2,-0.75,mCons,wz),0.075,9,[0.075,0.088]);
    add(bx(L+sw,0.55,-0.55,mPiedra,sw),0.088,9,[0.088,0.098]);
    var xa=Math.min(s[0],s[2])-wz/2+0.05,xb=Math.max(s[0],s[2])+wz/2-0.05,ya=Math.min(s[1],s[3])-wz/2+0.05,yb2=Math.max(s[1],s[3])+wz/2-0.05;
    function barra(o,y){if(hz)arm.push(xa,y,-(my+o),xb,y,-(my+o));else arm.push(mx+o,y,-ya,mx+o,y,-yb2);}
    [-wz/2+0.08,0,wz/2-0.08].forEach(function(o){barra(o,-0.7);});
    [-1,1].forEach(function(sg){barra(sg*(wz/2-0.08),-0.58);});
    var n=Math.floor(Lw/0.25);for(var k=0;k<=n;k++){var t=-Lw/2+0.03+k*(Lw-0.06)/n,a=wz/2-0.08,y0=-0.72,y1=-0.56;
      var p0=hz?[mx+t,my-a]:[mx-a,my+t],p1=hz?[mx+t,my+a]:[mx+a,my+t];
      arm.push(p0[0],y0,-p0[1],p1[0],y0,-p1[1], p0[0],y1,-p0[1],p1[0],y1,-p1[1], p0[0],y0,-p0[1],p0[0],y1,-p0[1], p1[0],y0,-p1[1],p1[0],y1,-p1[1]);}});
  lineas(arm,lRebar,0.06,0.075);
  /* ---- castillos (columnas de amarre) con arranques de varilla ---- */
  var CP={};
  SEG.forEach(function(s){var hz=s[1]===s[3],L=hz?Math.abs(s[2]-s[0]):Math.abs(s[3]-s[1]),n=Math.max(1,Math.ceil(L/3)),H=s[4]==='c'?5.4:2.4;
    for(var k=0;k<=n;k++){var t=k/n,x=s[0]+(s[2]-s[0])*t,y=s[1]+(s[3]-s[1])*t,key=x.toFixed(2)+'_'+y.toFixed(2);if(!CP[key])CP[key]={x:x,y:y,H:H};else CP[key].H=Math.max(CP[key].H,H);}});
  var arr=[];
  Object.keys(CP).forEach(function(k){var q=CP[k];
    add(box(0.17,q.H,0.17,q.x,0,-q.y,mCast,true),0.16,0.6);
    [[-0.05,-0.05],[0.05,-0.05],[-0.05,0.05],[0.05,0.05]].forEach(function(o){arr.push(q.x+o[0],-0.5,-(q.y+o[1]),q.x+o[0],0.9,-(q.y+o[1]));});
    for(var h=-0.4;h<0.9;h+=0.2)arr.push(q.x-0.05,h,-(q.y-0.05),q.x+0.05,h,-(q.y-0.05), q.x+0.05,h,-(q.y-0.05),q.x+0.05,h,-(q.y+0.05), q.x+0.05,h,-(q.y+0.05),q.x-0.05,h,-(q.y+0.05), q.x-0.05,h,-(q.y+0.05),q.x-0.05,h,-(q.y-0.05));});
  lineas(arr,lRebar,0.095,0.17);
  /* ---- cerramientos: dinteles sobre vanos y cadena de remate en bardas ---- */
  [[0.75,2.45,2.4],[3.09,4.31,2.26],[3.09,4.31,4.96],[4.64,5.86,2.26],[0.95,2.2,4.95],[4.64,5.86,4.96]].forEach(function(h){add(box(h[1]-h[0]+0.5,0.16,0.17,(h[0]+h[1])/2,h[2],-12,mCast,true),0.2,0.6);});
  SEG.filter(function(s){return s[4]==='b';}).forEach(function(s){var hz=s[1]===s[3],L=hz?Math.abs(s[2]-s[0]):Math.abs(s[3]-s[1]);add(hz?box(L,0.15,0.17,(s[0]+s[2])/2,2.25,-s[1],mCast,true):box(0.17,0.15,L,s[0],2.25,-(s[1]+s[3])/2,mCast,true),0.2,0.6);});
  /* ---- losas: cimbra de madera, puntales y armado, antes del colado ---- */
  function cimbra(x0,x1,y0,y1,top,a,b,pie){var cx=(x0+x1)/2,cy=(y0+y1)/2;
    add(box(x1-x0,0.05,y1-y0,cx,top-0.05,-cy,mCimb,true),a,b);
    var ar=[];for(var x=x0+0.1;x<x1;x+=0.2)ar.push(x,top+0.08,-(y0+0.1),x,top+0.08,-(y1-0.1));for(var y=y0+0.1;y<y1;y+=0.2)ar.push(x0+0.1,top+0.12,-y,x1-0.1,top+0.12,-y);
    lineas(ar,lRebar,a+0.005,b);
    for(var py=y0+0.4;py<y1;py+=0.9){add(box(x1-x0-0.1,0.1,0.1,cx,top-0.15,-py,mPunt,true),a,b+0.04);
      for(var px=x0+0.5;px<x1;px+=1.0){var base=pie(py);add(box(0.09,top-0.15-base,0.09,px,base,-py,mPunt,true),a,b+0.04);}}}
  cimbra(0.075,5.925,8.5,12,2.58,0.24,0.265,function(){return 0;});
  cimbra(0.075,5.925,4.5,12,5.28,0.31,0.335,function(y){return y>8.5?2.7:0;});
  /* ---- materiales en obra ---- */
  [[1.0,2.2],[2.4,2.0]].forEach(function(q){add(box(1.2,0.9,0.9,q[0],0,-q[1],mPal,true),0.1,0.6);});
  var ar1=new T.Mesh(new T.ConeGeometry(0.8,0.75,14),mArena);ar1.position.copy(P(4.8,2.3,0.37));add(ar1,0.04,0.6);
  var gv=new T.Mesh(new T.ConeGeometry(0.7,0.6,14),mGrava);gv.position.copy(P(5.3,3.4,0.3));add(gv,0.04,0.6);
})();
