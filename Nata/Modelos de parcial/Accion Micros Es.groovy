Accion Micros Es
Ambiente
    Fecha=registro
        AA: N(4)
        MM: 1..12
        DD: 1..31
    Finregistro

    Millas=registro
        DNI: N(8)
        Millas: N(10)
        Utl_Carga: Fecha
    Finregistro
    MILLAS: archivo indexado de Millas indexado por DNI
    reg1:Millas

    Destinos=registro
        Origen: N(1)
        Destino: N(1)
        Millas: N(10)
        Duración: N(2)
    Finregistro
    DESTINOS: archivo indexado de Destino indexado por Origen,Destino
    reg2: Destino

    Cont_UC,Milla: entero
    Fechahoy: Fecha

Proceso
    Abrir E/S(MILLAS)
    Abrir E(DESTINOS)

    Esc("Ingrese la fecha actual")
    Fechahoy:=fechaactual()

    Cont_UC:=0
    
    Esc("Desea realizar una carga de cliente? SI/NO");Leer(RTA)
    Mientras (RTA = "SI") hacer
        Esc("Ingrese el DNI del cliente"),Leer(DNI)
        reg1.DNI:=DNI
        Leer(MILLAS,reg1)
        Si existe entonces
            Esc("Ingrese el origen y el destino del cliente");Leer(Origen,Destino)
            reg2.Origen:=Origen
            reg2.Destino:=Destino
            Leer(DESTINOS,reg2)

            Si reg2.Millas => reg1.Millas entonces

                reg1.Millas:=reg1.Millas - reg2.Milla

                Esc("Desea realizar la carga de millas? SI/NO");Leer(RTA2)
                Esc("Cuantas millas desea cargar?");Leer(Millas)

                Si reg1.Utl_Carga.MM = Fechahoy.MM entonces
                    Cont_UC:=Cont_UC + 1
                FinSi

                Si RTA2 = "SI" entonces
                    reg1.Millas:=reg1.Millas + Milla
                FinSi

                REGRABAR(MILLAS,reg1)
            Sino
                Esc("NO tiene la suficiente cantidad de millas necesarias")
            FinSi
        FinSi
        Esc("Desea realizar ingresar otro cliente? SI/NO");Leer(RTA)
    FinMientras
    Cerrar(MILLAS);Cerrar(DESTINOS)
    Esc("La cantidad de clientes que abordaron el micro anteoriormente en el ultimo mes son:",Cont_UC)
FinAccion

----------------------------------------------
Accion Micro2 Es
Ambiente
    A: arreglo de [1..4,1..11] de viaje2
    i,j: entero
    

    Fecha=registro
        AA: N(4)
        MM: 1..12
        DD: 1..31
    Finregistro

    viaje = registro
        FECHAV: Fecha
        Origen: N(1)
        Destino: N(1)
        MillasCompra: N(10)
    Finregistro
    VIAJE: archivo de viajes
    reg: viaje

    viaje2 = registro
        MillasCant: N(10)
        MillasCompra: N(10)
    Finregistro
    reg1:viaje2
        

Proceso
    Abrir E/(VIAJE);Leer(VIAJE,reg)
    
    Para i:=1 hasta 5 hacer
        Para j:=1 hasta 10 hacer
            A[i,j]:=0
        FInPara
    FInPara
    
    Mientras NFDA(VIAJE) hacer

        j:=reg.Origen

        Según reg.FECHAV.MM hacer
            <=4:i:=1
            <=8:i:=2
            <=12:i:=3
        FinSegún
        
        A[i,j].MillasCompra:=A[i,j].MillasCompra + reg2.MillasCant
        A[i,j].MillasCant:=A[i,j].MillasCant + 1
        A[4,j].MillasCompra:=A[4,j].MillasCompra + A[i,j].MillasCompra
        A[4,j].MillasCant:=A[4,j].MillasCant + 1
        A[i,11].MillasCompra:=A[i,11].MillasCompra + A[i,j].MillasCompra
        A[i,11].MillasCant:=A[i,11].MillasCant + 1

        Leer(VIAJE,reg)

    FinMientras

    Min1:=HV;Min2:=HV
    Max:=LV
    Para i:=1 hasta 3 Hacer

        Si A[i,11].MillasCompra < Min1 Entonces
            Min1:=A[i,11].MillasCompra
            CuatrimMinita:=i
        FinSi

        Para j:=1 hasta 10 Hacer
            
            Si A[i,j].MillasCompra < Min2 Entonces
                Min2:=A[i,j].MillasCompra
                CuatrimMinita:=i
                OriginMinita:=j
            Sino
                Si A[4,j].MillasCompra > Max Entonces
                    CuatrimMaximus:=A[4,j].MillasCompra
                    OriginMaximus:=j
                Fin Si
            Fin Si
            
        Fin Para
    Fin Para
    Cerrar(VIAJE)
    Esc("El Cuatrimestre en el cual los clientes compraron la menor cantidad de millas es:",CuatrimMinita)
    Esc("El Origen en el cual los clientes compraron la mayor cantidad de millas es:",OriginMaximus)
    Esc("El Origen y Cuatrimeste en los cuales los clientes compraron la menor cantidad de millas son:",OriginMinita,CuatrimMinita)
FinAccion






            

