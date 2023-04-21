# Se desea calcular el costo de un telegrama, que se determina en función del número de palabras 
# (que vale V1 cada una), salvo que el promedio de letras por palabra supere las cinco letras, 
# caso en que cada palabra vale V2.
accion 2.1.17 es
    ambiente
        sec: secuencia de caracteres;
        v: caracter;
        cont_P, cont_L, V1, V2: entero;
        promedio: real;
    proceso
        arr(sec);
        avz(sec, v);
        cont_P:= 0;
        cont_L:= 0;

        Esc("Ingresar los valores de V1 y V2");
        leer(V1, V2);

        mientras (NDFS(sec)) hacer
            mientras (v = " ") hacer
                avz(sec, v);
            finMientras
            
            mientras (v <> " ") y (NDFS(sec)) hacer
                cont_L:= cont_L + 1;
                avz(sec, v);
            finMientras
            
            cont_P:= cont_P + 1;
        finMientras
        
        cerrar(sec);
        promedio:= cont_L / cont_P;
        
        si (promedio > 5) entonces
            Esc("El costo del telegrama es: ", cont_P * V2);
        sino
            Esc("El costo del telegrama es: ", cont_P * V1);
        finSi
    finProceso
finAccion