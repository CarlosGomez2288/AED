accion 2.2.13 es
    ambiente
        forma =Resgistro
            cod_Suc:N(4);
            Marca:AN(20);
            Modelo:An(20);
            cod_Trag:N(4);
        finRegistro

        fecha= Registro
            aa:N(4);
            mm:1..12;
            dd:1..31;
        finRegistro

        Repa= Resgistro
            clave:forma;
            fecha_Re:fecha;
            costo_Re:N(4);
        finRegistro

        archi:Archivo de Repa ordenado por clave
        reg:Repa;

        res_codSuc:N(4);res_marc:AN(20);
        res_mod:AN(20);res_codTra:N(4);

        Procedimiento corte_Trag() es:
            Esc("La cantidad de reparaciones es de ", totra_rep);
            Esc("El costo  de la  reparaciones es de ", totra_cos);
            toMod_rep:= toMod_rep + totra_rep;
            toMod_cos:= toMod_cos + totra_cos;

            totra_cos:=0;
            totra_rep:=0;

            res_codTra:=reg.clave.cod_Trag;
        finProcedimiento

        Procedimiento corte_Mod() es:
            corte_Trag();
            Esc("La cantidad de reparaciones es de ", toMod_rep);
            Esc("El costo  de la  reparaciones es de ", toMod_cos);
            toMar_rep:= toMar_rep + toMod_rep;
            toMar_cos:= toMar_cos + toMod_cos;

            toMod_cos:=0;
            toMod_rep:=0;

            res_Mod:=reg.clave.Modelo;
        finProcedimiento

        Procedimiento corte_Mar() es:
            corte_Mod();
            Esc("La cantidad de reparaciones es de ", toMar_rep);
            Esc("El costo  de la  reparaciones es de ", toMar_cos);
            toCodS_rep:= toCodS_rep + toMar_rep;
            toCodS_cos:= toCodS_cos + toMar_cos;

            toMar_cos:=0;
            toMar_rep:=0;

            res_Mar:=reg.clave.Marca;
        finProcedimiento

        Procedimiento corte_CodS() es:
            corte_Mar();
            Esc("La cantidad de reparaciones es de ", toCodS_rep);
            Esc("El costo  de la  reparaciones es de ", toCodS_cos);
            toG_rep:= toG_rep + toCodS_rep;
            toG_cos:= toG_cos + toCodS_cos;

            toCodS_cos:=0;
            toCodS_rep:=0;

            res_Mar:=reg.clave.cod_Suc;
        finProcedimiento
    proceso
        abrir E/(archi);leer(reg);
        
        res_codSuc:= reg.clave.cod_Suc;
        res_Mar:= reg.clave.Marca;
        res_Mod:= reg.clave.Modelo;
        res_codTra:= reg.clave.cod_Trag;

        toCodS_cos:=0;toCodS_rep:=0;
        toG_cos:=0;toG_rep:=0;
        toMar_cos:=0;toMar_rep:=0;
        toMod_cos:=0;toMod_rep:=0;
        totra_rep:=0;totra_rep:=0;

        Mientras NDFA(archi) hacer
            si(res_codSuc <> reg.clave.cod_Suc) entonces
                corte_CodS();
            sino
                si(res_Mar <> reg.clave.Marca) entonces
                    corte_Mar();
                sino
                    si(res_Mod <> reg.clave.Modelo) entonces
                        corte_Mod();
                    sino
                        si(res_codTra <> reg.clave.cod_Trag)entonces
                            corte_Trag();
                        finsi
                    finsi
                finsi
            finsi

            totra_cos:= totra_cos + reg.costo_Re;
            totra_rep:= totra_rep + 1;

            leer(archi,reg);
        finMientas
        corte_CodS();
        Esc("El total  de repaciones es ", toG_rep);
        Esc("El Costo total de repaciones es ", toG_cos);
        cerar(archi)
    finProceso
finaccion