Accion Comple 4.5 Es(Prim,Prim1,Prim2: puntero a NODO)
Ambiente
	r1=registro
		NroCliente: N(10)
		NroPedido: N(10)
		Precio: N(15,2)
		Tipo={"C","R"}
		prox: puntero a NODO
	finregistro
	Prim,P,Q,A: puntero a NODO

	r2=registro
		NroCliente: N(10)
		DNI: N(8)
		Domicilio: AN(50)
		DineroD: N(15,2)
		Deudor={"SI","NO"}
		Baja: logico
	finregistro
	reg: r2
	CLIENTES: archivo de r2 indexado por NroCliente

	r3=registro
		NroCliente: N(10)
		Total: N(15,2)
		prox: puntero a NODO
	finregistro
	Prim1,Prim2: puntero a NODO
	Tot: entero

Proceso
	Abrir E/(CLIENTES)
	Prim1:=Nill;Prim2:=Nill
	P:=Prim
	Mientras (P<>Nill) hacer
		reg.NroCliente:=*P.NroCliente
		Leer(CLIENTES,reg)
		Tot:=0
		Si existe entonces
			Si reg.Baja=Verdadero entonces
				reg.Baja:=Falso
			FinSi
			Mientras (P<>Nill) y (reg.NroCliente=*P.NroCliente) hacer
				Si *P.Tipo="R" entonces
					reg.DineroD:=reg.DineroD+*P.Precio
				FinSi
				Tot:=Tot+*P.Precio
				P:=*P.prox
			FinMientras
			Nuevo(Q)
			*Q.NroCliente:=*P.NroCliente
			Si reg.DineroD > 0 entonces
				reg.Deudor:="SI"
				*Q.Total:=Tot
				*Q.prox:=Prim1
				Prim1:=Q
			Sino
				reg.Deudor:="NO"
				*Q.Total:=Tot
				*Q.prox:=Prim2
				Prim2:=Q
			FinSi
			Regrabar(CLIENTES,reg)
		Sino
			Esc("El cliente no existe")
		FinSi
		P:=*P.prox
	FinMientras
	Cerrar(CLIENTES)
FinAccion



