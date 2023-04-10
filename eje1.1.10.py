accion 1.1.10 es
    ambiente
        A, B:Entero(2)
        S: Alfanumerico(2)
    proceso

        repetir
            Esc("c")
            leer(A, B)

            si (B mod A == 0) entonces
                Esc ("El Valor de A es divisor de B");
            sino
                Esc ("El Valor de A es divisor de B");
            finsi

            Esc("¿Deseas continuar n/y?");
            leer(S)    
        hasta que (S = n)    
finAccion

/*CODIGO DE PSIENT*/
Algoritmo sdea
	definir A, B Como Entero;
	definir S Como Caracter;
	
	Repetir
		Escribir "ingresar dos numeros entero"
        Leer A,B
		
		si (B mod A = 0) Entonces
			Escribir ("El Valor de A es divisor de B");
		SiNo
			si (A mod B = 0) Entonces
				Escribir ("El Valor de B es divisor de A");
			FinSi
		FinSi
        
		Escribir ("¿Deseas continuar n/y?");
		leer S 
	Hasta Que S = n
FinAlgoritmo