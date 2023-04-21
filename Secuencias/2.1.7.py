accion 2.1.7 es
    ambiente
        sec:secuencias de Enteros
        v, cuit:Enteros
        valid = {0,1,2,3};
    proceso
        arr(sec);
        
        repetir
            avz(sec,v);

            cuit:= (v mod 100 ) mod 10;

            si (((v mod 100) - c) en valid ) entonces 
                Esc(sec, v);
            finsi
        hasta que ( v <> 0 )

        cerrar(sec)
        Esc("Proceso Terminado");
    finProceso
finaccion