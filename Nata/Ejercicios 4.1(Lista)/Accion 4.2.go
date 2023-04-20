Accion 4.2 Es(Prim,Prim2: puntero a NODO)
Ambiente
    r=registro
        dato: entero
        prox: puntero a NODO
	finregistro
	P,Ant,Q: puntero a NODO

Proceso
	Prim2:=Nill
	Mientras (P<>Nill) hacer
		Nuevo(Q);*Q.dato:=*P.dato
		Si (P MOD 10 = 0) entonces
			Si Prim2=Nill entonces
				*Q.prox:=P
				Prim2:=Q
			Sino
				P:=Prim2
				Ant:=P
				Mientras(P<>Nill)y(*P.dato<*Q.dato)hacer
					Ant:=P
					P:=*P.prox
				FinMientras
				Si P=Prim entonces
					Prim:=Q
					*Q.prox:=Nill
				Sino
					*Ant.prox:=Q
					*Q.prox:=P
				FinSi
			FinSi
			P:=Prim
			Si Prim=Nill entonces
				Prim:=*P.prox
			Sino
				*Ant.prox:=*P.prox
			FinSi
			Disponer(P)
		Sino
			P:=*P.prox
		FinSi
	FinMientras
FinAccion






