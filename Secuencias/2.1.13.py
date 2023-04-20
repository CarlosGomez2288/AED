A partir del ejercicio anterior, determinar el porcentaje que representan las palabras que comienzan con "ALG" sobre todas 
las palabras de la secuencia.
accion 2.1.13 es
    ambiente
        sec: secuencia de caracteres;
        v: caracteres;
        contP, contA: Entero;
        porcen: real;

    proceso
        arr(sec);
        avz(sec, v);

        Mientras NFDS(sec) hacer
            Mientras (v = " ") hacer
                avz(sec, v);
            finMientras

            contP:= contP + 1;
            si(v = "A") Entonces
                avz(sec, v);
                si(v = "L") Entonces
                    avz(sec, v);
                    si(v = "G") Entonces
                        contA:= contA + 1;
                        avz(sec, v);
                        Mientras NFDS(sec) y (v <> " ") hacer
                            avz(sec, v);
                        finMientras
                    finsi
                finsi
            finsi

            Mientras NFDS(sec) y (v <> " ") hacer
                avz(sec, v);
            finMientras
        finMientras

        si (contP <> 0) entonces
            porcen:= (contA*100.0)/contP;
            Esc("El porcentaje de palabras que comienzan con 'ALG' es: ", porcen, "%");
        sino
            Esc("No se encontraron palabras en la secuencia");
        finsi

        cerrar(sec);
    finProceso
finAccion