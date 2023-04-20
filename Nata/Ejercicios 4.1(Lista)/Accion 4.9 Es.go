Accion 4.9 Es(Prim: puntero a NODO)
Ambiente
    r=registro
        Multiplicador: N(5)
        prox: puntero a NODO
    finregistro
    P,P2,Prim,Prim2,A: puntero a NODO

    A:arreglo de[1..255] de caracter
    i: entero
	Multi

Proceso
	Esc("Cuantos caracteres desea que tenga su mensaje menor a 255 caracteres?");Leer(numerito)
    Para i:=1 hasta numerito hacer
        Esc("Ingrese un caracter del texto que desea ingresar")
		Leer(A[i])
    FinPara
	Prim2:=Nill
    Para i:=1 hasta 255 hacer
		P:=Prim
        Para x:=1 hasta i hacer
			P:=*P.prox
		FinPara
		Multi:=(*P.Multiplicador)*ASCCI(A[i])

		Valorcito:=0
		Mientras (Multi>9) hacer
			Descomponer:=Multi MOD 10
			Valorcito:=Valorcito + Descomponer
			Multi:=MUlti DIV 10
		FinMientras
		Valorcito:=Valorcito+Multi

		NUEVO(Q)
		*Q.Multiplicador:=Valorcito
		*Q.prox:=Nill
		Si Prim2 = Nill entonces
			Prim2:=Q
		Sino
			*A.prox:=Q
		FinSi
		A:=Q
	FinPara
FinAccion

			


