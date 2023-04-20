Ejercicio 2.1.5
La secuencia de socios del problema anterior tiene el inconveniente
de que los números están ordenados pero no son correlativos.
Se desea generar una secuencia que contenga los números de socios
que no figuran en la secuencia de socios.

Acción 2.1.5 Es
Ambiente
    sec1,sec2:secuencia de enteros
    v1,v2: entero
Proceso
    ARR(sec1);AVZ(sec1,v1)
    Crear(sec2)
    cont:=v1
    Mientras NFDS(sec1,v) Hacer
        Si cont<>v Entonces
            v2:=cont
            Esc(sec2,v2)
        Sino
            AVZ(sec1,v1)
        FinSi
        cont:=cont+1
    FinMientras
    Cerrar(Sec1,v1);Cerrar(Sec2,v2)
FinAcción
