Accion 2.3.14 Es
Ambiente
    Fecha=registro
        dd: 1..31
        mm: 1..12
        aa: N(4)
    finregistro

    r1=registro
        DNI: N(8)
        Millas: N(10)
        Ult_Carga: Fecha
    finregistro
    reg1: r1
    Index1: archivo indexado de r1 ordenado por r1

    r2=registro
        Clave=registro
            Origen: N(1)
            Destino: N(1)
        finregistro
        Millas: N(10)
        Duracion: N(2)
    finregistro
    reg2: r2
    Index2: archivo indexado de r2 ordenado por r2

Proceso
    Abrir E/S(Index1)
    Abrir E/(Index2)

    Esc("Desea realizar una operacion? si/no");Leer(Rta1)
    Mientras Rta1="si" hacer
        Esc("Seleccione el tipo de operacion: 1.Carga de millas-2.Venta de viaje);Leer(opcion1)
        Si opcion1 = "1" entonces
            Esc("Ingrese un DNI");Leer(DNI)
            reg1.DNI:=DNI
            Leer(Index1,reg1)
            Si existe entonces
                Esc("Cuantas millas desea cargar);Leer(Carga)
                reg1.Millas:=reg1.Millas+Carga
                reg1.Ult_Carga:=Fechasistema()
                Regrabar(Index1,reg1)
            Sino
                reg1.DNI:=DNI
                reg1.Millas:=Carga
                reg1.Ult_Carga:=Fechasistema()
                Grabar(Index1,reg1)
            FinSi
        Sino  
            Esc("Ingrese el Origen y destino del viaje");Leer(A,B)
            reg2.Clave.Origen:=A
            reg2.Clave.Destino:=B
            Esc("Ingrese la cantidad de millas del viaje"),Milla
            Si reg1.Millas > Millas entonces
                reg1.Millas:=reg1.Millas-Milla
            Sino
                esc("no posee las millas suficientes")
            FinSi
        FinSi
        Si reg1.Ult_Carga.mm = Fechasistema.mm() entonces
            
        Esc("Desea realizar una operacion? si/no");Leer(Rta1)


                
            
            



    