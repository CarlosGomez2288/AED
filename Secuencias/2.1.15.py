# Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres. 
# Supóngase que los puntos son siempre contiguos al último caracter de la palabra. 
# La secuencia finaliza con una marca.
accion 2.1.15 es
    ambiente
        sec:secuenciade caracteres;
        v:caracter;
        cant_P, cant_O:Entero;
        promedio:Real[2.2];
    proceso
        cant_O:= 0;
        cant_P:= 0;
        arr(sec);
        avz(sec, v);

        Mientras (v <> "*") hacer 
            #1 comienza la oración.
            Mientras (v <> ".") hacer 
                #2 controla los espacio.
                Mientras ( v = " ") hacer 
                    avz(sec, v);
                finMientras
                #3Comienzo de una palabra.
                Mientras ( v <> " ") y ( v <> ".") hacer 
                    avz(sec, v);
                finMientras
                cant_P:= cant_P + 1; 
                #Final de una palabra.
            finMientras
            cant_O:= cant_O + 1;
            #final de una oración.
            avz(sec, v);
        finMientras
        cerrar(sec);
        promedio:= cant_O/cant_P;
        Esc("La Promedio de Palabra por oraciones es: ", promedio);
    finProceso
finAccion