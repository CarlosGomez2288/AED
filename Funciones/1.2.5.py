accion  1.2.6 es
    ambiente
        caracter:Alfanumerico;
         digito = {"1","2","3","4","5","6","7","8","9"}

         funcion digito (cara:Alfanumerico):boleano
            si No(cara en digito) en
                digito:= falso;
            sino
                digito:= verdadero
            finsi
         funcion
    proceso
        Esc("ingresa un caracter");
        leer (caracter)

        si(digito(caracter)) estonces
            Esc("El caracter ingreado es un digito");
        sino
            Esc("El caracter ingreado no es un digito");
        finsi
finaccion


# CODIGO PSEINT
SubAlgoritmo return <- digit ( cara )
	Dimension digito[9];
	definir num, i Como Entero;
	definir return Como Logico
	segun cara hacer
		"1": num:= 1;
		"2": num:= 2;
		"3": num:= 3;
		"4": num:= 4;
		"5": num:= 5;
		"6": num:= 6;
		"7": num:= 7;
		"8": num:= 8;
		"9": num:= 9;
	FinSegun
	para i<-1 hasta 9 Hacer
		digito[i]<- i;
	FinPara
	para i<- 1 hasta 9 Hacer
		si (digito[i]= num) Entonces
			return:= Verdadero;
		SiNo
			return:= Falso;
		FinSi
	FinPara
	
FinSubAlgoritmo

Algoritmo sin_titulo
	definir caract Como Caracter;
	Escribir "Ingresar un caracter";
	Leer caract;
	si(digit(caract)) Entonces
		Escribir "El caracter ingreado es un digito";
	sino
		Escribir "El caracter ingreado no es un digito";
	finsi
	
FinAlgoritmo