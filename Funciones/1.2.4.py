accion 1.2.4 es
    ambiente
        num:Entero

        funcion clave(num:Entero):Entero
            dig1, dig2,dig3:Entero
            si (num < 0 ) entonces
                clave:= -1;
            sino
                dig1:= num div 100;
                dig2:= (num div 10) mod 10;
                dig3:= num mod 10;

                clave:= (dig1 + dig2 + dig3) mod 7;
            finsi
        finFuncion
    proceso
        Repetir
            Esc("ingresar un numero"):
            leer num;

            si(clave(num) = -1) entonces
                Esc("Negativo")
            sino
                Esc("La clave es: ", clave(num));
            finsis
            Esc("DESEAR Terminar s/n")
        hasta que (op = "s");
finaccion
# CODIGO PSEINT
SubAlgoritmo return <- clave (num)
	Definir  return Como Entero;
		Definir  dig1, dig2,dig3 como Entero;
	si (num < 0 ) entonces
		return:= -1;
	sino
		dig1:= trunc(num / 100);
		dig2:= trunc(num / 10) mod 10;
		dig3:= num mod 10;
		
		return:= (dig1 + dig2 + dig3) mod 7;
	finsi
FinSubAlgoritmo

Algoritmo sin_titulo
	definir num, a Como Entero;

	Escribir "ingresar un numero";s
		leer num;
		
		si(clave(num)= -1) entonces
			Escribir "Negativo";
		sino
			Escribir "La clave es: ", clave(num);
		finsi 
FinAlgoritmo