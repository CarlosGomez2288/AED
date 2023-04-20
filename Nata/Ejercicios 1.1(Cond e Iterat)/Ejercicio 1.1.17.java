Ejercicio 1.1.17

Elabore un algoritmo que calcule el producto de dos enteros A y B empleando sólo la operación suma.

Acción 1.1.17 Es
Ambiente
    A,B,RESULT: numerico
Proceso
    Escribir("Ingrese 2 numeros")
    Leer(A,B)
    Result:=0
    Mientras (X<=B) Hacer
        Result:=Result + A
        X:=X+A
    FinMientras
    Escribir("El resultado del produc")