accion 2.1.10 es
    ambiente
        sec:secuencia de caracteres
        v, letra: caracteres
        cont:Entero
    proceso
        cont:=0;
        arr(sec);
        avz(sec, v);
        Esc("ingresar letra");
        leer(letra);

        Mientras NFDS(sec) hacer

            Mientras (v  = " ") hacer
                avz(sec, v);
            finMientras

            Si( v = letra) hacer
                cont:= cont + 1;
            finsi

            Mientras NFDS(sec) y ( v <> " ") hacer
                avz(sec);
            finMientras
        finMientras
        cerrar(sec);
    finProceso
finaccion