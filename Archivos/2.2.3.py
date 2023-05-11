accion 2.2.3 es
    ambiente
        Biblioteca = Registro
            N_socio:N(4);
            N_tele:N(8);
            ApyNom:AN(50);
            Carrea= {"ISI","IEM","LAR"}
            Domi:AN(50);
            cant:N(4);
        finRegistro

        Archi_biblio, archi_Isi: Archivo de Biblioteca
        reg_bilio, reg_Isi:Biblioteca;
    proceso
        abrir E/(Archi_biblio); abrir S/(archi_Isi);
        leer(Archi_biblio,reg_bilio);
        
        Mientras NFDA(Archi_biblio) hacer
            si(Archi_biblio.Carrera = "ISI") entonces
                Si ( reg_bilio.cant > 4) entonces
                    reg_Isi:= reg_bilio;
                    Esc(archi_Isi,reg_Isi);
                finsi
            finsi
            leer(Archi_biblio,reg_bilio);
        finMientras

        cerrar(archi_Isi);
        cerrar(Archi_biblio);
    finProceso
finaccion