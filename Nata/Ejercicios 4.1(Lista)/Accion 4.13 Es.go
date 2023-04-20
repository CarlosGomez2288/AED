Accion 4.13 Es(Prim:puntero a NODO)
Ambiente
	r=registro
		ant:puntero a NODO
		dato:entero
		prox:puntero a NODO
	finregistro
	P,aux: puntero a NODO

Proceso
	P:=Prim
	Mientras (P<>Nill) y (*P.dato <= *(*P.prox).dato) hacer
		P:=*P.prox
	FinMientras 
	Si P = Nill entonces
		Esc("La lista esta correctamente ordenada")
		Mientras (P<>Nill) hacer
			Si (*P.dato = *(*P.prox).dato) entonces
				Si P = Prim entonces
					Prim:=*P.prox
					*Prim.ant:=Nill
					Disponer(P)
				Sino
					Si P=ULT entonces
						ULT:=*P.ant
						*ULT.prox:=Nill
					Sino
						*(*P.prox).ant:=*P.ant
						*(*P.ant).prox:=*P.prox
					FinSi
				FinSi
			FinSi
			aux:=P
			P:=*P.prox
			Disponer(aux)
		FinMientras
		Esc("EXITO")
	Sino
		Esc("ERROR")
	FinSi
FinAccion