Ejercicio 2.1.6
Dada una secuencia de enteros que almacena la cantidad de habitantes
de las ciudades capitales de las 23 provincias de la República Argentina,
discriminados 4 categorías:
menores de 18 años (varones y mujeres) y
mayores de 18 años (varones y mujeres).
Se pide determinar la población total y los siguientes porcentajes:
masculinos, femeninos, mayores de 18 y menores de 18.

Acción 2.1.5 Es
Ambiente
    sec:secuencia de enteros
    v,Vmen,Vmay,Mmen,Mmay: entero
Proceso
    ARR(sec1);AVZ(sec1,v1)
    Vmen:=0,Vmay:=0,Mmen:=0,Mmay:=0
    Mientras NFDS(sec1,v) Hacer
        Vmen:=Vmen+v
        AVZ(sec1,v1)
        Vmay:=Vmay+v
        AVZ(sec1,v1)
        Mmen:=Mmen+v
        AVZ(sec1,v1)
        Mmay:=Mmay+v
        AVZ(sec1,v1)
    FinMientras
    Cerrar(Sec1,v1);Cerrar(Sec2,v2)
FinAcción