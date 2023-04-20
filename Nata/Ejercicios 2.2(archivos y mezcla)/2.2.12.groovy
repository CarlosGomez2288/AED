Ejercicio 2.2.12
Dada una secuencia con información de población de un PAIS:

POBLACION Ordenado por Provincia, Departamento, Ciudad, Barrio, ID_Casa

Provincia/Departamento/Ciudad/Barrio/ID_Casa/Cantidad_Habitantes
Generar una secuencia con información de los departamentos de esa provincia,
cuyo registro tenga el siguiente formato:

POBLACION_SALIDA

Provincia/Departamento/Cantidad_Habitantes


Acción 2.2.12 Es
Ambiente
	Subaccion Corte_Departamento Es
		sal.Provincia:=resgProvincia
		sal.Departamento:=resgDepartamento
		sal.Cantidad_Habitantes:=TotalDpto
		Grabar(POBLACION_SALIDA,sal)
		TotalDpto:=0
		resgDepartamento:=reg.Departamento
		resgProvincia:=reg.Provincia
	FinSubaccion

Proceso
	Abrir E/(Poblacion)
	Abrir S/(POBLACION_SALIDA)
	Leer(Poblacion,reg)
	TotalDpto:=0
	resgProvincia:=reg.Provincia
	resgDepartamento:=reg.Departamento
	Mientras NFDA(Poblacion) Hacer
		Si reg.Departamento <> resgDepartamento Entonces
			Corte_Departamento
		FinSi
		TotalDpto:=TotalDpto+reg.Cantidad_Habitantes
		Leer(Poblacion,reg)
	FinMientras
	Corte_Departamento
	Cerrar(Poblacion);Cerrar(POBLACION_SALIDA)
FinAccion



