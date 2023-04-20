Accion COSME Es(Prim,Ult:puntero a NODO)
Ambiente
    r1=registro
        Codigo: N(10)
        Rubro: AN(50)
        Precio: N(15,2)
		prox: puntero a r1
    finregistro
	p,aux: puntero a r1

	r2=registro
		Codigo: N(10)
		Nombre: AN(50)
		PrecioOf: N(15,2)
		Porcent: N(15,2)
		prox,ant: puntero a r2
	finregistro
	q,p,Prim,May: puntero a r2

	Prod=registro
		Codigo: N(10)
		Nombre: AN(50)
		Rubro: AN(50)
		Precio: N(15,2)
		Stock: N(10)
	finregistro
	reg: Prod
	Productos: archivo indexado Prod ordenado por Codigo
	Por: entero
Proceso
	Abrir E/(Productos)
	P:=Nill

	Mientras NFDA(Productos) hacer
		Mayor:=LV
		aux:=p
		Mientras (reg.Codigo=*p.Codigo) hacer
			reg.Codigo:=*p.Codigo
			Leer(Productos,reg)
			Si existe entonces
				Por:=(*p.PrecioOf*100/(reg.Precio))
				Si Por>Mayor entonces
					Mayor:=Por
					May:=p
				FinSi
			Sino
				Esc("No se encontro el producto")
			FinSi
			p:=*p.prox
		FinMientras

		reg.Codigo:=May.Codigo
		Leer(Productos,reg)

		Si existe entonces
			Nuevo(q)
			*q.Codigo:=*May.Codigo
			*q.Nombre:=reg.Nombre
			*q.PrecioOf:=*May.PrecioOf
			*q.Porcent:=Mayor
			Si Prim=Nill entonces
				*q.prox:=Nill
				*q.ant:=Nill
				Prim:=q
				Ult:=q
			Sino
				*q.prox:=Nill
				*q.ant:=Ult
				*Ult.prox:=q
				Ult:=q
			FinSi
		Sino
			Esc("El producto no existe")
		FinSi
		p:=*p.prox
	FinMientras
	Cerrar(Productos)
FinAccion




				



		
