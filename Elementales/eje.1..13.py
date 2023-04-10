accion 1.1..13 es
    ambiente
        num, bit100, bit10, bit1: Entero
    proceso

        Esc("Ingresar un monto entero mayor a 100 y menor a 1000")
        leer(num)

        si (num> 100 ) y (num < 1000) entonces

            bit100 := num div 100
            num:= num mod 100

            bit10 := num div 10
            num:= num mod 10

            
            num:= num

            Esc("Billetes de 100: " , bit100)
            Esc("Billetes de 10: " , bit10)
            Esc("Billetes de 1: " , bit1)
            
        sino
            Esc("supero el rango")
        finsi
finaccion

# CODIGO DE PSEINT
Algoritmo sin_titulo
	Definir num Como Entero;
	Definir  bit100, bit10, bit1 Como Real;
	definir op Como Caracter;
    
		op:= "n";
		
        Mientras (op = "n") Hacer
			Escribir ("Ingresar un monto entero mayor a 100 y menor a 1000");
			leer num;
			
			si (num> 100 ) y (num < 1000) entonces
				
				bit100 := trunc(num / 100);
				num:= num mod 100;
				
				bit10:= trunc(num / 10);
				num:= num mod 10;
				
				bit1:= num;
				
				Escribir "Billetes de 100: " , bit100;
				Escribir "Billetes de 10: " , bit10;
				Escribir "Billetes de 1: " , bit1;
			sino
				Escribir ("supero el rango");
			finsi
			
			Escribir "Deseas terminar el proceso";
			Leer  op;
			
		FinMientras
FinAlgoritmo
