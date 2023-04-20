Accion Telefonica(Prim,Prim1,Prim2,Prim3:puntero a NODO) Es
Ambiente
    Clientes = Registro
        Num_Cel:N(13)
        DNI:N(8)
    Fin Registro
    Arch:Archivo de Clientes
    reg:Clientes
    //lista circular de entrada
    r1 = Registro
        Ident_Regalo:AN(255)
        cantidad:N(4)
        prox:Puntero a r1
    Fin Registro
    p:Puntero a r1
    //listas de salida
    r2 = Registro
        DNI:N(8)
        Identificador:AN(255)
        prox:Puntero a r2
    Fin Registro
    Prim1,p1,q1:Puntero a r2
    
    r3 = Registro 
        Ident_Regalo:AN(255)
        cantidad:N(4)
        prox,ant:Puntero a r3
    Fin Registro
    Prim2,p2,q2:Puntero a r3
    
    r4 = Registro
        DNI:N(8)
        prox,ant: puntero a r4
    Fin Registro
    Prim3,p3,q3:Puntero a r4

Proceso
	Abrir E/(Arch);Leer(Arch,reg)
	Prim1:=Nill
	Prim2:=Nill
	Prim3:=Nill
	p:=Prim
	Mientras NFDA(Arch) hacer
		Si *p.cantidad > 0 entonces
			Si Prim1=Nill entonces
				Nuevo(q1)
				*q1.DNI:=reg.DNI
				*q1.Identificador:=p.Ident_Regalo
				*q1.prox:=Nill
				Prim1:=q1
				*p.cantidad:=*p.cantidad-1
			Sino
				p1:=Prim1
				Mientras (p1<>Nill) y (*p1.DNI<>*reg.DNI) hacer
					a:=p1
					p1:=*p1.prox
				FinMientras
				Si *p.cantidad > 0 entonces
					Nuevo(q1)
					*q1.DNI:=reg.DNI
					*q1.Identificador:=p.Ident_Regalo
					*a.prox:=q1
					*q1.prox:=Nill
					*p.cantidad:=*p.cantidad-1
				FinSi
			FinSi
			*p.prox
		Sino
			p3:=Prim3
			Si Prim3=Nill entonces
				Nuevo(q3)
				*q3.DNI:=reg.DNI
				*q3.Identificador:=p.Ident_Regalo
				*q3.prox:=Nill
				Prim3:=q3
				*p.cantidad:=*p.cantidad-1
			Sino
				p3:=Prim3
				Mientras (p1<>Nill) y (*p1.DNI<>*reg.DNI) hacer
					a:=p3
					p3:=*p1.prox
				FinMientras
		FinSi






			