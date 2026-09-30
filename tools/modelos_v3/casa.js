 /* ---- Casa: dos niveles con la misma huella, muros con vanos reales, escalera en U, cuartos, cochera con pérgola e instalaciones que llegan a cada mueble ---- */
 casa:function(){ var P=[],T=[],E=[], yb=.5, ya=3.8, H=3, t=.15, ST=.18333;
   /* cimentación y patios de servicio (todo lo exterior se apoya en una losa) */
   P.push(box('cimentacion',14,.5,10,0,0,0,'hormigon'));
   P.push(box('patio',15,.12,3,.5,0,6.5,'hormigon')); P.push(box('patio',4,.12,8.8,9,0,-1.2,'hormigon')); P.push(box('patio',3.5,.12,4.5,-8.75,0,-1.5,'hormigon'));
   /* planta baja: muros exteriores con puerta, portón de cochera y ventanas */
   paredX(P,'muros PB',-6,6,3.85,.3,yb,H,[[-4.7,-.7,1.0,3.0,'vidrio'],[-.55,.55,yb,2.7,'madera'],[2.8,5.6,yb,2.9,'madera']]);
   paredX(P,'muros PB',-6,6,-3.85,.3,yb,H,[[-.9,1.3,1.3,2.6,'vidrio']]);
   paredZ(P,'muros PB',-4,4,-5.85,.3,yb,H,[[-3.2,-2.4,1.8,2.8,'vidrio']]);
   paredZ(P,'muros PB',-4,4,5.85,.3,yb,H,[[-1.9,-1.0,yb,2.6,'madera']]);
   /* planta baja: cubo de escalera, cocina, cochera y cuarto de servicio */
   paredX(P,'muros PB',-5.7,-3.6,-1.55,t,yb,H); paredZ(P,'muros PB',-3.7,-1.4,-1.2,t,yb,H);
   paredX(P,'muros PB',-1.2,2.5,-1.4,t,yb,H,[[-.5,.4,yb,2.6]]);
   paredZ(P,'muros PB',-3.7,3.7,2.5,t,yb,H,[[-.2,.7,yb,2.6]]);
   paredX(P,'muros PB',2.5,5.7,-.9,t,yb,H,[[3,3.9,yb,2.6]]);
   /* entrepiso con el hueco de la escalera */
   [[-6.2,-5.7,-4.2,4.2],[-5.7,-3.8,-4.2,-3.7],[-5.7,-3.8,-1.75,4.2],[-3.8,-2.4,-4.2,-2.65],[-3.8,-2.4,-1.75,4.2],[-2.4,6.2,-4.2,4.2]].forEach(function(r){ P.push(box('entrepiso',r[1]-r[0],.3,r[3]-r[2],(r[0]+r[1])/2,3.5,(r[2]+r[3])/2,'hormigon')); });
   /* escalera en U: primer tramo hacia el oeste, descanso y segundo tramo de regreso hasta el piso de planta alta */
   for(var i=0;i<9;i++){ P.push(box('escalera',.28,yb+ST*(i+1),.9,-2.4-.28*(i+.5),0,-3.25,'hormigon')); P.push(box('escalera',.28,yb+ST*(9+i+1),.9,-4.9+.28*(i+.5),0,-2.2,'hormigon')); }
   P.push(box('escalera',.8,yb+ST*9,1.95,-5.3,0,-2.725,'hormigon'));
   /* planta alta: misma huella, ventanas por recámara y baño */
   paredX(P,'muros PA',-6,6,3.85,.3,ya,H,[[-4.9,-2.7,4.7,6.2,'vidrio'],[1.4,4.6,4.7,6.2,'vidrio']]);
   paredX(P,'muros PA',-6,6,-3.85,.3,ya,H,[[.4,1.4,5.3,6.2,'vidrio'],[3.2,5.2,4.9,6.2,'vidrio']]);
   paredZ(P,'muros PA',-4,4,-5.85,.3,ya,H,[[.4,2.2,4.7,6.2,'vidrio']]);
   paredZ(P,'muros PA',-4,4,5.85,.3,ya,H,[[.3,1.6,4.7,6.2,'vidrio']]);
   paredX(P,'muros PA',-5.7,-1.8,-1.55,t,ya,H); paredZ(P,'muros PA',-1.55,3.7,-1.8,t,ya,H,[[.6,1.5,ya,5.9]]);
   paredZ(P,'muros PA',.1,3.7,.25,t,ya,H,[[1,1.9,ya,5.9]]); paredX(P,'muros PA',.25,5.7,.1,t,ya,H);
   paredX(P,'muros PA',.25,2.4,-1.4,t,ya,H,[[.6,1.5,ya,5.9]]); paredZ(P,'muros PA',-3.7,-1.4,.25,t,ya,H); paredZ(P,'muros PA',-3.7,-1.4,2.4,t,ya,H);
   /* azotea con pretil, base y tinaco de 1,100 L elevado para dar presión */
   P.push(box('azotea',12.4,.3,8.4,0,6.8,0,'hormigon'));
   P.push(box('azotea',12.4,.5,.15,0,7.1,4.1,'hormigon')); P.push(box('azotea',12.4,.5,.15,0,7.1,-4.1,'hormigon')); P.push(box('azotea',.15,.5,8.2,6.1,7.1,0,'hormigon')); P.push(box('azotea',.15,.5,8.2,-6.1,7.1,0,'hormigon'));
   P.push(box('tinaco',1.5,1,1.5,4,7.1,-2,'hormigon')); P.push(cil('tinaco',.6,1.3,4,8.1,-2,'ligero'));
   /* cochera: pérgola de acero apoyada en el patio y anclada al muro de fachada */
   [2.5,5.9].forEach(function(x){ P.push(box('pergola',.15,3.08,.15,x,.12,7.4,'acero')); });
   P.push(box('pergola',3.6,.15,.18,4.2,3.2,7.4,'acero')); P.push(box('pergola',3.6,.15,.18,4.2,3.2,4.1,'acero'));
   for(var k=0;k<7;k++) P.push(box('pergola',.1,.1,3.3,2.7+k*.5,3.3,5.75,'acero'));
   /* agua fría: cisterna con bomba, subida exterior, tinaco y montante hasta la cocina */
   E.push(eqp('AF',2.4,1.2,2,-8.75,.12,-1.5)); E.push(eqp('AF',.5,.4,.4,-7.3,.12,-1.5));
   T.push(tub('AF',[[-8,1.0,-1.5],[-6.2,1.0,-1.5],[-6.2,7.3,-1.5],[2.9,7.3,-1.5],[2.9,9.0,-1.5],[2.9,9.0,-2],[3.4,9.0,-2]]));
   T.push(tub('AF',[[4.6,8.3,-2],[4.9,8.3,-2],[4.9,7.3,-2],[4.9,7.3,-3.55],[2,7.3,-3.55],[2,1.5,-3.55]]));
   T.push(tub('AF',[[2,4.9,-3.55],[.8,4.9,-3.55]])); T.push(tub('AF',[[2,1.5,-3.55],[.8,1.5,-3.55]]));
   /* agua caliente: calentador en el patio lateral, línea a cocina y baño */
   E.push(eqp('AC',.7,1.1,.45,7.5,.12,-2.6));
   T.push(tub('AC',[[7.5,1.22,-2.6],[7.5,1.5,-2.6],[2.25,1.5,-2.6],[2.25,1.5,-3.5],[2.25,5.5,-3.5],[.85,5.5,-3.5],[.85,5.5,-2.6]])); T.push(tub('AC',[[2.25,1.5,-3.5],[.9,1.5,-3.45]]));
   /* muebles de baño y cocina */
   E.push(eqp('AF',.9,.3,.5,.8,1.35,-3.4)); E.push(eqp('GAS',.6,.1,.6,-.5,1.35,-3.35));
   E.push(eqp('SAN',.4,.4,.7,1.6,3.8,-3.3)); E.push(eqp('AF',.6,.2,.45,.8,4.6,-3.5)); E.push(eqp('AC',.3,.05,.3,.85,5.75,-2.6));
   /* aguas negras: bajante con ventilación sobre el pretil, ramales de cada mueble y albañal al registro */
   T.push(tub('SAN',[[1.7,8.6,-3.62],[1.7,.15,-3.62],[1.7,.15,-8.6]])); T.push(tub('SAN',[[1.7,4.4,-3.62],[1.6,4.4,-3.4]])); T.push(tub('SAN',[[.8,4.4,-3.5],[1.7,4.4,-3.62]])); T.push(tub('SAN',[[.8,1.0,-3.4],[1.7,1.0,-3.62]]));
   E.push(eqp('SAN',.7,.2,.7,1.7,0,-8.8));
   /* pluvial: dos bajadas por el exterior que salen por el pretil */
   T.push(tub('PLU',[[5.7,7.2,3.6],[6.25,7.2,3.6],[6.25,.62,3.6],[7.35,.62,3.6],[7.35,.2,3.6],[7.35,.2,7]]));
   T.push(tub('PLU',[[5.4,7.2,-3.7],[5.4,7.2,-4.25],[5.4,.62,-4.25],[5.4,.62,-5.3],[5.4,.2,-5.3],[5.4,.2,-8]]));
   /* gas L.P.: tanque estacionario, calentador y estufa */
   E.push(eqp('GAS',1,1.3,1,9.6,.12,-3.3));
   T.push(tub('GAS',[[9.6,1.4,-3.3],[8.6,1.4,-3.3],[8.6,1,-3.15],[-.5,1,-3.15],[-.5,1.4,-3.15]])); T.push(tub('GAS',[[8.6,1,-3.15],[8.6,1,-2.6],[7.85,1,-2.6]]));
   /* eléctrica: tablero en la sala y charolas por nivel */
   E.push(eqp('ELE',.15,.9,.6,-5.6,1.5,1.5));
   T.push(tub('ELE',[[-5.5,2.4,1.5],[-5.5,3.3,1.5],[5.4,3.3,1.5]])); T.push(tub('ELE',[[0,3.3,1.5],[0,3.3,-2.6]])); T.push(tub('ELE',[[-5.5,3.3,1.5],[-5.5,6.4,1.5],[5.4,6.4,1.5]]));
   /* voz y datos: acometida desde el poste y ramal a la planta alta */
   E.push(eqp('TIC',.2,3.8,.2,-8.3,0,3)); T.push(tub('TIC',[[-8.3,3.6,3],[-5.5,3.1,3],[.5,3.1,3],[.5,6.3,3],[4.5,6.3,3]]));
   /* aire acondicionado: condensadora en el patio lateral y evaporadoras en la sala y la recámara */
   E.push(eqp('REF',.5,.7,.9,7.4,.12,2.2)); E.push(eqp('REF',.25,.3,.9,2.3,2.5,2.2)); E.push(eqp('REF',.25,.3,.9,5.55,5.9,2.2));
   T.push(tub('REF',[[7.15,.6,2.2],[6.45,.6,2.2],[6.45,2.65,2.2],[2.4,2.65,2.2]])); T.push(tub('REF',[[6.45,2.65,2.2],[6.45,6.05,2.2],[5.65,6.05,2.2]]));
   return {parts:P,tubos:T,equipos:E,
     ex:function(p){return {cimentacion:[0,-3,0],'muros PB':[0,0,0],escalera:[0,1.5,0],entrepiso:[0,3,0],'muros PA':[0,6,0],azotea:[0,10,0],tinaco:[0,13,0],pergola:[0,0,5]}[p.g]},
     ey:function(y){return y<.55?-3:y<3.5?0:y<3.8?3:y<6.8?6:y<7.65?10:13},
     niveles:[[.5,'PB'],[3.8,'PA'],[7.1,'AZOTEA']],
     plantas:[{n:'Planta baja · corte +1.8 m',cut:1.8,ylo:.5,yhi:3.5,ctx:['cimentacion','patio']},{n:'Planta alta · corte +5.1 m',cut:5.1,ylo:3.8,yhi:6.8,ctx:['entrepiso']},{n:'Azotea · corte +7.4 m',cut:7.4,ylo:6.9,yhi:9.6,ctx:['azotea']}],
     grupos:['Cimentación','Patios','Muros PB','Escalera','Entrepiso','Muros PA','Azotea','Tinaco','Pérgola']}; },

