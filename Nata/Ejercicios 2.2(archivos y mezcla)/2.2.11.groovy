Ejercicio 2.2.11
Se dispone de un archivo con datos de los alumnos de la U.T.N.
con la siguiente información para cada alumno:

PRODUCTOS Ordenado por Sexo, Carrera, Nro_Legajo

Sexo/Carrera/Nro_Legajo/Fecha_Ingreso/Total_Materias_Aprobadas

Se desea un listado con el siguiente detalle por sexo, carrera y total general

1.Total de alumnos que ingresaron en el año 2009 con más de
 20 materias aprobadas.

2.Total de alumnos que ingresaron en el año 2009 con menos de
 20 materias aprobadas

Accion 2.2.12 Es
Ambiente
	Alumno=registro
		Sexo
		Carrera
		Nro_Legajo
		Fecha_Ingreso=registro
			AA: N(4)
			MM: 1..12
			DD: 1..31
		FinRegistro
		Total_Materias_Aprobadas: N(2)
	FinRegistro
	PRODUCTOS: archivo secuencial Ordenado por Sexo, Carrera, Nro_Legajo
	reg: Alumno
	TotalAmas,TotalAmenos,contSexo,contCarrera,TotalAlum: entero

	Subaccion Corte_Sexo Es
		Corte_Carrera
		Esc("Para el Sexo",resgSexo,"tenemos una cantidad de aprobados de:",contalumnos)
		TotalAlum: TotalAlum + contSexo
		contSexo:=0
		resgSexo:=reg.Sexo
	FinSubacción

	Subaccion Corte_Carrera Es
		CorteNro_Legajo
		Esc("Para la Carrera",resgCarrera,"tenemos la cantidad de alumnos de:",contCarrera)
		contSexo:=contSexo+contCarrera
		contCarrera:=0
		resgCarrera:=reg.Carrera
	FinSubacción 

Proceso
	Abrir E/(Productos)
	Leer(Productos,reg)
	TotalAmas:=0;TotalAmenos:=0;contSexo:=0;contCarrera:=0;TotalAlum:=0
	resgSexo:=reg.Sexo
	resgCarrera:=reg.Carrera
	Mientras NFDA(Productos) Hacer
		Si reg.Sexo <> resgSexo Entonces
			Corte_Sexo
		Sino
			Si reg.Carrera <> resgCarrera Entonces
				Corte_Carrera
			FinSi
			contCarrera:=contCarrera+1
		FinSi
		contSexo:=contSexo+1

		Si reg.Total_Materias_Aprobadas>"20" y reg.Fecha_Ingreso ="2009"
			TotalAmas:=TotalAlum+TotalAmas
		Sino
			Si reg.Total_Materias_Aprobadas<"20" y reg.Fecha_Ingreso ="2009"
				TotalAmenos:=TotalAmenos+TotalAlum
			FinSi
		FinSi
		Leer(Productos,reg)
	FinMientras
	Corte_Sexo
	Esc("La cantidad de alumnos que aprobaron más de 20 materias son:",TotalAmas)
	Esc("La cantidad de alumnos que aprobaron menos de 20 materias son:",TotalAmenos)
	Cerrar(Productos)
FinAccion	






















Ejercicio 2.2.12
Dada una secuencia con información de población de un PAIS:

POBLACION Ordenado por Provincia, Departamento, Ciudad, Barrio, ID_Casa

Provincia/Departamento/Ciudad/Barrio/ID_Casa/Cantidad_Habitantes
Generar una secuencia con información de los departamentos de esa provincia,
cuyo registro tenga el siguiente formato:

POBLACION_SALIDA

Provincia/Departamento/Cantidad_Habitantes/

Accion 2.2.12 Es
	Poblaación=registro
		Provincia: AN(15)
		Departamento: AN(30)
		Ciudad: AN(30)
		Barrio: AN(30)
		ID_Casa: 


Proceso
	Abrir E/()
