Accion Digito Es
    Funcion DigitoP(n,d: entero):booleano entonces
		Si n = d entonces
			DigitoP:=Falso
		Sino
			Si n < 10 entonces
				DigitoP:=Verdadero
			Sino
				DigitoP:=DigitoP(n DIV 10,d)
			FinSi
		FinSi
	FinFuncion
FinAccion