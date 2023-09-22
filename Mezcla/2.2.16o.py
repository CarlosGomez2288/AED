accion 2.2.16 Ex es
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


    proceso
    abrir s/(archi_sal); abrir E/(archi_pelis); abrir E/(archi_nuevas);
    leer(archi_nuevas,resg_nuevas); leer(archi_pelis,resg_pelis);

    Mientras NFDA(archi_nuevas) y NFDA(archi_pelis) hacer
        si (resg_nuevas.Nro_peli < resg_pelis.Nro_peli) entonces
            resg_sal:= resg_nuevas;
            Esc(archi_sal,resg_sal);
            leer(archi_nuevas,resg_nuevas);
        sino
            si ( resg_nuevas.Nro_peli > resg_pelis.Nro_peli)entonces
                resg_sal:=resg_pelis;
                Esc(archi_sal,resg_sal);
                leer(archi_pelis,resg_pelis);
            sino
                si ( resg_nuevas.Nro_peli = resg_pelis.Nro_peli) entonces
                    resg_sal:=resg_nuevas;
                    Esc(archi_sal,resg_sal);
                    leer(archi_nuevas,resg_nuevas);
                    leer(archi_pelis,resg_pelis);
                finsi
            finsi
        finsi
    finMientras


    Mientras NFDA(archi_nuevas) hacer
        resg_sal.= resg_nuevas;
        Esc(archi_sal,resg_sal);
        leer(archi_nuevas,resg_nuevas);
    finMientras

    Mientras NFDA(archi_pelis) hacer
        resg_sal.= resg_pelis;
        Esc(archi_sal,resg_sal);
        leer(archi_sal,resg_sal);
    finMientras

    cerrar(archi_nuevas);
    cerrar(archi_pelis);
    cerrar(archi_sal); 
finaccion