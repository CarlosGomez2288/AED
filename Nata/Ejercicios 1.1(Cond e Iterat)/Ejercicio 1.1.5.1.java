Ejercicio 1.1.5.1
Escribir un programa que permita calcular el precio de un artículo para un año dado, considerando que la inflación es del 4 por 100 anual.

La fórmula del precio es: P = C * (1 + R) ^ (N - A)

C - Precio actual.
N - Año futuro.
R - Tasa de Inflación.
A - Año actual.

Ambiente
    //Variables
        C,N,A,R,Total: Numerico
    //Constantes
        R= 2022
Algoritmo
    Escribir("Ingrese el precio de su artículo")
    Leer(C)
    Escribir("Ingrese el año actual")
    Leer(A)
    Escribir("Ingrese el año futuro")
    Leer(N)

    Total= Precio * (1+Tasa) ^ (AñoF - AñoA)
    Escribir("El precio final del producto es:",Total)
FinAccion


