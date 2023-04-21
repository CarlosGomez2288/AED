accion 2.1.1 es
    ambiente
        s:secuenca de caracter
        v:caracter
        cont:Entero
    proceso
        cont:= 0;
        arr(s)
        avz(s,v)
        Mientras (v <> * ) hacer
            si ( v = "A") o (v = "a") hacer
                cont:= cont+ 1;
            finsi
            avz(s,b)
        finMientras
        cerrar(sec);
        Esc("En la secuencia hay ", cont," A");
finaccion