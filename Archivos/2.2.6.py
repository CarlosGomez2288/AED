accion 2.2.6 es
    ambiente

        Facultad = Registro
            ApyNom:AN(50);
            Promedio:N(2,2);
        finRegistro

        arch_facu: Archivo de Facultad;
        reg_facu:Facultad;

        cont_S, cont_N,cont_F,cont_MF, cont_Gral:N(4);
        Prome:N(2,2);

        # Procedimiento para mostrar por pantalla segun el Promedio
        Procedimiento Mostrar(reg_fac:Facultad, num:N(2))
            segun ( num ) hacer
                1:Esc(reg_fac.ApyNom," ", reg_fac.Promedio," Recomendación NO");
                2:Esc(reg_fac.ApyNom," ", reg_fac.Promedio," Recomendación SI");
                3:Esc(reg_fac.ApyNom," ", reg_fac.Promedio," Recomendación F");
                4:Esc(reg_fac.ApyNom," ", reg_fac.Promedio," Recomendación MF");
                Otros: Esc("Fuera de rango");
            finsegun
        finprocedimiento
    proceso
        cont_Gral:=0; cont_S:=0; cont_N:=0; cont_F:=0; cont_MF:=0;
        Abrir E/(arch_facu);
        leer(arch_facu,reg_facu);
        
        Mientras NFDA(arch_facu) hacer
            cont_Gral:= cont_Gral + 1;

            si(reg_facu.Promedio < 7) entonces
                cont_N:= cont_N + 1;
                Mostrar(reg_facu,1);
            sino
                si(reg_facu.Promedio < 8 ) entonces
                    cont_S:= cont_S + 1;
                    Mostrar(reg_facu,2);

                sino
                    si(reg_facu.Promedio < 9 ) entonces
                        cont_F:= cont_F + 1;
                        Mostrar(reg_facu,3);
                    sino
                        si(reg_facu.Promedio >= 9) entonces
                            cont_MF:= cont_MF + 1;
                            Mostrar(reg_facu,4);
                        finsi
                    finsi
                finsi
            finsi
            leer(arch_facu,reg_facu);
        finMientras
        Prome:= (cont_S + cont_N + cont_F + cont_MF)/cont_Gral;
        Esc("EL TOTAL DE GRADUADOS CON UN PROMEDIO MENOR A 7 ES:", cont_N);
        Esc("EL TOTAL DE GRADUADOS CON UN PROMEDIO MENOR A 8 ES:", cont_S);
        Esc("EL TOTAL DE GRADUADOS CON UN PROMEDIO MENOR A 9 ES:", cont_F);
        Esc("EL TOTAL DE GRADUADOS CON UN PROMEDIO MENOR A 10 ES:",cont_MF);
        Esc("el promedio global es:", Prome);
    finProceso
finaccion