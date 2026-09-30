 /* ---- Teleférico: estación terminal con andén, rueda motriz horizontal, línea de cable en circuito con pilona y estación de llegada ---- */
 estacion:function(){ var P=[],T=[],E=[],xs=[-8,-2.7,2.7,8];
   /* estación A: cimentación, andén con guardas y escalera de acceso, columnas de acero con contraventeos, trabes y cubierta */
   P.push(box('cimentacion',22,1,12,0,0,0,'hormigon')); P.push(box('plataforma',20,.5,10,0,1,0,'hormigon'));
   [-4.7,4.7].forEach(function(z){ P.push(box('plataforma',20,.03,.25,0,1.5,z,'seg')); });
   [-4.85,4.85].forEach(function(z){ P.push(box('plataforma',20,.06,.06,0,2.55,z,'acero')); P.push(box('plataforma',20,.06,.06,0,2.05,z,'acero')); for(var x=-10;x<=10;x+=4) P.push(box('plataforma',.08,1.05,.08,x,1.5,z,'acero')); });
   for(var i=0;i<5;i++) P.push(box('plataforma',.5,.3*(i+1),2.4,-10.25-.5*(4-i),0,0,'hormigon'));
   xs.forEach(function(x){ [-4,4].forEach(function(z){ P.push(box('columnas',1.1,.25,1.1,x,1.5,z,'acero')); P.push(box('columnas',.7,7.75,.7,x,1.75,z,'acero')); }); });
   [-4,4].forEach(function(z){ P.push(box('columnas',9.4,.15,.15,-5.35,5.6,z,'acero',0,[0,0,.97])); P.push(box('columnas',9.4,.15,.15,5.35,5.6,z,'acero',0,[0,0,-.97])); });
   xs.forEach(function(x){ P.push(box('trabes',.5,.6,9.4,x,9.5,0,'acero')); });
   [-4,0,4].forEach(function(z){ P.push(box('trabes',17.4,.35,.35,0,10.1,z,'acero')); });
   P.push(box('cubierta',22,.35,12,0,10.45,0,'ligero')); P.push(box('cubierta',22.2,.4,.3,0,10.4,6.05,'acero')); P.push(box('cubierta',22.2,.4,.3,0,10.4,-6.05,'acero'));
   P.push(box('cubierta',16,.05,1.6,0,10.8,0,'vidrio'));
   /* rueda motriz horizontal (Ø 5 m) en el extremo de la línea: el cable da la vuelta de un carril al otro; cuelga de una viga entre trabes */
   P.push(cil('rueda',2.5,.35,-6,7.325,0,'acero')); P.push(cil('rueda',.9,.6,-6,7.2,0,'acero'));
   P.push(cil('rueda',.3,5.7,-6,1.5,0,'acero')); P.push(cil('rueda',.25,1.1,-6,7.8,0,'acero'));
   P.push(box('rueda',5.3,.5,.4,-5.35,8.9,0,'acero')); P.push(box('rueda',3,2.4,1.4,-5.2,1.5,-3.9,'ligero'));
   /* línea: pilona intermedia con dos baterías de poleas, una por carril */
   P.push(box('torre',3,1,3,21,0,0,'hormigon')); P.push(cil('torre',.45,9.1,21,1,0,'acero'));
   P.push(box('torre',.6,.5,7.4,21,9.6,0,'acero'));
   [-2.5,2.5].forEach(function(z){ P.push(box('torre',.4,.35,.4,21,10.1,z,'acero')); P.push(cil('torre',.55,.4,21,10.25,z,'acero',0,[PI/2,0,0])); });
   /* estación B (llegada): más chica, con la misma altura de cable, rueda de retorno, escalera de salida y cubierta */
   P.push(box('estacionB',12,1,9,34.5,0,0,'hormigon')); P.push(box('estacionB',11,.5,8,34.5,1,0,'hormigon'));
   [-3.9,3.9].forEach(function(z){ P.push(box('estacionB',11,.03,.25,34.5,1.5,z,'seg')); });
   [30,34,38].forEach(function(x){ [-3.8,3.8].forEach(function(z){ P.push(box('estacionB',.6,8.1,.6,x,1.5,z,'acero')); }); });
   [30,34,38].forEach(function(x){ P.push(box('estacionB',.4,.5,8.4,x,9.1,0,'acero')); });
   P.push(box('estacionB',13,.3,10,34.5,9.6,0,'ligero'));
   P.push(cil('estacionB',2.5,.35,37,7.325,0,'acero')); P.push(cil('estacionB',.9,.6,37,7.2,0,'acero'));
   P.push(cil('estacionB',.3,5.7,37,1.5,0,'acero')); P.push(cil('estacionB',.25,.8,37,7.8,0,'acero')); P.push(box('estacionB',4.4,.5,.4,36,8.6,0,'acero'));
   for(var j=0;j<5;j++) P.push(box('estacionB',2.4,.3*(5-j),.5,31,0,4.25+.5*j,'hormigon'));
   /* cable en circuito cerrado: carril de ida (z=-2.5) y de regreso (z=+2.5); la altura sigue el perfil estación - pilona - estación */
   var yc=function(x){ return x<=11?7.5:x<=21?7.5+3.5*(x-11)/10:x<=30?11-3.5*(x-21)/9:7.5; }, lazo=[], t, ang;
   [-6,11,21,30,37].forEach(function(x){ lazo.push([x,yc(x),-2.5]); });
   for(t=1;t<=8;t++){ ang=PI*t/8; lazo.push([37+2.5*Math.sin(ang),7.5,-2.5*Math.cos(ang)]); }
   [30,21,11,-6].forEach(function(x){ lazo.push([x,yc(x),2.5]); });
   for(t=1;t<=8;t++){ ang=PI*t/8; lazo.push([-6-2.5*Math.sin(ang),7.5,2.5*Math.cos(ang)]); }
   T.push(tub('CAB',lazo));
   /* cabinas de 8 personas colgadas del cable: dos atracadas en los andenes (piso a nivel) y dos en tránsito, una por carril */
   [[0,-2.5],[33,2.5],[15,-2.5],[27,2.5]].forEach(function(c){ var by=yc(c[0])-5.85, x=c[0], z=c[1];
     P.push(box('cabinas',2.6,.9,2.2,x,by,z,'ligero')); P.push(box('cabinas',2.62,1.3,2.22,x,by+.9,z,'vidrio')); P.push(box('cabinas',2.7,.1,2.3,x,by+2.2,z,'acero'));
     P.push(cil('cabinas',.07,3.35,x,by+2.3,z,'acero')); P.push(box('cabinas',.4,.3,.5,x,by+5.5,z,'acero')); });
   /* eléctrica: tablero, ducto por la columna y a lo largo de las trabes, luminarias */
   E.push(eqp('ELE',.6,1.1,.3,-8,1.5,-4.6));
   T.push(tub('ELE',[[-8,2.6,-4.6],[-8,9.6,-4.6],[8,9.6,-4.6]])); T.push(tub('ELE',[[-2.7,9.6,-4.6],[-2.7,9.6,0],[-2.7,9.2,0]])); T.push(tub('ELE',[[2.7,9.6,-4.6],[2.7,9.6,0],[2.7,9.2,0]]));
   E.push(eqp('ELE',.8,.15,.3,-2.7,9.05,0)); E.push(eqp('ELE',.8,.15,.3,2.7,9.05,0));
   /* voz y datos: gabinete, canalización y cámara */
   E.push(eqp('TIC',.4,.5,.25,-7.4,1.5,-4.6)); T.push(tub('TIC',[[-7.4,2.2,-4.6],[-7.4,9.35,-4.7],[7.4,9.35,-4.7]])); T.push(tub('TIC',[[0,9.35,-4.7],[0,8.5,-4.7]])); E.push(eqp('TIC',.35,.25,.5,0,8.3,-4.7));
   /* pluvial: canalón en el alero y bajadas */
   T.push(tub('PLU',[[-10.6,10.3,6.2],[10.6,10.3,6.2]])); T.push(tub('PLU',[[10.6,10.3,6.2],[10.6,1.1,6.2]])); T.push(tub('PLU',[[-10.6,10.3,6.2],[-10.6,1.1,6.2]]));
   return {parts:P,tubos:T,equipos:E,
     ex:function(p){return {cimentacion:[0,-3,0],plataforma:[0,-1,0],columnas:[0,1,0],rueda:[0,1,0],trabes:[0,5,0],cubierta:[0,9,0]}[p.g]},
     ey:function(y){return y<1?-3:y<1.5?-1:y<9.4?1:y<10.2?5:9},
     niveles:[[1.5,'ANDÉN'],[7.5,'CABLE'],[10.45,'CUBIERTA']],
     plantas:[{n:'Andén · corte +3 m',cut:3,ylo:1.5,yhi:6,ctx:['cimentacion','plataforma','estacionB']},{n:'Cable y ruedas · corte +7.5 m',cut:7.5,ylo:6.5,yhi:9,ctx:['cimentacion','plataforma','estacionB']}],
     grupos:['Cimentación','Plataforma','Columnas','Rueda motriz','Trabes','Cubierta','Torre','Cabinas']}; },

