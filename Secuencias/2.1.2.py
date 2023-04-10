Dada una secuencia de letras del alfabeto que finaliza con la letra "Z", contar cuantas consonantes hay en la secuencia.
accion 2.1.2 es
    ambiente
        s:secuencia de caracter
        v:caracter
        cont:Entero
    proceso
        arr(s)
        cont:=0;

        repetir
            avz(s,v)
            si Not(v en vocal ) entonces
                cont:= cont + 1;
            FinSi
        hasta que (v = z)

        Esc("En la secuencia hay ", cont, " consonantes");
        cerrar(s)
finaccion