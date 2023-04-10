accion 1.10.17 es
    ambiente
        A,B resu, i: Entero
        op:Alfanumerico
    proceso

        Repetir
            Escribir "ingrear dos numeros enteros";
            Leer (A,B);
            
            resu:= 0;
            
            Para i<-1 Hasta B Con Paso 1 Hacer
                resu:= resu + A;
            FinPara
            
            Escribir "Resultado: ", resu;
            
            Escribir ("DESEAS CONTINUAR n/y");
            Leer  op;
        hasta que (op = "n");
finaccion


# codigo psint
Algoritmo sin_titulo
	definir A, B, resu, i Como Entero;
	definir op Como Caracter;
	
	Repetir
		Escribir "ingrear dos numeros enteros";
		Leer A,B;
		
		resu:= 0;
		
		Para i<-1 Hasta B Con Paso 1 Hacer
			resu:= resu + A;
		FinPara
		
		Escribir "Resultado: ", resu;
		
		Escribir "DESEAS CONTINUAR n/y";
		Leer  op;
	Hasta Que op = "n" 
	
FinAlgoritmo
