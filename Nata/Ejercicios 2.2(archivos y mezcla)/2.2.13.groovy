Ejercicio 2.2.13
Un Casino de la región ha notado un incremento en los costos
de las reparaciones de tragamonedas en sus sucursales.
Por ello solicitó un informe con la cantidad de reparaciones y sus costos,
discriminados según tragamonedas, modelo, marca, sucursal y total general.

Se dispone de un archivo REPARACIONES, con el siguiente formato.
Cada registro representa la reparación de un tragamonedas,
tener en cuenta que puede existir más de una reparación por tragamonedas.

REPARACIONES Ordenado por Cod_Sucursal, Marca, Modelo, Cod_Tragamonedas

Cod_Sucursal/Marca/Modelo/Cod_Tragamonedas/Fecha_Reparacion/Costo_Reparacion

Realice el algoritmo para emitir el informe con los totales solicitados

Accion 2.2.13 Es
Ambiente
	Fecha=registro
		AA: N(4)
		MM: 1..12
		DD: 1..31
	FinRegistro

	Datos=registro
		Cod_Sucursal: N(6)
		Marca: AN(30)
		Modelo: AN(15)
		Cod_Tragamonedas: N(6)
		Fecha_Reparacion: Fecha
		Costo_Reparacion: N(10)
	FinRegistro

	REPARACIONES: archivo secuencial ordenado por Cod_Sucursal, Marca, Modelo, Cod_Tragamonedas
	reg: REPARACIONES
	resgMarca,resgTragamonedas: alfanumerico
	resgSucursal,resgModelo: numerico

	cant_trag,tot_trag: numerico
	cant_modelo,tot_modelo: numerico
	cant_marca,tot_marca: numerico
	cant_sucursal,tot_sucursal: numerico
	cantgral,totgral: numerico

	Subaccion Corte_Tragamonedas Es
		Esc("Para el codigo de tragamonedas",resgTragamonedas,"la cantidad de veces reparadas es de:",cant_trag,
	"y el coste de:",tot_trag)
		tot_modelo:=tot_modelo+tot_trag
		cant_modelo:=cant_modelo+cant_trag
		resgTragamonedas:=reg.Cod_Tragamonedas
		tot_trag:=0
		cant_trag:=0
	FinSubaccion

	Subaccion Corte_Modelo Es
		Corte_Tragamonedas
		Esc("Para el Modelo",resgModelo,"la cantidad de veces reparadas es de:",cant_modelo,
	"y el coste de:",tot_modelo)
		tot_marca:=tot_marca+tot_modelo
		cant_marca:=cant_marca+cant_modelo
		resgModelo:=reg.Modelo
		tot_modelo:=0
		cant_modelo:=0
	FinSubaccion

	Subaccion Corte_Marca Es
		Corte_Modelo
		Esc("Para la marca",resgMarca,"la cantidad de veces reparadas es de:",cant_marca,
	"y el coste de:",tot_marca)
		tot_sucursal:=tot_marca+tot_sucursal
		cant_sucursal:=cant_marca+cant_sucursal
		resgMarca:=reg.Marca
		tot_marca:=0
		cant_marca:=0
	FinSubaccion

	Subaccion Corte_Sucursal Es
		Corte_Marca
		Esc("Para el codigo de sucursal",resgSucursal,"la cantidad de veces reparadas es de:",cant_sucursal,
	"y el coste de:",tot_sucursal)
		totgral:=tot_sucursal+totgral
		cantgral:=cant_sucursal+cantgral
		resgSucursal:=reg.Cod_Sucursal
		tot_sucursal:=0
		cant_sucursal:=0
	FinSubaccion


Proceso
	Abrir E/(REPARACIONES)
	Leer(REPARACIONES,reg)
	cant_trag:=0
	cant_modelo:=0 
	cant_marca:=0
	cant_sucursal:=0 
	cantgral:=0
	tot_trag:=0
	tot_modelo:=0
	tot_marca:=0
	tot_sucursal:=0
	totgral:=0

	resgTragamonedas:=reg.Cod_Tragamonedas
	resgModelo:=reg.Modelo
	resgMarca:=reg.Marca
	resgSucursal:=reg.Cod_Sucursal

	Mientras NFDA(REPARACIONES) hacer
		Si resgSucursal < reg.Cod_Sucursal Entonces
			Corte_Sucursal
		Sino
			Si resgMarca < reg.Marca Entonces
				Corte_Marca
			Sino
				Si resgModelo < reg.Modelo Entonces
					Corte_Modelo
				Sino
					Si resgTragamonedas < reg.Cod_Tragamonedas Entonces
						Corte_Tragamonedas
					FinSi
				FinSi
			FinSi
		FinSi
		tot_trag:=reg.Costo_Reparacion+tot_trag
		cant_trag:=cant_trag+1
		Leer(REPARACIONES,reg)
	FinMientras
	Corte_Sucursal
	Esc("El total general de reparaciones realizadas son:",cantgral)
	Esc("El total general de coste de repación realizadas es de:",totgral)
	Cerrar(REPARACIONES)
FinAccion
