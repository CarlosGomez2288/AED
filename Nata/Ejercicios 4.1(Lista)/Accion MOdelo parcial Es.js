Accion Super_Parcial(Prim1: puntero a NODO) Es
Ambiente
	Fecha=registro
		DD: 1..31
		MM: 1..12
		AAAA: N(4)
	finregistro
	
	secu=registro
		FechaC: Fecha
		DNI: N(8)
		CantArt: N(3)
		Importe: N(15,2)
	finregistro
	reg1: secu
	Arch1: archivo secuencial de secu ordenado por FechaC

	index=registro
		DNI: N(8)
		AyN: AN(60)
		FechaAd: Fecha
		Categoria: AN(5)
	finregistro
	reg2: index
	Arch2: archivo indexado de index ordenado por DNI

	sal=registro
		DNI: N(8)
		CantComp: N(2)
		Importe: N(15,2)
		prox: puntero a sal
	finregistro
	p2,q,Prim2: puntero a sal

	r=registro
		ImportMin:N(15,2)
		ImportMax:N(15,2)
		Descuento: 0,01 a 0,99
		Cupo: N(10)
		Rubro: 1..9
		prox,ant: puntero a r
	finregistro
	p1: puntero a r

	Porcent: real
	band: booleano
Proceso
	Abrir E/(Arch1);Leer(Arch1,reg1)
	Abrir E/(Arch2)
	Prim2:=Nill
	p1:=Prim1
	
	Mientras NFDA(Arch1) hacer
		band:=Falso
		reg2.DNI:=reg1.DNI
		Leer(Arch2,reg2)

		Si no existe entonces
			p2:=Prim2
			Mientras (p2<>Nill) y (reg1.DNI<>*p2.DNI) hacer
				a:=q;
				q:=*p.prox
			FinMientras
			Si (reg1.DNI=*p1.DNI) entonces
				*p1.CantComp:=*p1.CantComp+1
			Sino
				Si Prim2=Nill
					Prim2:=q
					*q.prox:=Nill
				Sino
					p2:=Prim2
					Nuevo(q)
					*q.DNI:=reg2.DNI
					*q.CantComp:=1
					*q.Importe:=reg1.Importe
					Mientras (p2<>Nill) y (*q2.DNI<*p2.DNI) hacer
						a:=q;
						q:=*p.prox
					FinMientras
					Si p2=Prim2 entonces
						Prim2:=q
						*q.prox:=p2
					Sino
						*ant.prox:=q
						*q.prox:=p2
					FinSi
				FinSi
			FinSi
		FinSi
		
		Mientras (p1<>Nill) y (band=Falso) hacer
			Si (reg1.Importe<=p1.ImportMax) y (reg1.Importe>=p1.ImportMin) entonces
				band:=Verdadero
			FinSi
			p1:=*p1.prox
		FinMientras
		Si band=Verdadero entonces
			Si *p1.Cupo>0 entonces
				Esc("El porcentaje de descuento del importe es:",Porcent:=*p1.Descuento*100)
				Esc("El rubro del mismo descuento es:",*p1.Rubro)
			Sino
				Esc("No le corresponde un descuento")
			FinSi
		FinSi
		Leer(Arch1,reg1)
	FinMientras
	Cerrar(Arch1);Cerrar(Arch2)
FinAccion

Accion Presion Es
	A1,A2: arreglo de [1..4] de entero
	i: entero

	r=registro
		DNI: N(8)
		NyA: AN(60)
		NroCama: N(4)
		NroHabit: N(3)
		Pa_sistolica: A[]
		Pa_diastolica: N(3)
	finregistro
	reg: r
	
	Funcion()











FinAccion