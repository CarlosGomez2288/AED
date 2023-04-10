
accion 1.2.10 es
    ambiente
        procedimiento Menu():Entero
            num1, num2, op:Entero

            repetir
                Esc("**************************************")
                Esc("*1-suma*2-Resta*3-Multi*4-Div*5-Salir*")
                Esc("**************************************")
                leer(op);

                si ( op <> 5) entonces
                    Esc("Ingresa dos valores para la operacion")
                    leer(num1, num2)
                finsi
                
                segun (op) hacer
                    1:Esc("La suma es: ", operacion(num1, num2));
                    2:Esc("La Resta es: ", operacion(num1, num2));
                    3:Esc("La multiplicion es: ", operacion(num1, num2));
                    4:Esc("La divicion es: ", operacion(num1, num2));
                finsegun
            hasta que (op <> 5)
        finProcedimiento

        funcion operacion(num1, num2, op:Entero):Entero
            segun (op ) hacer
                1:operacion:= num1+num2;
                2:operacion:= num1-num2;
                3:operacion:= num1*num2;
                4:operacion:= num1 div num2;
            finsegun
        finfuncion
    proceso
        Menu();
finaccion

# CODIGO PSEINT
Funcion return <- operacion ( num1,num2, op )
	segun (op ) hacer
		1:return:= num1+num2;
		2:return := num1-num2;
		3:return:= num1*num2;
		4:return:= num1 / num2;
	finsegun
Fin Funcion

Funcion  Menu ()
definir num1, num2, op como Entero
	
	repetir
		Escribir"**************************************";
		Escribir"*1-suma*2-Resta*3-Multi*4-Div*5-Salir*";
		Escribir"**************************************";
		leer op;
		
		si(op <> 5) Entonces
			Escribir"Ingresa dos valores para la operacion";
			leer num1, num2
		FinSi
		
		segun (op) hacer
			1:Escribir"La suma es: ", operacion(num1, num2,op);
			2:Escribir"La Resta es: ", operacion(num1, num2,op);
			3:Escribir"La multiplicion es: ", operacion(num1, num2,op);
			4:Escribir"La divicion es: ", operacion(num1, num2,op);
		finsegun
	hasta que (op = 5)
Fin Funcion

Algoritmo sin_titulo
	Menu();
FinAlgoritmo