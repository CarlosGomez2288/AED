accion 2.1.24 es
    ambiente
        secNombre, secDNI, salidad:Secuencia de caracteres
        v1,v2:caracter
        vocal = {"a","e","i","o","u"}
    proceso
        arr(secNombre);arr(secDNI);crear(salida);
        avz(secNombre,v1); avz(secDNI,v2);

        Mientras NFDS(secNombre) y NFDS(secDNI) hacer
            si( v1 no en vocal) hacer
                Mientras( v1 = " ") hacer
                    avz(secNombre, v1);
                finMientras

                para i = 1 hasta 8 hacer
                    Esc(salida,v2);
                    avz(secDNI,v2);
                finpara
                Esc(salida,",");

                Mientras ( v<> " ") hacer
                    Esc(salida, v1);
                    avz(secNombre,v1);
                finMientras
                Esc(salida,"#");
            sino
                Mientras( v1 = " ") hacer
                    avz(secNombre, v1);
                finMientras

                para i = 1 hasta 8 hacer
                    avz(secDNI,v2);
                finpara

                Mientras ( v<> " ") hacer
                    avz(secNombre,v1);
                finMientras
            finsi
        finMientras
        cerrar(secNombre);cerrar(secDNI); cerrar(salida);
        Esc("Secuencia creada...")
    finProceso
finAccion