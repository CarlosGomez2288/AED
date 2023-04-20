Accion 2.3.11 Es
Ambiente
	Puntos=registro
		DNI: N(8)
		CantPuntos: N(10)
		UltCarga: Fecha
	Fin Registro
	PUNTOS: archivo de Puntos ordenado por DNI
	reg1: PUNTOS

	Cliente=registro
		DNI: N(8)
		ApeNom: AN(30)
		Edad: N(2)
		Ciudad: AN(50)
	Fin Registro
	CLIENTE: archivo indexado de Cliente ordenado por DNI
	reg2: CLIENTE

	Cargas=registro
		DNI: N(8)
		MedioPago={"DEBITO","EFECTIVO","CREDITO"}
		ApeNom: AN(30)
		FechaC: Fecha
		Ciudad: AN(50)
	Fin Registro
	CARGAS: archivo de Cargas ordenado por DNI
	reg3: Cargas

	Fecha=registro
		AA: N(4)
		MM: 1..12
		DD: 1..31
	Fin Registro

	Mayor,Nuevos: entero
	rta1,rta2={"SI","NO"}
	Importe,Monto: real
	Metod={"DEBITO","EFECTIVO","CREDITO"}

Proceso
	Abrir E/S(PUNTOS)//reg1
	Abrir E/(CLIENTE)//reg2
	Abrir E/(CARGAS);Leer(CARGAS,reg3)

	Nuevos:=0
	Mayor:=0

	Esc("Desea realizar una carga? SI/NO")
	Leer(rta1)

	Mientras rta1 = "SI" Hacer

		reg2.DNI:=reg3.DNI
		Leer(CLIENTE,reg2)

		Mientras NFDA(CARGAS) hacer
			Si existe Entonces
				Mientras NFDA(CARGAS) y reg2.DNI=reg3.DNI hacer
					Esc("Con que metodo de pago desea realizar? DEBITO/EFECTIVO/CREDITO")
					Leer(Metod)

					Esc("Ingrese el monto a cargar")
					Leer(Monto)

					Si Monto > 1000 Entonces
						Mayor:=Mayor+1
					FinSi

					Puntois:=((Monto DIV 100)*10

					Según Metod hacer
						="EFECTIVO":Puntois:=Puntois*A[1]
						="DEBITO":Puntois:=Puntois*A[2]
						="CREDITO":Puntois:=Puntois*A[3]
					FinSegún

					reg1.CantPuntos:=reg1.CantPuntos + Puntois
					reg1.UltCarga:=reg3.Fecha
					REGRABAR(PUNTOS,reg1)

					Leer(CARGAS,reg3)
				FinMientras
			Sino
				Esc("Ingrese su edad")
				Leer(Viejo)

				reg2.DNI:=reg3.DNI
				reg2.ApeNom:=reg3.ApeNom
				reg2.Edad:=Viejo
				reg2.Ciudad.reg3.Ciudad
				GRABAR(CLIENTE,reg2)

				Mientras NFDA(CARGAS) hacer
					Esc("Con que metodo de pago desea realizar? DEBITO/EFECTIVO/CREDITO")
					Leer(Metod)

					Esc("Ingrese el monto a cargar")
					Leer(Monto)

					Si Monto > 1000 Entonces
						Mayor:=Mayor+1
					FinSi

					Puntois:=((Monto DIV 100)*10

					Según Metod hacer
						="EFECTIVO":Puntois:=Puntois*A[1]
						="DEBITO":Puntois:=Puntois*A[2]
						="CREDITO":Puntois:=Puntois*A[3]
					FinSegún

					reg1.CantPuntos:=Puntois
					reg1.UltCarga:=reg3.Fecha
					reg1.DNI:=reg3.DNI
					GRABAR(PUNTOS,reg1)

				FinMientras

				Nuevo:=Nuevo+1
			FinSi
		Finmi
		
		Esc("Desea realizar otra carga? SI/NO")
		Leer(rta2)

		Si rta2 = "SI" Entonces
			Leer(CARGAS,reg3)
		FinSi

	FinMientras
	Esc("La cantidad de Clientes Nuevos son:",Nuevos)
	Esc("La cantidad de CLientes que pagaron mas de $1000 son:",Mayor)

	CERRAR(CARGAS)
	CERRAR(CLIENTE)
	CERRAR(PUNTOS)
FinAccion




