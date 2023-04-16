Escriba un algoritmo para resolver el siguiente problema: Una empresa de transportes desea 
conocer el sueldo de sus 100 choferes. Éstos se calculan teniendo en cuenta la categoría (1 o 2) 
y la asistencia (perfecta: si o no). El sueldo se obtiene sumando el sueldo básico, más el 2% de 
antigüedad por cada año trabajado y $200 de premio por asistencia. El sueldo básico es de $700 para 
choferes de categoría 1 y de $500 para los de categoría 2.

accion 1.2 es
    ambiente
        cat,anio:entero;
        asis:Alfanumerico;

        procedimiento sueldo(asis:alfanumerico, cat,i,anio:Entero):Alfanumerico
            paga:=Real[2.2]
            segun(cat) hacer
                1:
                    paga:= 700 + (700*anio*0,02);
                2:
                    paga:= 500 + (500*anio*0,02);
                otros:
                    Esc("!!!Error esa categoria no existe!!!"),
            FinSi

            si (asi = "si")
                paga:= paga + 200;
            finsi
            
            Esc("El sueldo pagar")
            Esc("Para el Chofer ", i ," de Categoria " cat, "Es $", paga);
        finProcedimiento
    proceso
        para i= 1 hasta 100 hacer
            Esc("Sueldo deo Chofer: ", i);
            Esc("Ingresar la categoria que pertenece");
            leer(cat)
            Esc("¿Tiene asistencia perfecta ? Responde con si o no ")
            leer(asis)
            Esc("Ingrear el año de antiguedad en la empresa")
            leer(anio);

            sueldo(asis,cat, i, anio);
        finpara
finaccion

# <-----CODIGO DE PSEINT----->
Funcion  Sueldo(asis, cat, i, anio)
	Definir  paga como real;
	segun (cat) Hacer
		1: 
			paga:= 700 + (700*anio* 0.02);
		2:
			paga:= 500 + (500*anio* 0.02);
		De Otro Modo:
			Escribir ("!!!Error esa categoria no existe!!!");
	FinSegun
	si (asis = "si") Entonces
		paga:= paga + 200;
	FinSi
	Escribir ("El sueldo pagar");
	Escribir "Para el Chofer ", i ," de Categoria " cat, "Es $", paga;
Fin Funcion

Algoritmo sin_titulo
	Definir  i Como Entero;
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		Escribir "Sueldo deo Chofer: ", i;
		Escribir "Ingresar la categoria que pertenece";
		leer cat
		Escribir "¿Tiene asistencia perfecta ? Responde con si o no ";
		leer asis
		Escribir "Ingrear el año de antiguedad en la empresa";
		leer anio;
		
		sueldo(asis,cat, i, anio);
	Fin Para
FinAlgoritmo
