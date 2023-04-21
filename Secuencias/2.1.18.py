# Escribir un algoritmo que produzca una secuencia de salida que contenga una oración formada 
# por  las palabras en posición par de cada oración de una secuencia texto de entrada, 
# que además comienzan con la letra 'M'.
accion 2.1.18 es
    ambiente
        sec,sec2:secuencia de caracteres;
        v: caracter;
        cont_P:Entero;
    proceso
        arr(sec);
        avz(sec,v);
        
        Mientras NFDS(sec) hacer
            cont_P:= 0;
            es_par:= false;
            #Comienzo de una oracion
            Mientras (v <> ".") hacer
                #Controlo los espacio vacio
                Mientras ( v = " ") hacer
                    avz(sec,v);
                finMientras

                #comienzo de una palabra
                cont_P:= cont_P + 1;
                si (cont_P mod 2 = 0) entonces
                    si (v = "M") entonces
                        es_par := Verdadero;
                    finsi

                    #Agrego la palabra a la secuencia de salida
                    Mientras (v <> " ") y (v <> ".") hacer
                        si (es_par) entonces
                            Esc(sec2, v);
                        finsi
                        avz(sec, v);
                    finMientra
                sino
                    Mientras(v <> " ") y ( v <> ".") hacer
                            avz(sec,v);
                    finMientras
                finsi  
            finMientras
            avz(sec,v);
        finMientras
        cerrar(sec);
        cerrar(sec2);
    finProceso
finAccion
