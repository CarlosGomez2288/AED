accion 1.1.18 es
    ambiente
        F, G, resto, resu, cont:Entero

    proceso

    Esc("Ingresar dos valores enteros");
    leer (F, G);
    resu:= F;
    cont:= 0;

    Repetir
        resu:= resu -G;
        resto:= resu
        cont:=cont + 1;
    hasta que (resu < G)

    Esc("El resultado del cociente es: ", resu);
    Esc("El resto es: ", resto)
finaccion

# CODIGO DE PSINT
Algoritmo sin_titulo
	definir F, G, resu, resto ,cont Como Entero;
	Escribir "Ingresar dos valores enteros";
	leer F, G;
	cont:= 0;
	resu:= F;
	
	Repetir
		resu:= resu - G;
		resto:= resu;
		cont:= cont + 1;
	Hasta Que resu < G;
	
	Escribir "Resultado: ", cont;
	Escribir "Resto: ",resto;
FinAlgoritmo