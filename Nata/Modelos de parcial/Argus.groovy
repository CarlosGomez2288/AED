Accion ARGUS Es
AMBIENTE
	MEDICAMENTOS,SALIDA: secuencia de caracter
	COMPRAS: secuencia de entero
	v1: caracter
	v2: entero
	valor,Porcentaje,ContIgual,Cont,s1,s2,Lote: entero

 //Paracetamol#Dicofenac#PLin
 //150 10000 120 30000
Proceso
	ARR(MEDICAMENTOS);AVZ(MEDICAMENTOS,v1) 
	ARR(COMPRAS);AVZ(COMPRAS,v2)
	CREAR(SALIDA)
	ContIgual:=0
	Cont:=0
	Mientras NFDS(MEDICAMENTOS) y NFDS(COMPRAS) Hacer
		s1:=v2
		AVZ(COMPRAS,v2)
		s2:=v2
		Lote:=s1*s2
		Esc("Ingrese un valor del precio total de lotes")
		Leer(valor)
		AVZ(COMPRAS,v2)
		Si Lote > valor Entonces
			Mientras v1 <> "#" Hacer
				Esc(v1)
				AVZ(MEDICAMENTOS,v1)
			FinMientras
		Sino
			Si Lote < valor Entonces
				Mientras v1 <> "#" Hacer
					Esc(SALIDA,v1)
					AVZ(MEDICAMENTOS,v1)
				FinMientras
				Esc(SALIDA,"L")
				Esc(SALIDA,"O")
				Esc(SALIDA,"W")
			Sino
				Mientras v <> "#" Hacer
					AVZ(MEDICAMENTOS,v1)
				FinMientras
				ContIgual:=ContIgual+1
			FinSi
		FinSi
		Cont:=Cont+1
		AVZ(MEDICAMENTOS,v1)
		AVZ(COMPRAS,v2)
	FinMientras
	Porcentaje:=(ContIgual*100)/Cont
	Esc("El promedio de MEDICAMENTOS cuyo precio total de lotes son iguales al ingresado, son:",Porcentaje)
	CERRAR(MEDICAMENTOS)
	CERRAR(SALIDA)
	CERRAR(COMPRAS)
FinAccion







