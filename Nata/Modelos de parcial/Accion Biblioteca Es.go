Accion Biblioteca Es
Ambiente
	socios = registro
		dni : n (8)
		apynom: an (30)
		edad: 18...80
		ciudad: an (30)
		deudor : {"SI","NO"}
		cant: n (6)
	fin registro
	arch: archivo de socios indexado por dni
	reg: socios

	info2 = registro
		id: 1..100
		titulo: an (30)
		genero: n (2)
		disponible: booleano
	fin registro
	libros: archivo de info2 indexado por id
	reglibros: info2

	info3 = registro
		idpres: n (8)
		dni. n (8)
		idlibro: n (8)
		fecha = registro
			aa: n (4)
			mm: 1..12
			dd:1..31
		fin registro
		fechadev: fecha
		dev : {"SI","NO"}
	fin registro
	prestamos:archivo de info3 indexado por idpres
	regpres: info3

	dni,edad : entero
	apnom,ciudad: alfanumerico

	contprest, alta : entero

	arr_libros : arreglo [1..100] de alfanumericos
	i: entero
	proceso
		contprest := 0 ; alta := 0
		abrir e/s (arch) ; abrir s/(prestamos) ; abrir e/s(libros)
		pres:= 1
		esc ("Cargar un nuevo prestamo? SI/NO") ; leer (rta)
		mientras rta ="SI" entonces

			esc ("Ingrese dni del usuario al cual se le presta") ; leer (dni)

			esc ("Ingrese titulo del libro") ; leer (titulo) // busqueda con centinela
			i := 1
			mientras i < 101 y (arr_libros [i] <> titulo) hacer // busqueda
				i := i + 1
			fin mientras

			si arr_libros [i] = titulo entonces // busqueda con exito de titulo 
				reglibros.id := i  // busco con id , busqueda indexada del id
				si existe entonces
					si reglibros.disponible = falso entonces
						esc ("ERROR: libro no disponible para prestar")
					sino
						reg.dni := dni
						leer (arch,reg)  // busqueda indexada del dni

						si no existe entonces  // no existe el usuario, hay que darlo de alta 
							esc ("No existe socio, lo daremos de alta")
							reg.dni := dni
							esc ("Ingrese apellido y nombre") ; leer (apnom)
							reg.apynom :apnom
							esc ("Ingresar edad: ") ; leer (edad)
							reg.edad := edad
							esc ("Ingresar ciudad: ") ; leer (ciudad)
							reg.ciudad := ciudad
							reg.deudor := "NO"
							reg.cant := 0
							alta := alta + 1
							esc ("PROCESO DE ALTA FINALIZADO")
							GRABAR (arch,reg) // el alta 
						fin si

						reglibros.disponible = falso
						reg.cant := reg.cant + 1
						regpres.id :=  pres; // mantengo el id
						pres:= pres + 1; 
						regpres.dni := reg.dni
						regpres.idlibro := reglibros.id
						regpres.fecha := fecha_sistema ()
						si reg.cant > 10 y reg.deudor = "NO" entonces
							regpres.fechadev := regpres.fecha + 20
						sino
							regpres.fechadev := regpres.fecha + 14
						fin si
						
						regpres.dev := "NO"
						contprest := contprest + 1
						
						
						GRABAR (prestamos,regpres)
						REGRABAR (libros,reglibros)  // por el disponible
						REGRABAR (arch,reg) // por la cantidad de prestamos
					fin si
				
				fin si
			sino
				esc ("Error: no existe el titulo del libro que usted quiere alquilar")
			fin si

			esc ("Desea procesar otro prestamo?") ; leer (rta)
		fin mientras

		esc ("Total de altas:" , altas)
		esc ("Total de prestamos: ", cantprest)
		cerrar (arch) ; cerrar (prestamos) ; cerrar (libros)
	fin proceso
fin accion

----------------------------------------------------------------------------------------------
Accion Biblioteca2 Es
Ambiente
	ejem = registro
		Clave=registro
			IDEjem: N(8)
			IDLibro: N(30)
			Sucursal: 1..5
			Digital:{"SI","NO"}
			Disponible: booleano
		FinRegistro
	FinRegistro
	reg: ejem
	EJEMPLARES: archivo secuencial de ejem ordenado por Clave

	Tipo=registro
		Disponible: N(10)
		NoDisponible: N(10)
	FinRegistro

	A: arreglo de [1..3,1..6] de Tipo
	i,j,Sucu,x,totdig,totfis: entero
	dig: alfanumerico
	

Proceso
	Abrir E/(EJEMPLARES);Leer(EJEMPLARES,reg)

	Para i:=1 hasta 3 hacer
		Para j:=1 hasta 6 hacer
			A[i,j].Disponible:=0
			A[i,j].NoDisponible:=0
		FinPara
	FinPara

	Mientras NFDA(EJEMPLARES) hacer
		Si reg.Digital = "SI" entonces
			i:=1
		Sino
			i:=2
		FinSi

		j:=reg.Sucursal

		Si reg.Disponible = "True" entonces
			A[i,j].Disponible:=A[i,j].Disponible +1
			A[3,j].Disponible:=A[3,j].Disponible +1
			A[i,6].Disponible:=A[i,6].Disponible +1
		Sino
			A[i,j].NoDisponible:=A[i,j].NoDisponible +1
			A[3,j].NoDisponible:=A[3,j].NoDisponible +1
			A[i,6].NoDisponible:=A[i,6].NoDisponible +1
		FinSi
		Leer(EJEMPLARES,reg)
	FinMientras
	CERRAR(EJEMPLARES)
	
	Max:=LV
	ESC ("	Sucursal 1 - Sucursal 2 - Sucursal 3 - Sucursal 4 - Sucursal 5 - Total Tipo");
	ESC ("Disp/NoDisp - Disp/NoDisp - Disp/NoDisp - Disp/NoDisp - Disp/NoDisp - Disp/NoDisp")
 	Para i:=1 hasta 2 hacer
		Si i=1 entonces
			ESC("DIGITAL")
		Sino
			ESC("FISICO")
		FinSi

		Para j:=1 hasta 6 hacer
			Si A[3,j].Disponible > Max entonces
				Max:=A[3,j].disponible
				x:=j
			FinSi

			ESC (A[i,j])	
		FinPara
	FinPara
	Sucu:= (A[3,2].Disponibles + A[3,2].NoDisponibles)
	Esc("La cantidad de ejemplares en total de la sucursal 2 son:",Sucu )
	Esc("La sucursal con mayor cantidad de ejemplares disponibles es la numero:",x)
	totdig:= A[1,6].Disponibles + A[1,6].NoDisponibles
	Esc("La cantidad total de ejemplares digitales son:",totdig)
	totfis:=A[2,6].Disponibles + A[2,6].NoDisponibles
	Esc("La cantidad total de ejemplares fisicos son:",totfis)
FinAccion

	





