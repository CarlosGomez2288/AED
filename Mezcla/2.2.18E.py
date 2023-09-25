accion 2.2.18 es
    ambiente
        articulos = Registro
            cod_Pro:N(6);
            tipo:AN(20);
            Marca:An(20);
            descri:An(20);
            cant_unid:(20);
        finRegistro

        archi_suc1:archi_sec2,archi_sal:archivo de articulo;
        reg_sec1,reg_sec2,reg_sal:articulos;

        total,cant_s1,cant_sec2:Entero
    proceso
    abrir E/(archi_suc1); leer(archi_suc1,reg_sec1);
    abrir E/(archi_suc2); leer(archi_suc2,reg_sec2);
    abrir E/(archi_sal);

    total:=0;
    Esc("|Cod_Prod|	|Tipo| |Marca| |Descripción| |Cant_Suc_1| |Cant_Suc_2| |Total_Unidades|");


    Mientras NFDA(archi_suc1) y NFDA(archi_suc2) hacer
        si(reg_sec1.cod_Pro < reg_sec2.cod_Pro) entonces
            reg_sal:= reg_sec1;
            Esc(reg_sec1.cod_Pro, reg_sal.tipo, reg_sec1.Marca, reg_sec1.descri, reg_sec1.cant_unid, 0, reg_sec1.cant_unid);
            Esc(archi_sal,reg_sal);
            leer(archi_suc1,reg_sec1);
        sino
            si(reg_sec1.cod_Pro > reg_sec2.cod_Pro) entonces
                reg_sal:= reg_sec2;
                Esc(reg_sec2.cod_Pro, reg_sal.tipo, reg_sec2.Marca, reg_sec2.descri,0, reg_sec2.cant_unid, reg_sec2.cant_unid);
                Esc(archi_sal,reg_sal);
                leer(archi_suc2,reg_sec2);
            sino
                si(reg_sec1.cod_Pro > reg_sec2.cod_Pro) entonces
                    reg_sal:= reg_sec2;
                    total:=(reg_sec1.cant_unid+reg_sec2.cant_sec2);
                    Esc(reg_sec2.cod_Pro, reg_sal.tipo, reg_sec2.Marca, reg_sec2.descri,reg_sec1.cant_unid, reg_sec2.cant_unid, total);
                    Esc(archi_sal,reg_sal);
                    leer(archi_suc2,reg_sec2); leer(archi_suc1,reg_sec1);
                finsi
            finsi
        finsi
    finMientras

    Mientras NFDA(archi_suc1) hacer
        reg_sal:= reg_sec1;
        Esc(reg_sec1.cod_Pro, reg_sal.tipo, reg_sec1.Marca, reg_sec1.descri, reg_sec1.cant_unid, 0, reg_sec1.cant_unid);
        Esc(archi_sal,reg_sal);
        leer(archi_suc1,reg_sec1);
    finMientras

    Mientras NFDA(archi_suc1) hacer
        reg_sal:= reg_sec2;
        Esc(reg_sec2.cod_Pro, reg_sal.tipo, reg_sec2.Marca, reg_sec2.descri, 0, reg_sec2.cant_unid, reg_sec2.cant_unid);
        Esc(archi_sal,reg_sal);
        leer(archi_suc2,reg_sec2);
    finMientras
z
    cerrar(archi_sec2); cerrar(archi_suc2); cerrar(archi_sal);
finaccion