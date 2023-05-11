accion 2.2.2 es
    ambiente
        Fecha= Registro
            dd:1..31;
            mm:1..12;
            aa:n(4);
        finRegistro

        Factura = Registro
            N_Fac:N(8);
            fecha_Fac:Fecha;
            total:N(4);
        finRegistro

        arch_f:Archivo de Factura;
        reg_g:Factura;

        fecha_dada:Fecha;
    proceso
        Abrir E/(arch_f);
        leer(arch_f,reg_Fac);

        Esc("Ingresar fecha en el siguiente formato dd/mm/aa");
        leer(fecha_dada.dd,fecha_dada.mm,fecha_dada.aa);
        
        Mientras NFDA(arch_f) hacer
            si( reg_g.fecha_Fac > fecha_dada) entonces
                si(reg_g.total < 1001 ) entonces
                    Esc(reg_g.N_Fac,reg_g.fecha_Fac.dd,fecha_Fac.mm, fecha_Fac.aa, reg_g.total);
                finsi
            finsi
            leer(arch_Fac,reg_g);
        finMientras
        cerrar(arch_f);
    finProceso
finaccion