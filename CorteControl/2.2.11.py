accion 2.2.11 es
    ambiente
        Fecha = Registro
            aa:N(4);
            mm:1...12;
            dd:1...31;
        finRegistro

        FormatoClave = Registro
                sex:{"F","M"}
                carrera:{"ISI","IQ","IEM"};
                lega:N(4);
            finRegistro
        Alumnos = Resgistro
            clave:FormatoClave
            fecha_Ing:Fecha;
            total_Materia:N(2);
        finRegistro

        archi:archivo de Alumnos ordenados por clave;
        reg: Alumnos;

        resg:FormatoClave

        total_me:N(2);total_mas:N(2); total:N(2);
        sex_me20:N(2); sex_mas20:N(4);carre_me:N(2); carre_mas20:N(2);
        
        Procedimiento corte_Sex() es
            corte_Carrera();
            Esc("Total de alumno que del sex",resg.sex," con mas de 20 materias aprobadas es:" sex_mas20_mas20);
            Esc("Total de alumno que del sex",resg.sex," con menos de 20 materias aprobadas es:" sex_me20);

            total_mas:= total_mas + sex_mas20;
            total_me:= total_me + sex_me20;

            sex_mas20:=0;
            sex_me20:=0;

            resg.sex:= reg.clave.sex;
        finProcedimiento

        Procedimiento corte_Carrera() es
            Esc("Total de alumno que de la carrera",resg.carrera," con mas de 20 materias aprobadas es:" carre_mas20);
            Esc("Total de alumno que de la carrera",resg.carrera," con menos de 20 materias aprobadas es:" carre_me20);

            sex_mas20:= sex_mas20 + carre_mas20;
            sex_me20:= sex_me20 + carre_me20;

            carre_mas20:=0;
            carre_me20:=0;

            resg.carrera:= reg.clave.carrera;
        finProcedimiento
    proceso
        abrir E/(archi); leer(archi,reg);
        resg.carrera:= reg.clave.carrera;
        resg.sex:= reg.clave.sex;

        total_me:=0;total_mas:=0;
        sex_me20:=0; sex_mas20:=0;carre_me:=0; carre_mas20:=0;

        Mientras NDFA(archi) hacer
            si(resg.sex <> reg.clave.sex) entonces
                corte_Sex();
            sino
                si(resg.carrera <> reg.clave.carrera) entonces
                    corte_Carrera();
                finsi
            finsi

            si(reg.fecha_Ing.aa = 2009) entonces
                si(reg.total_Materia > 20 ) entonces
                    carre_mas20:= carre_mas20 + 1;
                sino
                    si(reg.total_Materia < 20 ) entonces
                        carre_me:= carre_me20 + 1;
                    finsi
            finsi

            leer(archi,reg);
        finMientas
        corte_Sex();
        Esc("El total de alumno con mas de 20 materias es", total_mas);
        Esc("El total de alumno con menos de 20 materias es", total_me);
        cerar(archi);
    finProceso
finaccion