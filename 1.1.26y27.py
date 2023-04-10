accion 1.1.2
    ambiente
        a, b, c,x,y: Entero
    proceso
        
        para x:20 hasta -20 con paso -2 hacer
            y:=a*x**2 + b*x + c;
            Escribir ("Coordenadas: (",x,",",yy,")";)
        finpara
finaccion
# codigo de pseint
Algoritmo sin_titulo
	Definir  a, b, c, x, yy Como Entero;
	a:= 1;
	c:= 4;
	b:= 5;
	para x <- 20 hasta -20 Con Paso -2 Hacer
		Yy:= a*x^2 + b*x+ c;
		Escribir "Coordenadas: (",x,",",yy,")";
	FinPara
	
FinAlgoritmo

accion 1.1.27
    ambiente
        a, b, c,x,y: Entero
    proceso
        repetir
            Esc("Ingresar Valores para ax2 + bx+ c.")
            leer a, b, c
                para x:20 hasta -20 con paso -2 hacer
                    y:=a*x**2 + b*x + c;
                    Escribir ("Coordenadas: (",x,",",yy,")";)
                finpara
            Esc("Se termina ingresando 9999")
            leer(a)
        hasta que (a = 99999)
finaccion