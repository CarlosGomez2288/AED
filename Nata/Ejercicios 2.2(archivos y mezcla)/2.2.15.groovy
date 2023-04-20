Ejercicio 2.2.15
El organismo del cual dependen las escuelas de un distrito lleva
un archivo con los registros para todos los alumnos de nivel secundario
de ese distrito:

ALUMNOS Ordenado por Escuela, Año, División

Escuela/Año/División/Nombre/Cant_Inasistencias
Se introduce como dato el número de distrito y la cantidad de días de clase
dictados en el año. El archivo está ordenado por número de escuela,
año y división.
Los alumnos que superan el 20% de las inasistencias están en situación
de LIBRES, de lo contrario son REGULARES.

Se desea conocer:
Para cada división:
- Cantidad de alumnos
Para cada año:
- Cantidad total de alumnos libres
- Cantidad de alumnos regulares
- Cantidad total de alumnos
Todas las escuelas:
- Cantidad total de alumnos
- Porcentaje de alumnos libres. - Promedio de inasistencias por alumnos.

Accion 2.2.15 Es
Ambiente
	Datos=registro
		Escuela: AN(30)
		Año: AN(10)
		División: AN(1)
		Nombre: AN(50)
		Cant_Inasistencias: N(2)
	FinRegistro

	SubAccion Corte_División Es
		Esc("Para la División",resgdivisión,"hay una cantidad de alumnos de:",SubtAlumD)
		SubtAlumA:=SubAlumA+SubtAlumD+CantAlumL+CantAlumR
		resgdivisión:=reg.División
		SubtAlumD:=0
	FinSubAccion

	SubAccion Corte_Año Es
		Corte_División
		Esc("Para el Año",resgaño,"hay una cantidad de alumnos de:",SubAlumA)
		SubtAlumE:=SubtAlumE+SubtAlumA
		resgaño:=reg.año
		SubtAlumA:=0
	FinSubAccion

	SubAccion Corte_Escuela Es
		Corte_Año
		Esc("Para el Año",resescuela,"hay una cantidad de alumnos de:",SubAlumE)
		SubtAlumE:=SubtAlumE+SubtAlumA
		resgaño:=reg.escuela
		SubtAlumA:=0
	FinSubAccion

Proceso
	AbrirE/(ALUMNOS)
	Leer(ALUMNOS,reg)
	TotAlum:=0
	CantAlumR:=0
	CantAlumL:=0
	SubtAlumD:=0
	SubtAlumA:=0
	SubtAlumE:=0

	resgdivisión:=reg.División
	resgaño:=reg.Año
	resgescuela:=reg.Escuela
	Esc("Ingrese la cantidad de días de asistencia del año")

	Mientras NFDA(ALUMNOS) Hacer
		Si resgescuela <> reg.Escuela Entonces
			Corte_Escuela
		Sino
			Si resgaño <> reg.Año Entonces
				Corte_Año
			Sino
				Si resgdivisión <> reg.División Entonces
					Corte_División
				FinSi
			FinSi
		FinSi
		TotInasistencias:=TotInasistencias + reg.Cant_Inasistencias
		
		Si TotInasistencias >    
	FinMientras
	Corte_Escuela

	Cerrar(Alumnos)
FinAccion

