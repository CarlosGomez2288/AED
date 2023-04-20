Ejercicio 2.1.1
Dada una secuencia de letras del alfabeto que finaliza con una marca '*',
contar cuantas letras "A" hay en la secuencia.

Acción 2.1.1 Es
Ambiente
    Cont:alfanumerico
    v,Sec:alfanumerico
Proceso
    ARR(Sec)
    AVZ(v,Sec)
    Mientras (v<>"*") Hacer
        Si (v="A") Entonces
            Cont:=Cont+1
        FinSi
        Avz(v,Sec)
    FinMientras
    Escribir("la cantidad de letras A que se encontraron son:",Cont)
    Cerrar(Sec)
FinAccion