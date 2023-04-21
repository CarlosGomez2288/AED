# Se dispone de una secuencia de números de DNI asignados a un circuito electoral, 
# generar otra secuencia de números que contenga los DNI múltiplos de 3.
accion 2.1.16 es
    ambiente
        sec, sec2:secuencia de enteros;
        v:Entero;
    proceso
        arr(sec);
        avz(sec,v);
        crear(sec2);

        Mientras NFDS(sec) hacer

            si (v mod 3 == 0) entonces
                Esc(sec2, v);
            finsi

            avz(sec,v);
        finMientras
        cerrar(sec); cerrar(sec2); 
        Esc("Secuencia creada.")
    finProceso
finAccion