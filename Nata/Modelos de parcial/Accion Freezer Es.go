Accion FRRZze Es(Prim1,Prim2,Prim3: puntero a NODO)
Ambiente
    gusto= registro de 
        codgusto:
        nombregusto:
        precio:
    finregistro

    pedido= registro de 
        codpedido:
        codgusto:
        nombrev:
        cantidad:
    finregistro

    salida= registro
        codgusto:
        cantidad:
    finregistro

    Nodo1= registro
        dato: gusto;
        prox: Puntero a Nodo1
    finregistro

    Nodo2= registro de 
        dato: pedido; 
        prox: puntero a nodo2;
    Finregistro

    Nodo3= registro
        dato: salida;
        ant, prox: puntero a nodo3;
    finregistro


Proceso
    Prim1:=Nill;
    Prim2:=Nill
    Mientras 
        Z:=Prim2
        Mientras (Z<>Nill) hacer
            Si Prim3=Nill entonces
                Nuevo(Q)
                *Q.CodGusto:=*Z.CodGusto
                *Q.Cantidad:=*Z.Cantidad
                Prim3:=Q
                ULT:=Q
                *Q.ant:=Nill
                *Q.prox:=Nill
            Sino   
                
        FinMientras

        Esc("Ingrese");Leer(Gusto)
        Mientras (P<>Nill) y (*P.CodGusto<>Gusto)hacer
            P:=*P.prox
        FinMientras
        Si P<>Nill entonces
            Esc("Se encontro el gusto")
        Sino
            Esc("No se encontro el gusto")
        FinSi
            


















accion ej parcial (prim1: puntero a nodo1, prim2: puntero a nodo2) es 
    gusto= registro de 
            codgusto:
            nombregusto:
            precio:
        finregistro
    pedido= registro de 
            codpedido:
            codgusto:
            nombrev:
            cantidad:
        finregistro
    salida= registro
            codgusto:
            cantidad:
        finregistro
        
    Nodo1= registro
        dato: gusto;
        prox: Puntero a Nodo1
        finregistro
    Nodo2= registro de 
        dato: pedido; 
        prox: puntero a nodo2;
        Finregistro
    Nodo3= registro
        dato: salida;
        ant, prox: puntero a nodo3;
        finregistro
        
    




Prim1 ==> Lista de Gusto
Prim2 ==> Lista de Pedido 
Prim3 ==> Lista de Salida



Proceso 
Esc("Seleccione Opcion: 1. Informe de Cantidad x Gusto / 2. Informe de Monto por Gusto");
Leer (Opc) 
Prim3:= nil; 
ult:= nil 
Si Opc = 1 entonces 
    t:= Prim2; 
    Mientras t <> nil hacer 
        si Prim3 = nil entonces 
            Nuevo (q); 
            *q.dato.codgusto:= *t.dato.codgusto;
            *q.dato.cantidad:= *t.dato.cantidad; 
            Prim3:= q;
            Ult:= q; 
            *q.ant:= nil; 
            *q.prox:= nil; 
        sino 
            r:= Prim3 
            Mientras r <> nil y *r.dato.codgusto <> *t.dato.codgusto hacer 
                r:= *r.prox;
            FinMientras
            Si *r.dato.codgusto = *t.dato.codgusto entonces 
                *r.dato.cantidad:= *r.dato.cantidad + *t.dato.cantidad;
            sino 
                Nuevo (q); 
                *q.dato.codgusto:= *t.dato.codgusto;
                *q.dato.cantidad:= *t.dato.cantidad; 
                // INSERTO EN ULTIMA POS // queda a criterio de cada uno!
                *q.prox:= nil;
                *q.ant:= ult; 
                *ult.prox:= q; 
                ult:= q;
            FinSi 
        FinSi
        t:= *t.prox; 
    FinMientras 
sino
    ESC("Ingrese Nombre del Gusto a procesar");
    Leer(Rpta); 
    p:= Prim1; 
    Mientras p<> nil y *p.dato.nombre <> Rpta hacer 
        p:= *p.prox; 
    FinMientras
    Si *p.dato.nombre = Rpta entonces 
        acum:= 0; 
        t:= Prim2 
        Mientras t <> nil hacer 
            Si *t.dato.codgusto = *p.dato.codgusto entonces	
                acum:= acum + *t.dato.cantidad;
            FinSi 
            t:= *t.prox;
        FinMientras
        total:= acum * *p.dato.precio; 
        ESC("Para el helado:", Rpta," se vendio: $", Total); 		
    sino 
        ESC("ERROR, el gusto ingresado no existe");
    FinSi 
FinSi

FinProceso