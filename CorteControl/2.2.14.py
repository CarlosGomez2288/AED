accion 2.2.14 es
    ambiente
        forma= Registro
            radio:N(2);
            manzana:AN(10);
            nro_vivienda:N(2);
        finRegistro

        Censo = Registro
            clave: forma
            condi:["buena","muy buena","mala"];
            cant_habi:N(4);
        finRegistro

        archi: Archivo de Censo ordenado por clave;
        reg:Censo

        total_ci,total_ra,total_ma:N(4);
        resg_ma:AN(10);
        resg_ra:N(2);

        Procedimiento corteManzana() es:
            Esc("El total de habitantes por manzana", resg_ma," es de,"total_ma);
            total_ra:=total_ra + total_ma;
            total_ma:=0;
            resg_ma:= reg.clave.manzana;
        finProcedimiento

        Procedimiento corteRadio() es:
            corteManzana();
            Esc(El total de habitantes por Radio, resg_ra, "es de ", total_ra);
            total_ci:= total_ci + total_ra;
            total_ra:= 0;
            resg_ra:= reg.clave.radio;
        finProcedimiento

    proceso
        abrir E/(archi); leer(reg,archi);
        total_ci:=0;,total_ra:=0;,total_ma:=0;

        resg_ma:= reg.clave.manzana;
        resg_ra:= reg.clave.radio;

        Mientras NDFA(archi) hacer
            Si( reg.clave.radio <> resg_ra) entonces
                corteRadio();
            sino
                si(reg.clave.manzana <> resg_ma) entonces
                    corteManzana();
                finsi
            finsi

            si (reg.condi = "muy buena") entonces
                total_ma:= total_ma + reg.cant_habi;
            finsi
            leer(reg,archi);
        finMientas
        corteRadio();
        Esc("El total en la ciudad es",total_ci);
        cerrar(archi);
    finProceso
finaccion