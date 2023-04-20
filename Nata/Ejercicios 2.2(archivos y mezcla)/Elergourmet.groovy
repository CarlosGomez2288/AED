Accion Elergourmet Es
Ambiente
	sec,sal: secuencia de caracteres
	v,c,d: caracter
	Cont,ContD,Porcentaje: entero
	Conjunto={"0","1","2"}
Proceso //D015sopa-Agua#F+
	ARR(sec);AVZ(sec,v)
	Crear(sal)
	Cont:=0;ContD:=0
	Mientras NFDS(sec) Hacer
		Mientras v<>"+" Hacer
			Si v = "D" Entonces
				AVZ(sec,v)
				c:=v
				AVZ(sec,v)
				d:=v
				AVZ(sec,v)
				Si c = "0" y d en Conjunto Entonces
					Esc(sal,"D")
					Esc(sal,c)
					Esc(sal,d)
					AVZ(sec,v)
					Esc(sal,v)
					AVZ(sec,v)
					Mientras v<>"#"
						Esc(sal,v)
						AVZ(sec,v)
					FinMientras
					Esc(sal,"#")
					AVZ(sec,v)
					Si v = "D" Entonces
						ContD:=ContD+1
					FinSi
					Esc(sal,v)
					AVZ(sec,v)
					Esc(sal,"+")
				Sino
					Mientras v<>"#"
						AVZ(sec,v)
					FinMientras
					Si v = "D" Entonces
						ContD:=ContD+1
					FinSi
			Sino
				Mientras v<>"#"
					AVZ(sec,v)
				FinMientras
				Si v = "D" Entonces
					ContD:=ContD+1
				FinSi
			FinSi
		FinMientras
		Cont:=Cont+1
		AVZ(sec,v)
	FinMientras
	Porcentaje:=(ContD*100)/Cont
	Esc("El porcentaje de platos dificiles son:",ContD,"sobre el total de:",Cont)
	Cerrar(sec)
	Cerrar(sal)
FinAccion