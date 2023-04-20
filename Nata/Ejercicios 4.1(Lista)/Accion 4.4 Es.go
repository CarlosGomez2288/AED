Accion 4.4 Es(Prim: puntero a NODO)
Ambiente
    r=registro
        dato:entero
        prox: puntero a NODO
    finregistro
    P,A: puntero a NODO
Proceso
    P:=Nill
    V:=Prim
    A:=Nill
    Mientras (V<>Nill) hacer
        P:=*V.prox
        *V.prox:=A
        A:=V
        V:=P
    FinMientras
FinAccion


