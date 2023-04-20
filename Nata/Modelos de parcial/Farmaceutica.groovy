Accion Farmaceutico Es
Ambiente
	sec,sal: secuencia de alfanumerico
	v,Lab: alfanumerico
	TotGral,ContL,ContProd,dec,uni,Suma: entero

	Función Letras(x:entero):alfanumerico
		Según x Hacer
			=1:Letras:="1"
			=2:Letras:="2"
			=3:Letras:="3"
			=4:Letras:="4"
			=5:Letras:="5"
			=6:Letras:="6"
			=7:Letras:="7"
			=8:Letras:="8"
			=9:Letras:="9"
		FinSegún
	FinFunción

Proceso
	ARR(sec);AVZ(sec,v);
	CREAR(sal)
	Escribir("Ingrese la primer letra del tipo de línea terapeutica")
	Leer(Lab)
	TotGral:=0
	Mientras NFDS(sec) Hacer
		Mientras v<>"-" Hacer
			Esc(v)
			AVZ(sec,v)
		FinMientras
		ContProd:=0
		AVZ(sec,v)
		Esc("Laboratorio")
		Esc("Cantidad")
		Mientras v<>"@" Hacer
			ContL:=0
			AVZ(sec,v)
			Si v = Lab Entonces
				Mientras v<>" " y v<>"@" Hacer// Parfamog-Glozano ibuprofeno ismigen@Farmar-Adelux 
					Esc(sal,v)
					ContL:=ContL+1
					AVZ(sec,v)
				FinMientras
				Si ContL>=10 Entonces
					dec:=ContL DIV 10
					uni:=ContL MOD 10
					Suma:=uni+dec
					Cantidad:=Letras(Suma)
					Esc(sal,Cantidad)
					ContProd:=ContProd+1
				Sino
					Cantidad:=Letras(Suma)
					Esc(sal,Cantidad)
				FinSi
				Esc(sal," ")
				AVZ(sec,v)
			Sino
				Mientras v <> " " y v<>"@" Hacer
					Avz(sec,v)
				FinMientras
				Mientras v = " " y v<>"@" Hacer
					Avz(sec,v)
				FinMientras
			FinSi
			AVZ(sec,v)
		FinMientras
		TotGral:=TotGral+ContProd;
		Esc(Lab)
		Esc(ContProd)
		AVZ(sec,v)
	FinMientras
	Esc("Total General:",TotGral)
	CERRAR(sec)
	CERRAR(sal)
FinAccion
