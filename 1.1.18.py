accion 1.1.28 es
    ambiente
        dig1, dig2, dig3, sum, i:Entero
    proceso
        para i:= 100 hasta 1000 hacer
            dig1:= i dv 100;
            dig2:= (i div 10) mod 10;
            dig3:= i mod 10;

            sum:= dig1^3 + dig2^3 + dig3^3;
            si ( sum = i) Entonces
                Escribir i;
            FinSi
finaccion
# codigo PSINT
Algoritmo sin_titulo
	Definir  dig1, dig2,dig3, i, sum Como Entero;
	
	para i <- 100 hasta 1000  Hacer
		dig1:= trunc(i / 100);
		dig2:= trunc(i / 10) mod 10;
		dig3:= i mod 10;
		sum:= dig1^3 + dig2^3 + dig3^3;
		si ( sum = i) Entonces
			Escribir i;
		FinSi
		
	FinPara
	
FinAlgoritmo