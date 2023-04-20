Accion 4.3 Es
Ambiente
	r=registro
		dato: entero
		prox: puntero a NODO
	finregistro
	P: puntero a NODO
	SumaI,SumaP: entero

Proceso
	SumaI:=0;SumaP:=0
	P:=Prim
	Mientras P<>Nil hacer
		Si *P.dato MOD 2 = 0 entonces
			SumaP:=SumaP + *P.dato
		Sino
			SumaI:=SumaI + *P.dato
		FinSi
		P:=*P.prox
	FinMientras

	Esc("Suma de pares:",SumaP)
	Esc("Suma de impares:",SumaI)
FinAccion



