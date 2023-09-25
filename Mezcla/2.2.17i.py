accicon 2.2.17 es
    ambiente

        Aspirantes = Registro
            dni:N(8);
            ApyNom:AN(20);
            carrera:{"ISI","IQ","IEM"};
            F_na:Fecha;
            email:AN(20);
            coleSc:AN(20)
            fecha_inscr:fecha;
            apro:{"si","NO"}
        finRegistro
        
        segui = Registro
            dni:N(8);
            ApyNom:AN(20);
            email:AN(20);
            coleSc:AN(20)
        finRegistro

        archi_fe,archi_agos:Archivo de Aspirantes ordenado por dni;
        reg_fe,reg_agos:Aspirantes;

        archi_sal: archivo de segui ordenado por dni;
        reg_sal:segui;

        cont:entero;

        procedimiento leer_fe() es
            leer(archi_fe,reg_fe);
            si FDA(archi_fe) entonces
                reg_fe.dni:=HV;
            finsi
        finprodecimiento

        procedimiento leer_agos() es
            leer(archi_agos,reg_agos);
            si FDA(archi_agos) entonces
                reg_agos.dni:=HV;
            finsi
        finprodecimiento

    proceso

        abrir E/(archi_fe); leer(archi_fe,reg_fe);
        abrir E/(archi_agos); leer(archi_agos,reg_agos);
        abrir S/(archi_sal);

        cont:= 0;

        Mientras NFDA(archi_fe) o NFDA(archi_agos) hacer
            si( reg_agos.dni < reg_fe.dni) entonces
                leer_agos();
            sino
                si( reg_agos.dni > reg_fe.dni) entonces
                    leer_fe();
                sino
                    si( reg_agos.dni = reg_fe.dni) entonces
                        si( reg_fe.apro = "NO") o ( reg_agos.apro = "NO") entonces
                            reg_sal.dni:= reg_agos.dni;
                            reg_sal.ApyNom:=reg_agos.ApyNom;
                            reg_sal.email:=reg_agos.email;
                            reg_sal.coleSc:=reg_agos.coleSc;
                            leer_agos(); leer_fe();
                            cont:= cont + 1;
                        finsi
                finsi
            finsi
        finMientras
        cerrar(archi_agos); cerrar(archi_fe); cerrar(archi_sal);
        Esc("Los aspirante en el seguimiento es de: ", cont);
finaccion