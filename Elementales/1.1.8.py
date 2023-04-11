/*Escriba un algoritmo que permita conocer la edad de una persona, con solo 
ingresar la fecha de nacimiento y la fecha actual, ambas en el formato: DIA, MES, AÑO*/
Accion fecha
	ambiente
		dia, mes, anio, diaA, mesA, anioA:entero;
		edad: Entero
	proceso
		Escribir("ingresar dia Nacimiento: ");
		leer(dia)
		Escribir("ingresar mes Nacimiento: ");
		leer(mes)
		Escribir("ingresar año Nacimiento: ");
		leer(anio)

		Escribir("ingresar dia actual: ");
		leer(diaA)
		Escribir("ingresar mes actual: ");
		leer(mesA)
		Escribir("ingresar año actual: ");
		leer(anioA)

		15/07/2002  14/03/2003
		edad:= (anioA - anio) ; //20
		si(mesA <= mes) entonces //7 <= 7
			si(diaA <= dia)entonces //12 <=  15
				edad:= edad - 1; // 19
			Finsi
		Finsi
		Escribir("La edad es: ", edad)
fin_Accion