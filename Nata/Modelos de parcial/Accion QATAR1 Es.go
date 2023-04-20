Accion QATAR1 Es
Ambiente
	r2=registro
		Clave=registro
			Cod_fig: N(5)
			Cod_amigo: N(5)
		FinRegistro
		FechaS: Fecha
	FinRegistro
	reg2: r2
	INTERCAMBIOS: archivo de r2 ordenado por Clave

	Fecha=registro
		AA: N(4)
		MM: 1..12
		DD: 1..31
	FinRegistro

	r1=registro
		Cod_fig: N(5)
		Cantidad: N(2)
		Permitir:{"SI","NO"}
	FinRegistro
	reg1,reg3,aux: r1
	ALBUM,SAL: archivo de r1 ordenado por Cod_fig

	Cont: entero

	Procedimiento LeerMae Es()
		Leer(ALBUM,reg1)
		Si FDA(ALBUM) entonces
			reg1.Cod_fig:=HV
		FinSi
	FinProcedimiento

	Procedimiento LeerMov Es()
		Leer(INTERCAMBIOS,reg2)
		Si FDA(INTERCAMBIOS) entonces
			reg1.Clave:=HV
		FinSi
	FinProcedimiento

Proceso
	Abrir E/(ALBUM);LeerMae()
	Abrir E/(INTERCAMBIOS;LeerMov()
	Abrir S/(SAL)
	Cont:=0

	Mientras (reg1.Cod_fig<>HV o reg2.Clave.Cod_fig<>HV) hacer
		Si (reg1.Cod_fig < reg2.Clave.Cod_fig) entonces
			reg3:=reg1
			GRABAR(SAL,reg3)
			LeerMae()
		Sino
			Si (reg1.Cod_fig = reg2.Clave.Cod_fig) entonces
				Si reg2.Permitir = "SI" entonces
					aux:=reg2
					Mientras (reg1.Cod_fig = reg2.Clave.Cod_fig) hacer
						aux.Cantidad:=aux.Cantidad+1
						Cont:=Cont+1
						LeerMov()
					FinMientras
					reg3:=aux
				Sino
					Mientras (reg1.Cod_fig = reg2.Clave.Cod_fig) hacer
						LeerMov()
					FinMientras
				FinSi
				reg3:=aux
				GRABAR(SAL,reg3)
				LeerMae()
			Sino
				Si (diff_dias(7,reg2.FechaS) = Verdadero) entonces
					reg3.Cod_fig:=reg2.Cod_fig
					reg3.Cantidad:=1
					reg3.Permitir:="NO"
				Sino
					Mientras (reg1.Cod_fig = reg2.Clave.Cod_fig) hacer
						LeerMov()
					FinMientras
				FinSi
				GRABAR(SAL,reg3)
				LeerMov()
			FinSi
		FinSi
	FinMientras
	CERRAR(INTERCAMBIOS);CERRAR(ALBUM);CERRAR(SAL)
	Esc("La cantidad de figuritas permitidas son:",Cont)
FinAccion
------------------------------------------------------------------------------
Accion QATAR2 Es
Ambiente
	r1=registro
		Cod_Usuario: N(5)
		Cod_fig: N(5)
		Cantidad: N(2)
		Tipo:{"C","D","V"}
	FinRegistro
	reg1: r1
	ALBUM: archivo de r1 ordenado por Cod_Usuario

	r2=registro
		Cod_Usuario: N(5)
		Apellido: AN(15)
		Nombre: AN(15)
		Celular: N(10)
	FinRegistro
	reg2,z: r2
	AMIGOS: archivo de r2 indexado por Cod_Usuario

	A: arreglo de [1..4,1..11] de AN
	i,j,Max,Total: entero
	Percet: real

Proceso
	Abrir E/(ALBUM);Leer(ALBUM,reg1)
	Abrir E/(AMIGOS);Leer(AMIGOS,reg2)
	
	Para i:=1 hasta 4 hacer
		Para j:=1 hasta 11 hacer
			A[i,j]:=0
		FinPara
	FinPara

	Mientras NFDA(ALBUM) hacer
		Según reg1.Tipo hacer
			="D":i:=1
			="C":i:=2
			="V":i:=3
		FinSegún
		j:=reg1.Cod_Usuario

		A[i,j]:=A[i,j]+1
		A[4,j]:=A[4,j]+1
		A[i,11]:=A[i,11]+1
		Total:=A[i,j] + Total
		Leer(ALBUM,reg1)
	FinMientras

	Max:=LV
	Para i:=1 hasta 3 hacer
		Para j:=1 hasta 10 hacer
			Si A[i,j] > Max entonces
				Max:=A[i,j]
				z:=j
			FinSi

			Esc("Porcentaje",Percet:=(A[i,j]*100)/Total)
			Esc("TotalxUsuario",A[4,j])
		FinPara
		Esc("TotalxTipo",A[i,11])
	FinPara

	reg2.Cod_amigo:=z
	Leer(AMIGOS,reg2)
	Si existe entonces
		z.Apellido:=reg2.Apellido
		z.Nombre:=reg2.Nombre
	FinSi

	Esc("El usuario Numero",j,"su nombre es:",z.Apellido," ",z.Nombre)

	CERRAR(ALBUM);CERRAR(AMIGOS)
FinAccion
	




					