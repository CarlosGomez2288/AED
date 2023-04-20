Ejercicio 2.1.11
Dada una secuencia de caracteres,
determinar la cantidad de palabras de 4 caracteres (letras)

aCCIÓN 2.1.11 Es
Ambiente
    sec: secuencia de entero
    v:caracter
    contp,contl:entero
Proceso
    ARR(sec);AVZ(sec,v)
    cont:=0
    Mientras NFDS(sec) Hacer
        Mientras (v=" ") Entonces
            AVZ(sec,v)
        FinSi
        contl:=0
        Mientras (v<>"" y NFDS(sec)) Hacer
            contl:=contl+1
            AVZ(sec,v)
        FinMientras
        Si (contl = 4) Entonces
            contp:=contp+1
        FinSi
    FinMientras
    Cerrar(sec)
FinAccion
