Accion SitioWeb Es
Ambiente
    Fecha=registro  
        AA: N(4)
        MM: 1..12
        DD: 1..31
    Finregistro
    Opiniones=registro
        Clave=registro
            Usuario: AN(30)
            FechaOP: Fecha
        Finregistro
        FechaUC: Fecha
        Calificación: 1..5
        Servicio: 1..20
    Finregistro
    OPINIONES: archivo de Opiniones ordenado por Clave
    reg1: Opiniones

    Usuarios=registro
        Usuario: AN(30)
        AyN: AN(30)
        Categoria:{"Silver","Gold"}
    Finregistro
    USUARIOS: archivo indexado de Usuarios indexado por Usuario
    reg2: Usuarios

    A: arreglo de [1..20] de Alfanumerico
    i: entero

Proceso
    Abrir E/(OPINIONES);Leer(OPINIONES,reg1)
    Abrir E/S(USUARIOS)

    Mientras NFDA(OPINIONES) hacer
		i:=reg1.Servicio
		Si reg1.Calificación = 1 o reg1.Calificación = 2 entonces
			Esc("El nombre del servicio",A[i])
		FinSi
		ContOp:=0
		aux:=reg2.Usuario
		Mientras aux = reg2.Usuario hacer
			ContOp:=ContOp+1
			Leer(OPINIONES,reg1)
		FinMientras
		reg2.Usuario:=reg1.Usuario
		Leer(USUARIOS,reg2)
		Si existe entonces
			Si ContOp > 5 entonces
				reg2.Categoria:="Gold"
				REGRABAR(USUARIOS,reg2)
			FinSi
		FinSi
	FinMientras
	CERRAR(OPINIONES);CERRAR(USUARIOS)
FinAccion

    
