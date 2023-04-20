Ejercicio 1.1.28
Construya un algoritmo capaz de encontrar todas las cifras de 
tres dígitos que cumplan con la condición de que la suma de 
los cubos de sus dígitos sea igual al número que la cifra 
representa.

Accion 1.1.28 Es
Ambiente
    Cen,Dec,Uni,Total:numerico
Proceso
    Para i:=100 hasta 999 Hacer
        Cen:=(Num MOD 100)**3
        Dec:=((Num MOD 100) DIV 10)**3
        Uni:=((Num MOD 100) MOD 10)**3
        Total:=Cen+Dec+Uni
        Si (Total = i) Entonces
            Escribir("La suma representa el valor inicial")
        Sino
            Escribir("La suma  no representa el valor inicial")
    FinPara
FinProceso



