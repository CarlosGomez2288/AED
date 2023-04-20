Ejercicio 2.2.14
Dados el siguiente fichero con datos de un censo de la ciudad de Resistencia:

CENSO Ordenado por Radio, Manzana, Nro_Vivienda

Radio/Manzana/Nro_Vivienda/Condicion_Vivienda/Cantidad_Habitantes
Condición puede ser : Muy Buena, Buena o Mala.
Obtener los siguientes totales de personas que habitan en viviendas
cuya condición es muy buena: total en la ciudad y totales por Radio y Manzana).

Accion 2.2.14 Es
Ambiente
	Resistencia=registro
		Radio: N(5)
		Manzana: N(5)
		Nro_Vivienda: N(4)
		Condición_Vivienda={"muy buena","buena","mala"}
		Cantidad_Habitantes: N(10)
	FinRegistro
	CENSO: Archivo secuencial de Resistencia ordenado por Radio, Manzana, Nro_Vivienda
	reg: Resistencia
	totciudad,totradio,totmanzana: entero
	resgradio,resgmanzana: alfanumerico

	SubAccion Corte_Manzana Es
		Esc("Para Manzana",resgmanzana,"la cantidad de habitantes por manzana con condición (muy buena) son:",totmanzana)
		totradio:=totmanzana+totradio
		resgmanzana:=reg.Manzana
		totmanzana:=0
	FinSubAccion

	SubAccion Corte_Radio Es
		Corte_Manzana
		Esc("Para el radio",resgradio,"la cantidad de habitantes por radio con condición (muy buena) son:",totalradio)
		totciudad:=totciudad+totradio
		resgradio:=reg.Radio
		totradio:=0
	FinSubAccion

Proceso
	AbrirE/(CENSO);Leer(CENSO,reg)
	totciudad:=0
	totradio:=0
	totmanzana:=0
	resgradio:=reg.Radio
	resgmanzana:=reg.Manzana

	Mientras NFDA(CENSO) Hacer
		Si resgradio <> reg.Radio Entonces
			Corte_Radio
		Sino
			Si resgmanzana <> reg.Manzana Entonces
				Corte_Manzana
			FinSi
		FinSi
		Si reg.Condición = "Buena" Entonces
			totmanzana:=totmanzana+reg.Cantidad_Habitantes
		FinSi
		Leer(CENSO,reg)
	FinMientras
	Corte_Radio
	Esc("El total de habitantes que viven en Resistncia con la condición de (muy buena) son:",totciudad)
	Cerrar(CENSO)
FinAccion
