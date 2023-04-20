Accion 5.1.1 Es
	Funcion Facts(n: entero): entero
		Si n=0 entonces
			Facts:=1
		Sino
			Facts:=Facts(n-1)*n
		FinSi
	FinFuncion
FinFuncion