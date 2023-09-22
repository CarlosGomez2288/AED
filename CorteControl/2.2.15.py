accion 2.2.15 es
    ambiente
        fecha =Registro
            aa:N(4);
            mm:1..12;
            dd:1..31;
        finRegistro

        Alumnos =Registro 
            clave= Resgistro
                Esc:AN(30);
                anio:fecha;
                divi:AN(10);
            finRegistro
            nom:AN(50);
            cant_Ina:N(4);
        finRegistro

        archi: Archivo de Alumnos ordenados por clave
        reg:Alumnos;

        tota_Esc,total_alumno;total_aR;total_aL:N(4);
        total_Inasi,cant_alumno,cant_aL,cant_aR,dias:N(4);

        Procedimiento corteDivi() es:
            Esc("La cantida de Alumno de la divicion ", resg_divi, "Cantidad", cant_alumno);
            total_alumno:= total_alumno + cant_alumno;
            total_aL:= total_aL + cant_aL;
            total_aR:= total_aR + cant_aR;

            cant_aL:=0;
            cant_aR:=0;
            cant_alumno:=0;

            resg_div:=reg.clave.divi;
        finProcedimiento

        Procedimiento corte_año() es
            corteDivi();
            Esc("La cantidad total de alumno libres es", total_aL);
            Esc("La cantida total de alumno Regular es: total_aR");
            Esc("La cantidad de alumos es: ",total_alumno);

            tota_Esc:= total_esc + (total_aL + total_aR);

            total_aL:=0;
            total_aR:=0;
            total_alumno:=0;
            resg_año:= reg.clave.anio;
        finProcedimiento

        Procedimiento corte_esc() es:
            corte_año();
            Esc("La cantidad de alumno es ", tota_Esc);
            Esc("El porcentaje de alumno libre es: ",(total_aL/tota_Esc)*100);
            Esc("El promedio de inasistencia es: " total_Inasi_Inasi/tota_Esc);

            tota_Esc:=0;
            total_Inasi:=0;
            resg_esc:=reg.clave.Esc;
        finProcedimiento
    proceso
        tota_Esc:=0,total_alumno:=0;total_aR:=0;total_aL:=0;
        total_Inasi:=0,cant_alumno:=0,cant_aL:=0,cant_aR:=0;

        abrir E/(archi); leer(archi,reg);

        resg_año:=reg.clave.anio;
        resg_divi:=reg.clave.divi;
        resg_esc:=reg.clave.Esc;

        Esc("Ingresar cantida de dias");
        leer(dias);

        Mientras NFDA(archi) hacer
            si(resg_esc <> reg.clave.Esc)entonces
                corte_esc();
            sino
                si(resg_año <> reg.clave.anio)entonces
                    corte_año();
                sino
                    si(resg_divi <> reg.clave.divi) entonces
                        corteDivi();
                    finsi
                finsi
            finsi

            cant_alumno:= cant_alumno + 1;
            cant_Inasi:= cant_Inasi + reg.cant_Ina;

            si(reg.cant_Ina > (dias * 0.2)) entonces
                cant_aL:= cant_aL + 1;
            sino
                cant_aR:= cant_aR + 1:
            finsi
            leer(archi,reg);
        finMientas
        corte_esc();
        cerrar(archi);
    finProceso
finaccion