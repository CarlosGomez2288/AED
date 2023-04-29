accion 2.1.20
    ambiente
        sec1, sec2,salida:secuencia de caracteres
        v1, v2:caracter
        cont_O1, cont_O2:Entero
    proceso
        cont_O1:= 0, cont_O2:= 0;
        arr(sec1);
        arr(sec2);
        crear(salida);
        avz(sec1, v1);
        avz(sec2, v2);

        Mientras NDFS(sec1) y NFDS(sec2) hacer

                Mientras (v1  = " ") hacer #salta los blanco
                    avz(sec1, v1);
                finMientras

                Mientras( v1 <> ",") y ( v1 <> " ") hacer #copia el sujeto de la sec1
                    Esc(salida, v1);
                    avz(sec1, v);
                finMientras

                Esc(salida,v1);

                Mientras ( v1 <> ".") hacer #avanzo el  predicado sec1
                    avz(sec1, v1);
                finMientras

            avz(sec1,v1);
            cont_O1:= cont_O1 + 1;


            Mientras ( v2 <> ",") hacer #avanzo todo el sujeto de la sec2
                avz(sec2, v2);
            finMientras

                Mientras (v2 = " ") hacer
                    avz(sec2,v2);
                finMientras

                Mientras( v2 <> ".") y ( v2 <> " ") hacer #copia el predicado de la sec2
                    Esc(salida, v2);
                    avz(sec2,v2);
                finMientras
                
            Esc(salida,v2);
            avz(sec2,v2);
            cont_O2:= cont_O2 + 1;
        finMientras

        si FDS(sec1) entonces
            Mientras NDFS(sec2) hacer
                Mientras( v2 <> ".") hacer
                    avz(sec2,v2);
                finMientras
                cont_O2:= cont_O2 + 1;
                avz(sec2,v2)
            finMientras
        sino
            Mientras NDFS(sec1) hacer
                Mientras( v1 <> ".") hacer
                    avz(sec2,v2);
                finMientras
                cont_O:= cont_O1 + 1;
                avz(sec1,v1)
            finMientras
        finsi
        Esc("Primer Secuencia tine ", cont_O1," oraciones");
        Esc("Segunda  Secuencia tine ", cont_O2," oraciones");
        cerrar(sec1);
        cerrar(sec2);
        cerrar(salida);
finAccion