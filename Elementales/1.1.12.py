accion 1.1.12 es
    ambiente
        num:Entero(4)
        unidades, decenas, centenas, suma:Entero(2)
    proceso

        Esc("Ingresar un  numero entero")
        leer ( num)

        unidades:= num mod 10
        decenas:= (num / 10) mod 10
        centenas:= (num / 100) mod 10

        Esc("unidades: ", unidades)
        Esc("decenas: ", decenas)
        Esc("centenas: ", centenas)
        
        suma:= unidades + decenas+ centenas;

        si(suma mod 3 == 0) entonces
            Esc("Si es multiplo de 3")
        sino
            Esc("No es multiplo de 3")
        finsi
finaccion
 
#  /*CODIGO DE PSEINT*/

Algoritmo DescomposicionYMultiploDe3
	// Declarar las variables
	Definir num, unidades, decenas, centenas, suma Como Entero;
	
	// Pedir al usuario un número entero
	Escribir("Ingrese un número entero: ");
	Leer num;
	
	// Descomponer el número en unidades, decenas y centenas
	unidades := num % 10;
	decenas := trunc(num / 10) mod 10;
	centenas := trunc(num / 100) mod 10;
	
	// Mostrar las unidades, decenas y centenas
	Escribir"Unidades: ", unidades;
	Escribir"Decenas: ", decenas;
	Escribir"Centenas: ", centenas;
	
	// Verificar si el número es múltiplo de 3
	suma := unidades + decenas + centenas;
	Si suma mod 3 == 0 Entonces
		Escribir("El número es múltiplo de 3");
	Sino
		Escribir("El número no es múltiplo de 3");
	FinSi
	
FinAlgoritmo