accion 2.1.23 es
    ambiente
        secNombre, secDNI, salida:Secuencia  de caracteres
        v1,v2:caracter
        num1:Entero;
        funcion convertir(num:entero):entero es -> #funcion para cambiar los tipos
            segun (num) hacer
                "1": convertir:=1;
                "2": convertir:=2;
                "3": convertir:=3;
                "4": convertir:=4;
                "5": convertir:=5;
                "6": convertir:=6;
                "7": convertir:=7;
                "8": convertir:=8;
                "9": convertir:=9;
                "0": convertir:=0;
            finsegun
        finFuncion
    proceso
        arr(secNombre); arr(secDNI); crear(salida);
        avz(secNombre, v1); avz(secDNI, v2);

        num1:= convertir(v2);

        Mientras NFDS(secNombre) y NFDS(secDNI) hacer
            si( num1 mod 2 <> 0 ) hacer -> # verifico si el dni comienza con impar

                Mientras( v1 = " ") hacer -> #Saltea los blancos
                    avz(secNombre, v1);
                finMientras

                para i = 1 hasta 8 hacer -> #copio el dni
                    Esc(salida,v2);
                    avz(secDNI,v2);
                finpara
                Esc(salida,",");

                Mientras( v <> " ") hacer -> #copio el nombre
                    Esc(salida,v1);
                    avz(secNombre,v1);
                finMientras
                Esc(salida,"#");
            sino -> #En caso que no comienze con impar
                Mientras( v1 = " ") hacer
                    avz(secNombre, v1);
                finMientras

                para i = 1 hasta 8 hacer
                    avz(secDNI,v2);
                finpara

                Mientras( v <> " ") hacer
                    avz(secNombre,v1);
                finMientras
            finsi
        finMientras
        cerrar(secNombre);cerrar(secDNI); cerrar(salida);
        Esc("Secuencia creada...")
    finProceso
finAccion