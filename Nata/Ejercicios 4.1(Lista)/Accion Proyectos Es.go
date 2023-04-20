Accion Proyectois(Prim: puntero a r1) Es
Ambiente
	proy=registro
		Codigo: N(10)
		Nombre: AN(60)
		Tipo:{"D","W"}
		CantE: N(3)
	finregistro
	reg: proy
	Arch: archivo secuencial de proy ordenado por Codigo

	r1=registro
		Descripción: AN(250)
		Estado:{"N","O","R"}
		prox: puntero a r1
	finregistro
	p: puntero a r1

	r2=registro
		Codigo: N(10)
		Nombre: AN(60)
	finregistro
	p1,p2,q,Prim1,Prim2: puntero a r2

Proceso
	Abrir E/(Arch);Leer(Arch,reg)
	Prim1:=Nill
	Prim2:=Nill
	p

FinAccion