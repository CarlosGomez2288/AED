accion 2.2.16 es
    ambiente
        pelis = Registro
            Nro_peli:N(4);
            Titulo:AN(30);
            Genero:AN(30);
            Cant_co:N(4);
            Fecha= Resgistro
                aa:N(4);
                mm:1..12;
                dd:1..31;
            finRegistro
        finRegistro

        archi_nuevas, archi_pelis,archi_sal:Archivo de pelis ordenado por Nro_pelis;
        resg_nuevas,resg_pelis,resg_sal:pelis;

        procedimiento leer_nuevas() es
            leer(archi_nuevas,resg_nuevas);

            si FDA(archi_nuevas) entonces
                resg_nuevas.Nro_peli:= HV;
            finsi
        finprocedimiento

        procedimiento leer_pelis() es
            leer(archi_pelis,resg_pelis);

            si FDA(archi_pelis) entonces
                resg_pelis.Nro_peli:=HV;
            finsi
        finprocedimiento
    proceso

    abrir s/(archi_sal); abrir E/(archi_pelis); abrir E/(archi_nuevas);
    leer(archi_nuevas,resg_nuevas); leer(archi_pelis,resg_pelis);

    Mientras NFDA(archi_pelis) o NFDA(archi_nuevas) hacer
        si ( resg_nuevas.Nro_peli < resg_pelis.Nro_peli) entonces
            resg_sal.Nro_peli:= resg_nuevas.Nro_peli;
            resg_sal.Titulo:= resg_nuevas.Titulo;
            resg_sal.Genero:= resg_nuevas.Genero;
            resg_sal.Cant_co:= resg_nuevas.Cant_co;
            resg_sal.Fecha:= resg_nuevas.Fecha;
            Esc(archi_sal,resg_nuevas);
            leer_nuevas();
        sino
            si ( resg_nuevas.Nro_peli > resg_pelis.Nro_peli) entonces
                resg_sal.Nro_peli:= resg_pelis.Nro_peli;
                resg_sal.Titulo:= resg_pelis.Titulo;
                resg_sal.Genero:= resg_pelis.Genero;
                resg_sal.Cant_co:= resg_pelis.Cant_co;
                resg_sal.Fecha:= resg_pelis.Fecha;
                Esc(archi_sal,resg_nuevas);
                leer_pelis();
            sino
                si ( resg_nuevas.Nro_peli =  resg_pelis.Nro_peli) entonces
                    resg_sal.Nro_peli:= resg_nuevas.Nro_peli;
                    resg_sal.Titulo:= resg_nuevas.Titulo;
                    resg_sal.Genero:= resg_nuevas.Genero;
                    resg_sal.Cant_co:= resg_nuevas.Cant_co;
                    resg_sal.Fecha:= resg_nuevas.Fecha;
                    Esc(archi_sal,resg_nuevas);
                    leer_pelis();
                    leer_nuevas();
                finsi
            finsi
        finsi
    finMientras
 
finaccion