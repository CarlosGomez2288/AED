accion 1.2.6 es
    ambiente
        uni,precio:Entero
        funcion descuento(uni, precio:Entero):Real
            si (uni <= 6) entonces
                descuento:= 0.0;
            sino
                si ( uni < 13) entonces
                    descuento:= precio* 0,04;
                sino
                    si(uni > 12) entonces
                    descuento:= precio* 0.10;
                finsi
            finsi
    proceso
    Esc("Ingresar unidades y precio");
    leer(uni, precio)

    Esc("El total a pagar es: " precio + descuento(uni, precio));
finaccion

# CODIGO PSEINT
SubAlgoritmo return <- descuento ( uni, precio )
	Definir  return como real;
	si (uni <= 6) entonces
		return:= 0.0;
	SiNo
		si ( uni < 13) entonces
			return:= precio* 0.04;
		sino
			si(uni > 12) entonces
				return:= precio* 0.10;
			FinSi
		FinSi
	finsi
FinSubAlgoritmo

Algoritmo sin_titulo
	Definir  uni, precio Como Entero;
	Escribir "Ingresar unidades y precio";
    leer uni, precio;
	
    Escribir "El total a pagar es: " precio + descuento(uni, precio);
FinAlgoritmo
