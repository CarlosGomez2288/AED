Accion Super Es
Ambiente
    stock=registro
        PID: N(10)
        Stock: N(10)
    Finregistro
    MAE,Act: achivo secuencial de stocl ordenado por PID
    reg1,act: stock

    diarias=registro
        PID: N(10)
        CID: N(10)
        Tipo:("C","D")
        Cantidad: N(10)
        PUni: N(15,2)
        Total: N(15,2)
        TipoE:("Domicilio","Retiro")
    Finregistro
    MOV: archivo secuencial de diarias ordenado por PID
    reg2: diarias

    Prod=registro
        PPID: N(10)
        Nombre: AN(50)
        Descp: AN(150)
        Rubro:("Limpieza","Carnicería","Vendrulería","Bazar","Panadería")
    Finregistro
    reg3: Prod
    index: archivo indexado de Prod ordenado por PID

    Subaccion 

    subaccion_cerrar_archivos_es
		cerrar (Act) ; cerrar (index) ; cerrar (MAE); cerrar (MOV)
	fin subaccion

    Subaccion leerMAE Es
        leer(MAE,reg1)
        Si FDA(MAE) entonces
            reg1.PID:=HV
        FinSi
    FinSubaccion

    Subaccion leerMOV Es
        leer(MOV,reg2)
        Si FDA(MOV) entonces
            reg2.PID:=HV
        FinSi
    FinSubaccion

Proceso
    abrir E/(MAE);leerMAE()
    abrir S/(Act)
    abrir E/(MOV);;leerMOV()
    abrir E/(index)

    Mientras reg1.PID <> HV y reg2.PID <> HV hacer
        Si reg1.PID < reg2.PID entonces
            act:=reg2
            GRABAR(Act,act)
            leerMAE()
        Sino
            Si reg1.PID = reg2.PID entonces
                aux:=reg2
                Mientras reg1.PID = reg2.PID hacer
                    Si regmov.Tipo = "C" entonces
                        Si reg1.Stock >= reg2.Cantidad entonces
                            act:=reg1
                            act.Stock:=act.Stock - reg2.Cantidad
                            Si TipoEnvio = "Domicilio" entonces
                                ContDom:=ContDom+1
                            FinSi
                        Sino
                            ContInsuf:=ContInsuf + 1
                            reg3.PID:=reg2.PID
                            leer(index,reg3)
                            Si existe entonces
                                Esc("No se pudo vender",reg2.Cantidad,"prodcutos de:",reg3.Nombre,"del rubro:",reg3.Rubro)
                            FinSi
                        FinSi
                    Sino
                        act.Stock:=act.Stock + reg2.Cantidad
                    FinSi
                    leerMOV()
                FinMientras
                GRABAR(Act,act)
                leerMAE()
            FinSi
        FinSi
    FinMientras
    Esc("La cantidad de productos comprados con envio a domicilio son:",ContDom)
    Esc("La cantidad de productos que no se vndieron por cantidad infsuficiente son:",ContInsuf)
    cerrar_archivos()
FinAccion

----------------------------------------------------------------------------------
Accion SuperResis2 Es
Ambiente
    A: arreglo de [1..3,1..5] de ente#Region 



Proceso
    Para i:=1 hasta 3 hacer
        Para j:=1 hasta 5 hacer
            A[i,j]:=0
        FinPara
    FinPara


                
