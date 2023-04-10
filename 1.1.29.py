accion 1.1.22 es
    ambiente
        num, i:Entero;
	     primo:Logico;
	    primo:= Verdadero;
    proceso
	    Esc("ingresar un numero");
        leer(num)
        
        para i<- 2  Hasta num  Hacer
                primo:= Verdadero;
           
           para j:= 2 hasta raz(mum) hacer
                si num mod i = 0 hacer
                    primo:= falso;
                finsi
           finpara

            si primo Entonces
                Escribir i;
            FinSi
        FinPara
    
finaccion