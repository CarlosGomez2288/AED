accion 1.2.2 es 
    ambiente
        a:Entero
        funcion return(b: Entero):Enter
            sum, dig:Entero;
            Mientras (b > 0) hacer
                dig:= b mod 10;
                sum:= sum + dig;
                b:= b div 10;
            FinMientras
            return:= sum;
        finFuncion
    proceso
        Escribir "ingresar valor entero";
	    leer a;
	
	    Escribir "La suma de sus digitos  ",a," es: ", return(a);
finaccion

# CODIGO PSEINT
SubAlgoritmo return <- suma (b)
	Definir  return, sum, dig Como Entero;
	sum := 0;
	Mientras (b > 0 ) Hacer
		dig:= b mod 10;
		sum:= sum + dig;
		b:=  trunc(b/10) ;
	FinMientras
	return <- sum;
FinSubAlgoritmo

Algoritmo sin_titulo
	definir a Como Entero;
	
	Escribir "ingresar valor entero";
	leer a;
	
	Escribir "La suma de sus digitos  ",a," es: ", suma(a);
FinAlgoritmo
