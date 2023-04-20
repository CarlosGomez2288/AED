Ejercicio 1.1.19 y 20
Escribir un algoritmo que ingrese una variable V y emita el valor de ésta, su cuadrado y su cubo.

Ejercicio 1.1.20
Teniendo en cuenta el ejercicio anterior, realizar un incremento de la variable V en forma constante y creciente recalculando los demás valores 10 veces.

Por ejemplo


V=2

   V    V2    V3  
   2     4     8
   3     9    27
....  ....  ....
  12   144  1728

Acción 1.1.20
Ambiente
    V,V2,V3,x: numerico
Proceso
    Escribir("Ingrese un número")
    Leer(V)
    x:=V
    Para x:=1 hasta 10 Hacer
        V2:=V**2
        V3:=V**3
        Escribir("El numero es:",V,"su cuadrado:",V2,"y su cubo:"V3)
        V:=V+1
    FinPara
FinAccion
