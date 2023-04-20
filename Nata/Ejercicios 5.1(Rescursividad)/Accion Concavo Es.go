Accion Concavo Es
	Funcion Concavo(A:arreglo de[1..20]de entero,pos: entero):entero Es
		Si A[pos]>A[pos+1] entonces
			Concavo:=pos
		Sino
			Concavo:=Concavo(A,pos+1)
		FinSi
	FinFuncion
FinAccion