Accion Palabras Es
Ambiente
	sec,sal:secuencia de caracter
	v,SumaCar:caracter
	contL,ContP,dec,uni,SumaEnt:entero
	vocal={"a","e","i","o","u"}
	Función CARENT(x:caracter):entero
		Según x Hacer
		="0":CARENT:=0
		="1":CARENT:=1
		="2":CARENT:=2
		="3":CARENT:=3
		="4":CARENT:=4
		="5":CARENT:=5
		="6":CARENT:=6
		="7":CARENT:=7
		="8":CARENT:=8
		="9":CARENT:=9
		FinSegún
	FinFunción

Proceso
	ARR(sec);AVZ(sec,v)
	Crear(sal)
	ContP:=1
	Mientras v<>"*" Hacer
		Mientras v=" " y v<>"."Hacer
			AVZ(sec,v)
		FinMientras
		Mientras v<>"." Hacer
			ContL:=0
			Si ContP MOD 2 = 0  y v no en vocal Entonces
				Mientras v <> " " y v <>"." Hacer
					Esc(sal,v)
					ContL:=ContL+1
					AVZ(sec,v)
				FinMientras
				Si ContL > 9 Entonces
					dec:=ContL Div 10
					uni:=ContL MOD 10
					SumaEnt:=dec+uni
					Si SumaEnt > 9 Entonces
						dec:=ContL Div 10
						uni:=ContL MOD 10
						SumaEnt:=dec+uni
						SumaCar:=CARENT(SumaEnt)
						Esc(sal,SumaCar)
					Sino
						Esc(sal,SumaCar)
					FinSi
				Sino
					SumaCar:=CARENT(ContL)
					Esc(sal,SumaCar)
				FinSi
				Esc(sal," ")
			Sino
				Mientras v="" y v <>"." Hacer
					AVZ(sec,v)
				FinMientras
				Mientras v<>" " y v <>"." Hacer
					AVZ(sec,v)
				FinMientras
			FinSi
			ContP:=ContP+1
		FinMientras
		Esc(sal,".")
		AVZ(sec,v)
	FinMientras
	Cerrar(sec)
	Cerrar(sal)
FinAccion






