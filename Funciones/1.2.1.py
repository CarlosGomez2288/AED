accion 1.2.1 es
    ambiente
        num: Entero
        funcion cuadrado (a:Entero):Entero es
            cuadrado:= a**2;
        finFuncion
    proceso
        Esc("Ingresar un valor entero");
        leer (a);

        Esc("Es cuadrado de ", a, "Es: ", cuadrado);
finaccion
# codigo PSEINT
SubAlgoritmo cuadrado <- c (b)
	Definir  cuadrado Como Entero;
	cuadrado <- b ^2;
FinSubAlgoritmo

Algoritmo sin_titulo
	definir a ,cuadrado Como Entero;
	
	Escribir "ingresar valor entero";
	leer a;
	
	Escribir "El cuadrado de ",a," es: ", c(a);
FinAlgoritmo
