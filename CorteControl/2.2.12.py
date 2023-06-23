accion 2.2.12 es
    ambiente
        FormatoClave = Resgistro
            provin:AN(30);
            Depar:AN(30);
            ciud:AN(30);
            Barrio:AN(30);
            Id:N(4);
        finRegistro

        Poblacion = Registro
            clave:FormatoClave;
            cantidad:N(4);
        finRegistro

        archi: archivo de Poblacion ordenados por clave;
        reg:Poblacion;

        salida = Resgistro
            provin:AN(30);
            Depar:AN(30);
            cantidad:N(4);
        finRegistro

        archi_sal:archivo de salida;
        reg_sal:salida

        resg_depa:AN(30); resg_pro:N(30);

        Procedimiento cortePro() es:
            corteDepa();
            resg_pro:= reg.clave.provin;
        finProcedimiento

        Procedimiento corteDepa() es:
            reg_sal.provin:= resg_pro;
            reg_sal.depa:=resg_depa;
            reg_sal.cantidad:= cant_habi;
            Esc(archi_sal,reg_sal);

            cant_habi:= 0;
            resg_depa:= reg.clave.Depar;
        finProcedimiento
    proceso
        abrir E/(archi); abrir S/(archi_sal); leer(archi,reg);
        cant_habi:= 0;

        resg_depa:= reg.clave.Depar;
        resg_pro:= reg.clave.provin;

        Mientras NDFA(archi) hacer
            si( resg_pro <> reg.clave.provin) entonces
                cortePro();
            sino
                si(resg_depa <> reg.clave.Depar) entonces
                    corteDepa();
                finsi
            finsi

            cant_habi:= cant_habi + reg.cantidad;

            leer(archi,reg);
        finMientas
        cortePro();
        cerrar(archi_sal); cerrar(archi);

    finProceso
finaccion