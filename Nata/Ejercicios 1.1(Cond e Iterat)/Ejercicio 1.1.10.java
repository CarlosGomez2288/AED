Ejercicio 1.1.10
Dados dos números enteros A y B generar un algoritmo que permita determinar si A es divisor de B o B es divisor de A.

Acción 1.1.10 Es
Ambiente
    A,B: numericos
Proceso
    Esc("Ingrese los numeros que desee")
    Leer(A,B)
    Si A MOD B = 0 Entonces
        Esc("El número",A,"es divisor de",B)
    FinSi
    Si B MOD A = 0 Entonces
        Esc("El número",B,"es divisor de",A)
    FinSi
FinAcción