accion 2.2.1 es
    ambiente
        Fecha= Registro
            dd:1..31;
            mm:1..12;
            aa:n(4);
        finRegistro

        Facultad = Registro
            ApyNom:AN(50);
            Carrea= {"ISI","IQ","IEM"};
            N_Leg:N(4);
            fecha_N:Fecha;
            fecha_I:Fecha;
            DNI:N(8);
            sex= {"F","M"}
            fecha_U:fecha;
            nota:N(2);
        finRegistro

        arch_Fac: Archivo de Facultad;
        reg_Fac: Facultad;
    proceso

        Abrir E/(arch_Fac);
        leer(arch_Fac,reg_Fac);

        Mientras NFDA(arch_Fac) hacer
            Esc(reg_Fac.N_Leg, reg_Fac.ApyNom, reg_Fac.DNI, reg_Fac.Carrea);
            leer(arch_Fac, reg_Fac);
        finMientras
        cerrar(arch_Fac);
    finProceso
finaccion