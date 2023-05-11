accion 2.1.22 es
    ambiente
        secNombre, secDNI, salidad:secuencia de caracteres
        v1, v2:caracter
        contP:Entero

    proceso
    arr(secNombre);
    arr(secDNI);
    avz(secNombre, v1);
    avz(secDNI,v2);

    Mientras NFDS(secNombre) y NFDS(secDNI) hacer 
        contP.= contP + 1;
        si(contP mod 2 <> 0 ) entonces

            Mientras( v1 = " ") hacer 
                avz(secNombre,v1);
            finMientras

            para i = 1 hasta 8 hacer 
                Esc(salida, v2); 
                avz(secNombre,v1);
            finpara
            Esc(salida, ",");

            Mientras( v<> " ") hacer
                Esc(salida,v1);
                avz(secNombre,v1);
            finMientras
            Esc(salida,"#");
        sino
            Mientras( v1 = " ") hacer
                avz(secNombre,v1);
            finMientras

            para i = 0 hasta 8 hacer
                avz(secNombre,v1);
            finpara
            
            Mientras( v<> " ") hacer
                avz(secNombre,v1);
            finMientras
            
        finsi
    finMientras
    cerrar(secNombre);cerrar(secDNI); cerrar(salida);
    Esc("Secuencia creada...")
    fin_proceso
finAccion