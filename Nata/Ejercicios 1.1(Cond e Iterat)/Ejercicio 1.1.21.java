Ejercicio 1.1.21
Repita el ejercicio anterior con un cálculo de n veces, con n > 1. Por final emitir la suma de los cuadrados de V.

Accion 1.1.21 Entonces
Ambiente
    V,V2,V3,Cont,n: numerico
Proceso
    Esscribir("Ingrese el numero que desee")
    Leer(V)
    Esscribir("Ingrese la cantidad de n veces que sea mayor a 1")
    Leer(n)
    V2:V**2
    V3:V**3
    Cont:=0
    Para i:=1 hasta n Hacer
        V2:=V**2
        V3:=V**3
        Cont:=Cont+V2
        Escribir("El numero es:",V,"su cuadrado:",V2,"y su cubo:"V3)
        V:=V+1
    FinPara
    Escribir("La suma de los cuadrados es",Cont)
FinAcción
    