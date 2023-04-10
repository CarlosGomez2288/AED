Se dispone de una secuencia de caracteres y se desea obtener una secuencia de salida que resulte
de copiar la secuencia de entrada, descartando el caracter "$".
accion 2.1.3 es
    ambiente
        s, s2:secuencia de caracter
        v:caracter
    proceso
        arr(s)
        crear(s2)
        avz(s,v)

    Mientras NDFS(s) hacer
         si (v <> "$") entonces
            Esc(s2,v)
        FinSi
        avz(s,v)
    finMientras
    cerrar(s)
    cerrar(s2)
finaccion