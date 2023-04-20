Ejercicio 1.1.22
Escriba un algoritmo que determine si un número es primo.

Accion 1.1.22 Entonces
Ambiente
    n,Prim:numerico
Proceso
    Escribir("Ingrese un numero para saber si es primo")
    Leer(n)
    Cont:=0
    Para i:=1 hasta n Hacer
        Si(n MOD i = 0) Entonces
            Prim:=n
        FinSi
        Cont:=Cont+1
    FinPara
    Escribir("El numero es primo")
FinAcción