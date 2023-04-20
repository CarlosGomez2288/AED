Accion IPDUV Es
Ambiente
	sec,sal1,sal2: secuencia de caracter
	v,x: caracter
	L1,L2,L3,L4,P1,P2,P3,P4,Total,num: entero
	Función CarEnt(s:caracter): entero
		Según s Hacer
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		="0":CarEnt:=0
		FinSegún
	FinFunción
Proceso
	ARR(sec);AVZ(sec,v)
	CREAR(sal1);CREAR(sal2)
	L1:=0;L2:=0;L3:=0;L4:=0;Total:=0
	Mientras NFDS(sec) hacer
		Mientras v<> "&" y NFDS(sec) Hacer
			Mientras v <> "-" Hacer
				AVZ(sec,v)
			FinMientras
			AVZ(sec,v)
			Para i:=1 Hasta 8 Hacer
				x:=v
				AVZ(sec,v)
			FinPara
			AVZ(sec,v)
			Según v Hacer
				="1":L1:=L1+1
				="2":L2:=L2+1
				="3":L3:=L3+1
				="4":L4:=L4+1
			FinSegún
			AVZ(sec,v)
			AVZ(sec,v)
			num:=CarEnt(x)
			Si num MOD 2 = 0 Entonces
				Mientras v <> "-" Hacer
					Esc(sal1,v)
					AVZ(sec,v)
				FinMientras
				Esc(sal1,"#")
			Sino
				Mientras v <> "-" Hacer
					Esc(sal2,v)
					AVZ(sec,v)
				FinMientras
				Esc(sal2,"#")
			FinSi
			Mientras v <> "&" Hacer
				AVZ(sec,v)
			FinMientras
		FinMientras
		Total:=Total+1
		AVZ(sec,v)
	FinMientras
	P1:=(L1*100)/Total
	P2:=(L2*100)/Total
	P3:=(L3*100)/Total
	P4:=(L4*100)/Total
	Esc("La cantidad de sorteados de Resistencia:",P1)
	Esc("La cantidad de sorteados de Barranqueras:",P1)
	Esc("La cantidad de sorteados de Pto Vilelas:",P1)
	Esc("La cantidad de sorteados de Fontana:",P1)
	Esc("El total de sorteados son:",Total)
	Cerrar(sec)
	Cerrar(sal1)
	Cerrar(sal2)
FinAccion


