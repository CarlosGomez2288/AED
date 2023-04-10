accion 1.1.30 es
    ambiente
        sueldo, cat, i:Entero
        asistencia:Alfamunerico
    proceso

        para i:= 1 hasta 100 hacer
            Esc("¿A que categoria pertenece 1 o 2?")
            leer(cat)
            Esc("El trabajador tiene asistencia perfecta? si o no");
            leer( asistencia)

            si ( cat = 1) entonces
                sueldo:=  ( 700* 1,02);
            sino
                si(cat = 2) entonces
                    sueldo:=  ( 700* 1,02);
                finsi
            finsi

            si( asistencia = "si") entonces
                sueldo:= sueldo + 200;
            finsi

            Esc("El sueldo para el trabajaor: ", i, "Es $", sueldo);
        finpara
        
finaccion