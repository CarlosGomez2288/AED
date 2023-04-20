
accion 2.1.5 es
    ambiente
        sec,sec2:secuencias de Enteros
        v,c1,c2, copiar,i:Enteros
    proceso
        arr(sec);
        crear(sec2);
        avz(sec, v) ;
        
        Mientras NFDS(sec) hacer
            c1:=v; 
            avz(sec,v);
            c2:=v;
            
            para i:= c1 hasta c2 hacer  
                copiar:= i + 1; 
                si (copiar < c2) entonces 
                    Esc(sec2,copiar);
                finsi
            finpara
            avz(sec,v)
        finMientras
        cerrar(sec);
        cerrar(sec2);
finaccion