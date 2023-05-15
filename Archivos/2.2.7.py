accion 2.2.7 es
    ambiente
        procedimiento secu(reg_padron:Padron)
        Padron=registro
            ApyNom:An(50);
            clase:N(4);
            DNI:N(8);
            dire:AN(50);
            n_Mesa:N(4);
            obser:AN(50);
            n_Cir:N(4);
            partido = {0,1,2,3};
        finregistro 

        arch_Padron: archivo de Padron
        reg_padron:Padron

        Salida = registro
            ApyNom:An(50);
            DNI:N(8);
            dire:AN(50);
        finRegistro
        
        arch_C, arch_N: Archivo de Salida;
        reg_C,reg_N:Salida;
    proceso
        abrir E/(arch_Padron); abrir S/(arch_C); abrir S/(arch_N);
        leer(arch_Padron, reg_padron);

        Mientras NFDA(arch_Padron) hacer
            si(reg_padron.partido = 3 ) entonces
                reg_C.ApyNom:= reg_padron.ApyNom;
                reg_C.DNI:= reg_padron.DNI;
                reg_C.dire:= reg_padron.dire;
                Esc(arch_C,reg_C);
            sino
                si(reg_padron.partido = 0) y (reg_padron.clases > 1940) entonces
                    reg_N.ApyNom:= reg_padron.ApyNom;
                    reg_N.DNI:= reg_padron.DNI;
                    reg_N.dire:= reg_padron.dire;
                    Esc(arch_N,reg_N);
                finsi
            finsi
            leer(arch_Padron,reg_padron);
        finMientras
        cerrar(arch_Padron); cerrar(arch_N); cerrar(arch_C);
finaccion
