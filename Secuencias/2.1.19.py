# Dada una secuencia de caracteres, generar otra secuencia con todas las palabras de tres caracteres. 
# Informar el porcentaje de las mismas, sobre el total de palabras de la secuencia de entrada. 
# Considerar que puede haber más de un blanco entre palabras.
accion 2.1.19 es
    ambiente
        sec,sec2:secuencia de caracteres;
        v,c1,c2,c3:caracter;
        cont_P, cont_P3, cont_L:Entero;
        porce:= Real[2.2];
    proceso
        cont_P:= 0;
        cont_P3:= 0;
        porce:= 0;
        arr(sec);
        crear(sec2);
        avz(sec,v);

        Mientras NDFS(sec) hacer  #hol como era 
            cont_L:= 0;
            c1:= " ", c2:= " ", c3:= " ";

            Mientras(v=" ") hacer
                avz(sec,v);
            finMientras

            cont_P:= cont_P + 1;

            Mientras (v<>" ") y NFDS(sec) hacer #hol como 
                c1:= c2; #o
                c2 := c3;#m
                c3 := v; #o
                cont_L:= cont_L + 1; #1 2 3 4
                avz(sec,v);
            finMientras
            
            # Mientras (v <> " ") y NFDS(sec) hacer
            #     avz(sec,v);
            #     cont_L:= cont_L + 1;# 
            # finMientras

            Si (cont_L = 3) Entonces
                Esc(sec2,c1);
                Esc(sec2,c2);
                Esc(sec2,c3);
                cont_P3:= cont_P3 + 1;
            finsi
        finMientras
        cerrar(sec);
        cerrar(sec2);
        porce:= (cont_P3*100)/cont_P;
        Esc("El porcentaje de la palabra con 3 letra son: ", porce);
    finProceso
finAccion