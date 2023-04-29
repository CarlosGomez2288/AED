accion 2.1.25 es
    ambiente
        sec, sec2:secuencia de caracteres;
        sec3:secuencia de enteros;
        v:caracter;
        cant_v,v2, cant_P, cant_O:Entero;
        PROM:Real
        vocal = {"a","e","i","o","u"};
    proceso
        cant_v:=0;
        arr(sec);
        avz(sec,v);
        crear(sec2);
        crear(sec3);
        Mientras NFDS(sec) hacer 

            Mientras (v<> ".") hacer

                Mientras(v = " ") hacer
                    avz(sec, v)
                finMientras
                cant_P:= cant_P + 1; 
            
               Si (v en vocal)entonces 
                    cant_v:= cant_v + 1; 
                    Mientras (v <> " ") y (v <> ".") hacer 
                        si( v en vocal) entonces
                            Esc(sec2, "#") 
                            cant_v:= cant_v + 1; 
                        sino
                            Esc(sec2, v) 
                        finsi
                        Esc(sec3,cant_v); 
                        avz(sec, v);
                    finMientras
                sino
                    Mientras (v <> " ") y (v <> ".") hacer
                        avz(sec, v);
                    finMientras
                finsi
            finMientras
            cant_O:= cant_O + 1;
            avz(sec,v);
        Mientras     
    finProceso
    cerrar(sec);
    cerrar(sec2);
    cerrar(sec3);
    PROM:= (cant_P/cant_O)
	ESCRIBIR("El promedio de palabras por oracion es: ", PROM);
finaccion