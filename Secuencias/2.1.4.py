accion 2.1.4 es
    ambiente
        s:secuencia alfanumerico
        v, cont:Entero
    proceso
        cont:=0;
        arr(s)
        avz(s,v)
        Mientras NDFS(S) hacer
            cont:= cont + 1;
            avz(s,v)
        finMientras
        Esc("En la secuencia hay ", cont , "socio")
        cerrar(s);
finaccion
