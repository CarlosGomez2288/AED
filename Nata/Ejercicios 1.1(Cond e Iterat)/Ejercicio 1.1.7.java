Ejercicio 1.1.7
Escriba un algoritmo que acepte dos números, calcule la suma e imprima el mensaje de acuerdo al resultado obtenido.

Suma <= 50
Suma > 50 y <= 100
Suma > 100 y <= 200
Suma > 200

Acción 1.1.7
Ambiente
    A,B,Result: Numerico
Proceso
    Escribir("Ingrese dos números")
    Leer(A,B)
    Result:=A+b
    Escribir("el numero es:",Result)
    Según Result Hacer
        <=50: Escribir("El resultado es menor o igual a 50")
        >50 y <=100: Escribir("El resultado esta entre 50 y 100")
        >100 y <=200: Escribir("El resultado esta entre 100 y 150")
        >200: Escribir("El resultado es mayor a 200")
    FinSegún
FinAccion