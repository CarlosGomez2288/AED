Accion 4.1 Es
Ambiente
	r=registro
		dato: entero
		posi: entero
		prox: puntero a NODO
	finregistro
	k,Cont: entero
	P,Q,A: puntero a NODO
Proceso
	Esc("Que opción desea realizar? Eliminar/Insertar/Acceder");Leer(Rta)

	Esc("Ingrese la posición solicitada");Leer(posi)
	Cont:=0

	Si Rta = "Acceder" entonces
		P:=Prim
		Mientras (P<>Nill) y (Cont<*P.posi) hacer
			P:=*P.prox
			Cont:=Cont+1
		FinMientras

		Si * = Nill entonces
			Error()
		Sino
			Si k>Cont entonces
				Error()
			Sino
				Esc("Se encontró la posición numero:",posi)
			FinSi
		FinSi
	Sino
		Si Rta = "Insertar" entonces
			Nuevo(Q)
			Si Prim = Nill entonces
				Error()
			Sino
				P:=Prim
				A:=Nill
				Mientras (P<>Nill y *P.posi<*Q.posi) hacer
					A:=P
					P:=*P.prox
				Si Prim = Nill
					Prim:=Q
					*Q.prox:=P
				Sino
					Si *P.posi > *Q.posi entonces
						Error
					Sino
						*A.prox:=Q
						*Q.prox:=P
					FinSi
				FinSi
			FinSi
		Sino
			P:=Prim
			Mientras (P<>Nill) y (*P.posi<>k)
				A:=P
				P:=*p.prox
			FinMientras
			Si P = Nill entonces
				Error()
			Sino
				*A.prox:=*P.prox
				Disponer(P)
			FinSi
		FinSi
	FinSi
FinAccion