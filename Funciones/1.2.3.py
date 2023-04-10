accion 1.2.3 es
    ambiente
        num:Entero
    proceso
        Repetir
            Para i:= 1 hasta 3 hacer
                Esc("ingresar el ", i, " numero");
                leer( num)
            finpara
        hasta que (op = "s")
finaccion