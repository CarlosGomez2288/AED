Accion 1.1.10 es
    ambiente
        anio:Entero(4)
    proceso

        Esc("ingresar el año");
        leer(anio)

        segun ( anio ) hacer
            2023 = anio: Esc("ACTUAL");
            < 2023: Esc("PASADO");
            anio>2023: Esc("FUTURO");
        finSegun
finAccion