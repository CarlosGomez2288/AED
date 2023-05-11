accion 2.2.4 es
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

        anioA:N(4);
        carrera_dada:An(3);
        
        arch_Fac, archi_Apro: Archivo de Facultad;
        reg_Fac, reg_apro: Facultad;
    proceso

        Abrir E/(arch_Fac); Abrir s/(archi_Apro);
        leer(arch_Fac,reg_Fac);
        
        Esc("Ingresar carrera ISI/IEM/LAR");
        leer(carrera_dada);
        Esc("ingresar año actual");
        leer(anioA);
        Mientras NFDA(arch_Fac) hacer
           si(carrera_dada = reg_Fac.Carrea) entonces
                si(reg_Fac.fecha_U.aa = anioA) y ( reg_Fac.nota > 7) entonces
                    reg_apro:= reg_Fac;
                    Esc(archi_Apro,reg_apro);
                finsi
          finsi
          leer(arch_Fac,reg_Fac);
        finMientras
        cerrar(arch_Fac);
        carrar(archi_Apro);
    finProceso
finaccion