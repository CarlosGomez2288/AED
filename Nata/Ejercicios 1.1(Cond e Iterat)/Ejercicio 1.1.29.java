Ejercicio 1.1.29
Escriba un algoritmo para imprimir los números primos menores a un valor dado n.

Accion 1.1.29 Es
Ambiente
    N,N1,primo,Primos: numerico
Proceso
    Escribir("Ingrese un numero")
    Leer(N)
    N1:=N-1 //N=20
    Para i:=2 hasta N1,1 Hacer //N1=19
        Si i=1 o i=2 o i=3
            Escribir("El numero",i,"es primo")
        Sino 
            Si(N1 MOD i = 0) Entonces //
                primo:=i
            FinSi
        
    FinPara
    Escribir("Los números primos menores a ",N,"son:",Primos)
FinAccion