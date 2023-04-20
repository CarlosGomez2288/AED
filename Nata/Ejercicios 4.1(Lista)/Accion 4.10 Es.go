Accion 4.10 Es(Prim,Prim2,ULT:puntero a NODO)
Ambiente
	r=registro
		Num: N(5)
		prox: puntero a NODO
	finregistro
	P,Prim: puntero a NODO

	r2=registro
		Conjunto: N(5)
		ant,prox: puntero a NODO
	finregistro
	Prim2,Q,ULT,P2: puntero a NODO

	C,n: entero
	prom: real
	Max,Min: entero
Proceso
	P:=Prim
	Prim2:=Nill
	ULT:=Nill
	Max:=LV;Min:=HV

	Mientras (*P.prox<>Prim) hacer
		C:=0
		n:=*P.Num
		Para (i:=1 hasta n) hacer
			P:=*P.prox
			C:=C+*P.Num
		FinPara
		prom:=C/n
		Nuevo(Q);*Q.Conjunto:=prom

		P2:=Prim2
		Si Prim2=Nill entonces
			*Q.prox:=Nill
			*Q.ant:=Nill
			ULT:=Q
			Prim2:=Q
		Sino
			P2:=Prim2
			Mientras (P2<>Nill) y (*P2.Conjunto<*Q.Conjunto) hacer
				P2:=*P2.prox
			FinMientras
			Si P2=Prim2 entonces
				*Q.prox:=P2
				*Q.ant:=Nill
				*P2.ant:=Q
				Prim2:=Q
			Sino
				Si P2=Nill entonces
					*Q.prox:=Nill
					*Q.ant:=ULT
					*ULT.prox:=Q
					ULT:=Q
				Sino
					*Q.prox:=P2
					*Q.ant:=*P2.ant
					*(*P2.ant).prox:=Q
					*P2.ant:=Q
				FinSi
			FinSi
		FinSi
		P:=*P.prox
	FinMientras

	P2:=Prim2
	Mientras (P<>Nill) hacer
		Si *P2.Conjunto < Min entonces
			Min:=*P2.Conjunto
		FinSi
		Si *Q.Conjunto > Max entonces
			Max:=*P2.Conjunto
		FinSi
		P:=*P.prox
	FinMientras
		
	Esc("El máximo del promedio del conjunto de numeros es:",Max)
	Esc("El mínimo del promedio del conjunto de numeros es:",Min)
FinAccion