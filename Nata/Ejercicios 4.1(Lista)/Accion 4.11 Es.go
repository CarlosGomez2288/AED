Accion 4.11 (Prim,ULT: puntero a NODO)Es
Ambiente
	r1=registro
		Antiguedad: N(2)
		NroPerso: N(5)
		Nombre: AN(50)
		Asignaciones: N(2)
		ant,prox: puntero a NODO
	finregistro

	r2=registro
		DNI: N(8)
		Nombre: AN(50)
		Antiguedad: N(2)
	finregistro
	Arch: archivo ordenado por DNI
	reg: r2


Proceso
	Abrir E(Arch);Leer(Arch,reg)
	Prim:=Nill
	ULT:=Nill


	Mientras (NFDA(Arch)) hacer
		Nuevo(Q)
		*Q.Antiguedad:=r2.Antiguedad
		*Q.NroPerso:=r2.DNI
		*Q.Nombre:=reg.Nombre
		*Q.Asignaciones:=0
		
		Si Prim=Nill entonces
			*Q.ant:=Nill
			*Q.prox:=Nill
			ULT:=Q
			Prim:=Q
		Sino
			P:=Prim
			Mientras (P<>Nill) 



		P:=*P.prox
	FinMientras

	


