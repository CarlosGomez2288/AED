accion 2.2.2 es
    ambiente
        sec,sec1,sec2:secuencia de caracteres
        v:caracter
        numeros={"1","2","3","4","5","6","7","8","9"}
        cont1,cont2:Enteros
    proceso
        cont1:=0;cont2:=0;
        arr(sec), crear(sec1) crear(sec2); avz(sec,v);

        Mientras NFDS(sec) hacer
            si(v en numeros) entonces
                Esc(sec1,v);
                cont1:=cont1 + 1;
            sino
                Esc(sec2,v);
                cont2:=cont2 + 1,
            finsi
            avz(sec,v);
    finProceso
    cerrar(sec1);
    cerrar(sec2);
finaccion