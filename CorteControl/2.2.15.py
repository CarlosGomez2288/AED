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

        Procedimiento corteDivi() es:
            Esc("La cantida de Alumno de la divicion ", resg_divi, "Cantidad", cant_alumno);
            total  
    proceso

    finProceso
finaccion