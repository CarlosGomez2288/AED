Ejercicio 2.1.9
Se dispone de una secuencia de caracteres.
Se desea determinar la cantidad de palabras que comienzan con la letra 'I'.

Accion 2.1.9 Es
Ambiente
    s: secuencia de caracteres
    v: caracteres
    cont: entero
Proceso
    ARR(s,v);AVZ(s,v)
    Mientras (v<>" ") hacer
        Mientras (v<>".") hacer
            Mientras (v<>",") hacer
                Si (v="l") entonces
                    cont:=cont+1
                FinSi
                AVZ(s,v)
            FinMientras
            AVZ(s,v)
        FinMientras
        AVZ(s,v)
    FinMientras
    Cerrar(s)
FinAcción
