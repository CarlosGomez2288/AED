Accion Pedidosha Es(Prim.puntero a NODO)
Ambiente
	secu=registro
		Codigo: N(6)
		Domicilio: AN(60)
		Person: N(60)
		Costo: N(5,2)
	finregistro
	reg: secu
	Arch: archivo de secu ordenado por Codigo

	r1=registro
		Codigo: N(6)
		Domicilio: AN(60)
		Person: N(60)
		Costo: N(5,2)
		prox: puntero a r1
	finregistro
	p,a: puntero a r1

	Total,ContE,ContNE,ContT: entero
	Porcent: real
	rta: booleano
Proceso
	Abrir E/(Arch)
	Leer(Arch,reg)
	Mientras NFDA(Arch) hacer
		Esc("Se entregó el pedido? si/no")
		Si rta="si" entonces
			ContE:=ContE+1
			p:=Prim
			Mientras (p<>Nill) y (*p.Codigo<>reg.Codigo) hacer
				a:=p
				p:=*p.prox
			FinMientras
			Si p=prim entonces
				p:=*p.prox
			Sino
				*a.prox:=*p.prox
			FinSi
			Disponer(p)
			Total:=Total+reg.Costo
		Sino
			Esc("Se pudó entregar el pedido la segunda vez? si/no")
			Si rta="si" entonces
				ContE:=ContE+1
				p:=Prim
				Mientras (p<>Nill) y (*p.Codigo<>reg.Codigo) hacer
					a:=p
					p:=*p.prox
				FinMientras
				Si p=prim entonces
					prim:=*p.prox
				Sino
					*a.prox:=*p.prox
				FinSi
				Disponer(p)
				Total:=Total+reg.Costo
			Sino
				ContNE:=ContNE+1
				Total:=Total-reg.Costo
			FinSi
		FinSi
		ContT:=ContT+1
		p:=*p.prox
		Leer(Arch,reg)
	FinMientras
	Cerrar(Arch)
	Porcent:=(ContNE*100)/ContT

	Esc("El total de pedidos entregados son:",ContE)
	Esc("El total de pedidos no entregados son:",ContNE)
	Esc("El porcentaje de pedidos no entregados es:",Porcent)
	Si Total>0 entonces
		Esc("La ganancia del día es de:",Total)
	Sino
		Esc("No se consiguió ganancias el día de hoy")
	FinSi
FinAccion