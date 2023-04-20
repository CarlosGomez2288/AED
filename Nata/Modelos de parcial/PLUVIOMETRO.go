accion_pluviometro_es
ambiente
	precipitaciones = registro // mae
		clave= registro
			idpluv : n (5)
			fechareg: fecha
		fin registro
		precip: n (2,2)
		estado: {"AC","MA"}
	fin registro
	P,PA: archivo de precipitaciones ordenado por clave
	reg1,reg2,aux: precip

	mediciones = registro  // mov
		clavec = registro
			idpluv: n (5)
			fechareg: fecha
		fin registro
		hora: n (2,2)
		estado : {"AC","MA"}
		precip : n (2,2)
	fin registro

	M : archivo de mediciones ordenado por clavec
	reg3: medi

	A: arreglo [1..25] de alfanumericos
	i: alfanumericos

	pluviometros = registro
		idpluv : n(5)
		modelo: an (20)
		desc : an (30)
		dpto : 1..25
	fin registro
	index: archivo de pluviometros indexado por idpluv
	reg4: pluviometros

	fecha = registro
		aa: n (4)
		mm: 1..12
		dd:1..31
	fin registro

	subaccion_leermae_es
		leer (prec,regprec)
		si fda (prec) entonces
			regprec.clave := HV
		fin si
	fin subaccion

	subaccion_leermov_es
		leer (med,regmed)
		si fda (med) entonces
			regmed.clavec := HV
		fin si
	fin subaccion

	ContM: entero

	subaccion_cerrar_archivos_es
		cerrar (act) ; cerrar (index) ; cerrar (prec); cerrar (med)
	fin subaccion

Proceso
	Abrir E(prec);leermae()
	Abrir S(act);leermov()
	Abrir E/(med);Leer(med,regmed)
	Abrir E/(index)

	Mientras (reg1.clave<> HV o reg3.clavec<>HV) Hacer
		Si reg1.clave < reg3.clavec entonces
			regact:=regprec
			GRABAR(act,regact)
			leermae()
		Sino
			Si reg1.clave = reg3.clavec entonces
				aux:=reg3
				x:=True
				Mientras regprec.clave = regmed.clavec  Hacer
					Si x <> True entonces
						Si aux.estado = "AC" entonces
							aux.precip:=aux.precip + reg3.precp 
						Sino
							x:=False
							ContM:=ContM + 1
							aux.estado:="MA"
							reg4.idpluv:=aux.idpluv
							leer(index,reg4)
							Si existe
								i:=reg3.dpto
								Esc("El puvliometro con id:",reg3.idpluv,"del departamento",A[i],"esta en mantenimiento")
							FinSi
						FinSi
					FinSi
					leermov()
				FinMientras
				reg2:=aux
				GRABAR(act,reg2)
				leermae()
			Sino
				aux.clave:=reg3.clavec
				aux.precip:=reg3.precip
				aux.estado:=reg3.estado
				leermov()
				x:=True

				Mientras regprec.clave = regmed.clavec  Hacer
					Si x <> True entonces
						Si aux.estado = "AC" entonces
							aux.precip:=aux.precip + reg3.precp 
						Sino
							x:=False
							ContM:=ContM + 1
							aux.estado:="MA"
							reg4.idpluv:=aux.idpluv
							leer(index,reg4)
							Si existe
								i:=reg3.dpto
								Esc("El puvliometro con id:",reg3.idpluv,"del departamento",A[i],"esta en mantenimiento")
							FinSi
						FinSi
					FinSi
					leermov()
				FinMientras
				reg2:=aux
				GRABAR(act,reg2)
				leermae()
			FinSi
		FinSi
	FinMientras
	Esc("El total de pluviometros en mantenimiento son:",ContM)
	cerrar_archivos()
FinAccion

----------------------------------------------------------------------------------------------------
Accion pluviometro2 Es
ambiente
	A: arreglo de [1..26,1..12] de entero
	i,j: entero

Proceso
	Abrir E/(MAE);leer(MAE,reg1)
	Abrir E/(index)

	Para i:=1 hasta 26 Hacer
		Para j:=1 hasta 12 Hacer
			A[i,j]:=0
		FinPara
	FinPara

	Mientras NFDA(MAE) Hacer
		reg2.PID:=reg1.clave.PID
		leer(index,reg2)
		Si existe entonces
			Si reg2.estado = "AC" entonces
				i:=reg2.departamento
				j:=reg1.clave.fechareg.mes
				A[i,j]:=A[i,j] + reg1.precip
				A[26,j]:=A[26,j] + reg1.precip
			FinSi
		Sino
			Esc("No se encontro el id")
		FinSi
	FinMientras

	minprecip:=HV
	min:=HV

	Para j:=1 hasta 12 Hacer
		Para i:=1 hasta 26 Hacer
			Si A[26,j] < min entonces
				Mes:=j
				min:=A[26,j]
			FinSi
		Para i:=1 hasta 25 Hacer
			Si A[i,j] > 350 entonces
				Según
					=1
					=2
					=3
					=4
					=5
					=6
					=7
					=8
					=9
					=10
					=11
					=12:m:="Diciembre"
				FinSegún
				Esc("En el dpto",A[i],"del mes:",m,"las precipitaciones superaron los 350 mm caidos")
			FinSi
			Si A[i,j] < minprecip entonces
				minprec:=A[i,j]
				mesmin:=j
				dptomin:=i
			FinSi
		FinPara
	FinPara
	Según mesmin Hacer
		=1
		=2
		=3
		=4
		=5
		=6
		=7
		=8
		=9
		=10
		=11
		=12:m:="Diciembre"
	FinSegún
	Esc("En el dpto",A[i],"del mes:",m,"las precipitaciones superaron los 350 mm caidos")
	
			