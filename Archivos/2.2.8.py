accion 2.2.8 es
    ambiente
        Fecha= Registro
            aa:N(4);
            mm:1...12;
            dd:1...31;
        finRegistro 

        Compra = Registro
            Nro_Cliente:N(4);
            fecha_ult:Fecha;
            Monto:real
        finRegistro

        archi_com:Archivo de compra ordenado por Nro_Cliente;
        regcom:compra;

        clientes = Registro
            Nro_Cliente:N(4);
            ApyNombre:AN(50);
            domi:AN(50);
            Monto:real
        finRegistro

        archi_cli:Archivo de cliente ordenado por Nro_Cliente;
        regCli:clientes;

        fecha_dada:Fecha;
        monto_Dada:real
    proceso
    abrir E/(compra), abrir E/(cliente);
    leer(compra,regcom); leer(cliente,regCli);

    Esc("Ingresar fecha en el siguiente formato dd/mm/aa");
    leer(fecha_dada.dd,fecha_dada.mm,fecha_dada.aa);

    Esc("Inresar Monto");
    leer(monto_Dada);

    Mientras NFDA(archi_com) hacer
        #buscar el numero del cliente que coincida con le num de la compra
        Mientras (regCom.Nro_Cliente <> regClie.Nro_Cliente) hacer
            leer(archi_cli,regCli);
        finmientras

        si( regCom.fecha_ult > fecha_dada) y (regCom.Monto > monto_Dada) entonces
            Esc("Nombe: regClie.ApyNombre", "Fecha: " regCom.fecha_ult, " Monto: "regCom.Monto);
        finsi
        leer(archi_cli,regCli);
        leer(archi_com,regCom);
    finmientras
finaccion

proceso

