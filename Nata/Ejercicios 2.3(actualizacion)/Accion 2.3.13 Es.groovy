Accion 2.3.13 Es
Ambiente
    r2=registro
        Clave=registro
            cod_figurita: N(5)
            cod_amigo: N(5)
        finregistro
        FechaS: Fecha
    finregistro
    reg2: r2
    Arch2: archivo de r2 ordenado por Clave

    r1=registro
        cod_figurita: N(5)
        cantidad: N(2)
        permitir:{"si","no"}
    finregistro
    reg1,sal: registro
    Arch1,ArchSal: archivo de r1 ordenado por cod_figurita

    subaccion LEERMaestro es
		leer (Arch1, reg1)
		si fda (Arch1) entonces
			reg1.cod_figurita:= HV
		fin si
	fin subaccion

	subaccion LEERMovimiento es
		leer (Arch2, reg2)
		si fda (Arch2) entonces
			reg2.Clave.cod_figurita := HV
		fin si
	fin subaccion
    cont: entero
Proceso
    Abrir E/(Arch1);LEERMaestro
    Abrir E/(Arch2);LEERMovimiento
    Abrir S/(ArchSal)
    cont:=0

    Mientras (reg1.cod_figurita<>HV) o (reg2.Clave.cod_figurita<>HV) hacer
        Si (reg1.cod_figurita = reg2.Clave.cod_figurita) entonces
            sal:=reg2
            Grabar(ArchSal,sal)
            LEERMaestro
        Sino
            Si (reg1.cod_figurita = reg2.Clave.cod_figurita) entonces
                aux:=reg1
                Si reg1.permitir = "si" entonces
                    Mientras (reg1.cod_figurita = reg2.Clave.cod_figurita) hacer
                        aux.cantidad:=aux.cantidad+1
                        cont:=cont+1
                        LEERMovimiento
                    FinMientras
                Sino
                    Mientras (reg1.cod_figurita = reg2.Clave.cod_figurita) hacer
                        LEERMovimiento
                    FinMientras
                Finsi
                sal:=aux
                Grabar(ArchSal,sal)
                LEERMaestro
            Sino
                Si (diff_dias(7,reg2.FechaS)=Verdadero) entonces
                    sal.cod_figurita:=reg2.Clave.cod_figurita
                    sal.cantidad:=1
                    sal.permitir:="no"
                    Grabar(ArchSal,sal)
                FinSi
                LEERMovimiento
            FinSi
        Finsi
    FinMientras
    Esc("La cantidad de veces que se permitio duplicados son:",cont)
    Cerrar(Arch1)
    Cerrar(Arch2)                    
    Cerrar(ArchSal)
FinAccion

Accion punto 2 Es
Ambiente
    album=registro
        User:
        cod_figurita
        cantidad
        tipo
    finregistro
    arch1: archivo de album ordenado por usuario
    reg1: album

    amigos=registro
        usuario:
        apellido
        nombre
        celular
    finregistro
    arch2:archivo indexado de amigos ordenado por usuario
    reg2: amigos

    dato=registro
        NyA:
        cantidad
    finregistro

    A: arreglo de [1..4,1..11] de dato

Proceso
    Abrir E/(Arch1);Leer(Arch1,reg1)
    Abrir E/(Arch2);

    Para i:=1 hasta 4 hacer
        Para j:=1 hasta 11 hacer
            A[i,j].NyA:=0
            A[i,j].cantidad:=0
        FinPAra
    FinPAra

    Mientras NFDA(Arch1) hacer
        aux.User:=reg1.User
        Mientras aux.User=reg2.User hacer
            Según reg1.tipo hacer
               ="1":i:=reg1.tipo
               ="2":i:=reg1.tipo
               ="3":i:=reg1.tipo
            Finsegún
            j:=reg2.usuario
            A[i,j].cantidad:=A[i,j].cantidad+1
            A[4,j].cantidad:=A[4,j].cantidad+1
            A[i,11].cantidad:=A[i,11].cantidad+1
            A[4,11].cantidad:=A[4,11].cantidad+1
            Leer(Arch2,reg2)
        FinMientras
        Leer(Arch1,reg1)
    FinMientras
    Cerrar(Arch1);Cerrar(Arch2)

    Max:=LV
   
    Para j:=1 hasta 10 hacer
        Para 1 hasta 3 hacer
            Si A[i,j].cantidad > Max entonces
                x:=i
                Max:=A[i,j].cantidad
            FinSi
        FinPara
        
            




