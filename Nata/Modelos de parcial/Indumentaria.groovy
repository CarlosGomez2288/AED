Accion Indumentaria Es
Ambiente
	sec1,sec2,sal: secuencia de caracter
	v1,v2,s,d,u: caracter
	v2,L,M,S,XL,Mayor,Sum: entero

	Función CarEnt(x:caracter):entero
		Según x hacer
			="0":EntCar:=0
			="1":EntCar:=1
			="2":EntCar:=2
			="3":EntCar:=3
			="4":EntCar:=4
			="5":EntCar:=5
			="6":EntCar:=6
			="7":EntCar:=7
			="8":EntCar:=8
			="9":EntCar:=9
		FinSegún
	FinFunción

Proceso
	ARR(sec1);AVZ(sec1,v1)
	ARR(sec2);AVZ(sec2,v2)
	CREAR(sal)
	Prenda:=0
	Mientras NFDS(sec1) y NFDS(sec2) Hacer
		Si v1 = "p" Entonces
			d:=v2
			AVZ(sec2,v2)
			u:=v2
			Sum:=d+u
			Mientras v2 <> "!" Hacer
				AVZ(sec2,v2)
			FinMientras
			Mientras v1 <> "&" Hacer
				Esc(sal,v1)
				AVZ(sec1,v1)
				s:=v1
			FinMientras
			Esc(sal,"-")
			d:=CarEnt(d)
			Esc(sal,v2)
			AVZ(sec2,v2)
			u:=CarEnt(u)
			Esc(sal,u)
			AVZ(sec2,v2)
			Esc(sal,"$")
			Sum:=d*10+u
			Mientras v2 <> "!" Hacer
				AVZ(sec2,v2)
			FinMientras
			Según s Hacer
				="1":S:=S+Sum
				="2":M:=M+Sum
				="3":L:=L+Sum
				="4":XL:=XL+Sum
			FinSegún
		Sino
			Mientras v2 <> "!" Hacer
				AVZ(sec2,v2)
			FinMientras
			Mientras v1 <> "&" Hacer
				s:=v1
				AVZ(sec1,v1)
			FinMientras
			Según s Hacer
				="1":ContS:=ContS+1
				="2":ContM:=ContM+1
				="3":ContL:=ContL
				="4":ContXL:=ContXL+1
			FinSegún
		FinSi
		AVZ(sec1,v1)
		AVZ(sec2,v2)
	FinMientras

	Si S > M Entonces
	    Si S > L Entonces
	        Si S > XL Entonces
	            Max:=S
	        Sino
	            Max:=XL
	        Fin Si
	    Sino
	        Si L > M Entonces
	            Si L > Xl Entonces
	                Max:=L
	            Sino
	                Max:=XL
	            Fin Si
	        Sino
	            Si M > L Entonces
	                Si M > XL Entonces
	                    Max:=M
	                Sino
	                    Max:=XL
	                Fin Si
	            Sino
	            	Si L > XL Entonces
	            FinSi
	        FinSi 
	    Fin Si
	Sino
	    Si M > L Entonces
	        Si M > XL Entonces
	            Max:=M
	        Sino
	            Max:=XL
	        Fin Si
	    Sino
	        Si L > Xl Entonces
	            Max:=L
	        Sino
	            Max:=XL
	        Fin Si
	    Fin Si
	Fin Si


	CERRAR(sec1)
	CERRAR(sec2)
	CERRAR(sal)
FinAccion


			
			


