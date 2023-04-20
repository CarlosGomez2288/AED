Dada una secuencia de caracteres, determinar la cantidad de palabras de 4 caracteres
accion 2.1.11 es
    ambiente
        sec:secuencia de caracteres
        v:caracteres
        cont, contp:Entero
    proceso
        #hola estaria como estar
        arr(sec);
        avz(sec,v);

        Mientras NFDS(Sec) hacer  

            Mientras ( v = " ") hacer  #V:= 
                avz(sec, v);
            finMientras

            cont:= 0;
            Mientras ( v <> " ") hacer # hola estaria 
                cont:= cont + 1; #1 2 3 4 5 6 7
                avz(sec, v); 
            finMientras

            Mientras NFDS(sec) y ( v <> " ") hacer
                avz(sec, v)
            finMientras

            si( cont = 4) Entonces
                contp:= contp + 1; #1 2 
            finsi
        finMientras
        Esc("Hay", contp)
finaccion