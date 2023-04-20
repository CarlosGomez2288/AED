Accion Urunday Es
Ambiente
	sec,sal1,sal2,sal3: secuencia de caracter
	v:caracter
	F,E,A,Error,Total,mil,cen,dec,uni,Suma: entero

	Subaccion Sal Es
		Según s Hacer
		="A":Esc(sal1,v)
		="F":Esc(sal2,v)
		="E":Esc(sal3,v)
		FinSegún
	FinSubaccion

	Funcion CarEnt(x:caracter): entero
		Según x Hacer
		="0":CarEnt:=0
		="1":CarEnt:=1
		="2":CarEnt:=2
		="3":CarEnt:=3
		="4":CarEnt:=4
		="5":CarEnt:=5
		="6":CarEnt:=6
		="7":CarEnt:=7
		="8":CarEnt:=8
		="9":CarEnt:=9
		="a":CarEnt:=1
		="e":CarEnt:=2
		="i":CarEnt:=3
		FinSegún
	FinFunción
	Vocal={"a","e","i"}

	Subaccion Salida Es
		Según s Hacer
		="A":Esc(sal1,"!")
		="F":Esc(sal2,"!")
		="E":Esc(sal3,"!")
		FinSegún
	FinSubaccion

	Subaccion año Es
		Según Suma Hacer
		="A":mil:=Suma Div 1000:

	Subaccion cont Es
		Según s Hacer
		="A":A:=A+1
		="F":F:=F+1
		="E":E:=E+1
		FinSegún
	FinSubaccion

Proceso
	ARR(sec);AVZ(v)
	CREAR(sal1)
	CREAR(sal2)
	CREAR(sal3)
	F:=0;A:=0;E:=0;ERROR:=0;Total:=0

	Mientras NFDS(sec) Hacer
		Mientras v <> "!" Hacer
			s:=v
			Sal
			AVZ(sec,v)
			Para i:1 hasta 30 Hacer
				Sal
				AVZ(sec,v)
			FinPara
			AVZ(sec,v)

			mil:=CarEnt(v);Sal;AVZ(sec,v)
			cen:=CarEnt(v);Sal;AVZ(sec,v)
			dec:=CarEnt(v);Sal;AVZ(sec,v)

			Según s Hacer
			="A":uni:=CarEnt(v);Sal;AVZ(sec,v)
			="F":uni:=CarEnt(v);Sal;AVZ(sec,v)
			="E":Si v en Vocal Entonces
					Según v Hacer
					="a":uni:=1;Esc(sal3,"1")
					="e":uni:=2;Esc(sal3,"2")
					="i":uni:=3;Esc(sal3,"3")
					FinSegún
					ERROR:=ERROR+1
				Sino
					uni:=CarEnt(v);Esc(sal3,v)
				FinSi
			FinSegún
		
			Suma:=mil*1000+cen*100+dec*10+uni

			Si Suma > 2000 Entonces
				cont
			FinSi

		FinMientras
		Total:=Total+1
		Salida
		AVZ(sec,v)
	FinMientras
	Porcentaje:=(ERROR*100)/Total
	Esc("El porcentaja de autores con fallo en el año son:",ERROR)
	Esc("La cantidad de autores de America que empezaron luego del 2000 son:",A)
	Esc("La cantidad de autores de Africa que empezaron luego del 2000 son:",F)
	Esc("La cantidad de autores de Europa que empezaron luego del 2000 son:",E)
	Esc("El total de autores analizados son:",Total)
	CERRAR(sec)
	CERRAR(sec1)
	CERRAR(sec2)
	CERRAR(sec3)
FinAccion



			





