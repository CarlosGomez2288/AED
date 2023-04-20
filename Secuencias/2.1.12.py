Se dispone de una secuencia de caracteres. Se desea listar las palabras que comiencen con "ALG".
accion 2.1.12 es
    ambiente
        sec:secuencia de caracteres
        v:caracteres
    proceso
        arr(sec);
        avz(sec, v)

        Mientras NFDS(sec) hacer
            
            Mientras ( v = " ") hacer
                avz(sec,v);
            finMientras

            si(v = "A") Entonces
                avz(sec, v);
                si(v = "L") Entonces
                    avz(sec, v);
                    si(v = "G") Entonces
                        Esc("ALG");
                        avz(sec, v);
                         Mientras NFDS(sec) y ( v <> " ") hacer
                            avz(sec,v);
                        finMientras
                    finsi
                finsi
            finsi

            Mientras NFDS(sec) y ( v <> " ") hacer
                avz(sec,v);
            finMientras

        finMientras
        cerrar(sec);
finaccion
