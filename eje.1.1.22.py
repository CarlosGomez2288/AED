accion 1.1.22 es
    ambiente
        num, i:Entero;
	     primo:Logico;
	    primo:= Verdadero;
    proceso
	    num:= 7;
        
        para i<- 2 Hasta raiz(num) Hacer
            si num mod i = 0 Entonces
                primo:= Falso;
            FinSi
        FinPara
        si primo Entonces
            Escribir "es primo";
        SiNo
            Escribir "no es primo";
        FinSi
finaccion
# CODIG PSEINT
Algoritmo sin_titulo
	definir num, i Como Entero;
	definir primo Como Logico;
	primo:= Verdadero;
	num:= 7;
	para i<- 2 Hasta raiz(num) Hacer
		si num mod i = 0 Entonces
			primo:= Falso;
		FinSi
	FinPara
	si primo Entonces
		Escribir "es primo";
	SiNo
		Escribir "no es primo";
	FinSi
FinAlgoritmo