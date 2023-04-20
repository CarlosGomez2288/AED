Ejercicio 2.1.2
Dada una secuencia de letras del alfabeto que finaliza con la letra "Z", contar cuantas consonantes hay en la secuencia.

Acción 2.1.1 Es
Ambiente
    Cont:alfanumerico
    Vocal={"a","e","i","o","u","A","E","I","O","U"}
    v,Sec:alfanumerico
Proceso
    ARR(Sec)
    AVZ(v,Sec)
    Mientras (v<>"Z") Hacer
        Si (v=Vocal) Entonces
            Cont:=Cont+1
            AVZ(v,Sec)
        Sino
            AVZ(v,Sec)
        FinSi
    FinMientras
    Escribir("la cantidad de vocales que se encontraron son:",Cont)
    Cerrar(Sec)
FinAccion