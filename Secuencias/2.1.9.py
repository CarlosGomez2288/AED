accion 2.1.9 es
    ambiente
        sec:secuencias de caracteres;
        v: caracteres;
        cont:entero; 
    proceso
        cont:= 0;
        arr(sec);
        avz(sec, v);

        Mientras NFDS(sec) hacer

            Mientras (V = " ") hacer
                avz(sec, v);
            finMientras

            Si ( v= "I ") entonces
                cont:= cont + 1;
            finsi

            Mientras NFDS(sec) y (v <> " ") hacer
                avz(sec, v)
            finMientras
        finMientras
        cerrar(sec);
        Esc("La palabra que hay son ", cont);
finaccion