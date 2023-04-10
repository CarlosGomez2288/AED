acccion 1.1.23 es
    ambinte
        reglon, cantidad,i:Entero
        valor, total, subtotal:Real(2)
    proceso
        total:= 0;
        Esc("Ingresar la cantidad de reglones");
        leer(reglon);

        para i:=1 hasta reglon hacer 
            Esc("Ingresar valor");
            leer(valor)

            si (valor <= 0) entonces
                Esc("ERROR el valor unitario es menor a cero"); 
            sino
                Esc("Ingresar cantidad");
                leer(cantidad)
                subtotal:= cantidad* valor;

                Esc("El subtotal del reglon: ",i, " Es: $: ",subtotal);
                total:=total + subtotal;
            finsi
        finpara
            Esc("El Total de la compra es: ",total );
finaccion

# CODIGO PSEINT
Algoritmo sin_titulo
	definir reglon, cantidad,i como Entero;
	definir valorr, total, subtotal como entero;
	
	total:= 0;
    Escribir"Ingresar la cantidad de reglones";
    leer reglon;
	
	Para i<- 1 hasta reglon Hacer
		Escribir"Ingresar valor";
        leer valorr;
		
        si (valorr <= 0) entonces
            Escribir"ERROR";
        sino
            Escribir "Ingresar cantidad";
            leer cantidad;
            subtotal:= cantidad* valorr;
			
            Escribir "El subtotal del reglon: ", i, " Es: $: ", subtotal;
            total:=total + subtotal;
        finsi
	FinPara
	Escribir "El Total de la compra es: ",total;
FinAlgoritmo
