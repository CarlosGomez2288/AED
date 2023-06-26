accion 2.8.9 es
    ambiente
        producto = Resgistro
            cod_Produc:N(4);
            tipo = {1,2,3};
            marca:AN(20);
            modelo:AN(30);
            descr:AN(50);
            cant_Exis:N(4);
            prec_Uni:N(4.2);
        finRegistro

        archi_Produc,archi_sal:Archivo de producto odenado por cod_Produc;
        reg,reg_sal: producto;

        cant_T1,cant_T2,cant_T3,total:N(4);
    proceso
        abrir E/(archi_Produc); abrir S/(archi_sal);
        leer(reg,archi_Produc);
        cant_T1:= 0;cant_T2:= 0;cant_T3:= 0;total:=0;

        Mientras NFDA(archi_Produc) hacer
            
            segun ( reg.tipo) hacer
                1:
                    cant_T1:= cant_T1 + 1;
                    reg_sal:=reg;
                    reg.prec_Uni:= prec_Uni + ( prec_Uni*0,10);
                2:
                    cant_T2:= cant_T2 + 1;
                    reg_sal:=reg;
                    reg.prec_Uni:= prec_Uni + ( prec_Uni*0,25);
                3:
                    cant_T3:= cant_T3 + 1;
                    reg_sal:=reg;
                    reg.prec_Uni:= prec_Uni + ( prec_Uni*0,50);
            finsegun
            total:=total + 1;
            Esc(archi_sal,reg_sal);

            leer(archi_Produc,reg);
        finmientras
        Esc("El total del tipo 1 es",cant_T1);
        Esc("El total del tipo 2 es",cant_T2);
        Esc("El total del tipo 3 es",cant_T3);
        Esc("El total General es",total);
        cerrar(archi_sal);cerrar(archi_Produc);
    finProceso
finaccion