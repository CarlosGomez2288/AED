Accion 2.3.12b Es
Ambiente
    Fecha=registro
        dd: 1..31
        mm: 1..12
        aa: N(4)
    finregistro

    r1=registro
        DNI: N(8)
        NumCuenta: N(8)
        Crédito: N(10)
        UltCarga: Fecha
    finregistro
    reg1: r1
    ArchI1: archivo indexado de r1 ordenado por r1

    r2=registro
        DNI: N(8)
        Nombre: AN(100)
        FechaN: Fecha
        Telefono: AN(100)
        valido: booleano
    finregistro
    reg2: r2
    ArchI2: archivo indexado de r2 ordenado por r2

    r3=registro
        Clave=registro
            Nro: N(10)
            DNI: N(8)
        finregistro
        idservicio: N(10)
        Monto: N(2)
        FechaC: Fecha
    finregistro
    reg3: r3
    ArchS: archivo secuencial de r3 ordenado por Clave

    A: arreglo de [1..200] de entero
    i: entero

Proceso
    Abrir E/S(ArchI1)
    Abrir E/S(ArchI2)
    Abrir E/(ArchS);Leer(ArchS,reg3)
    Esc("Ingrese el precio del dolar");Leer(Precio)


    Mientras NFDA(ArchS) hacer
        reg2.DNI:=reg3.Clave.DNI
        Leer(ArchI2,reg2)
        Si existe entonces
            reg1.DNI:=reg2.Clave.DNI
            Leer(ArchI1,reg1)
            Si existe entonces
                reintegro:= 0; 
                Mientras NFDA(ArchS) y (reg3.Clave.DNI=reg1.DNI) hacer
                    Dolar:=(reg3.Monto/Precio)
                    Si (Dolar < 200) y (reg3.FechaC.mm >= 10 y reg3.FechaC.mm <=12) entonces
                        i:=reg3.idservicio
                        Si A[i] = 1 entonces
                            reintegro:= reintegro + reg3.monto; 
                            aux:= reg3.Fecha;
                        FinSi 
                    FinSi 
                    Leer (ArchS, reg3);
                FinMientras 
                reintegro:= reintegro * 0.5; 
                Si reintegro > 200000 entonces 
                    reg1.UltCarga.dd:=1
                    reg1.UltCarga.mm:=1
                    reg1.UltCarga.aa:=1999
                    reg2.valido:=Falso; 
                    Regrabar(ArchI2,reg2)
                sino 
                    reg1.Crédito:=reg1.Crédito+reintegro;
                    reg1.UltCarga:= aux;
                FinSi 
                Regrabar(ArchI1,reg1)
                ESC ("Para el usuario:", reg1.DNI,"se otorgo un credito de:", reintegro); 
            FinSi 
        FinSi 
    FinMientras
    Cerrar(ArchI1)
    Cerrar(ArchI2)
    Cerrar(ArchS)
FinAccion

Accion PUnto 2 Es
Ambiente
    Fecha=registro
        dd: 1..31
        mm: 1..12
        aa: N(4)
    finregistro

    r=registro
        DNI: N(8)
        FechaV: Fecha
        Provincia: N(2)
        Monto: N(10)
    finregistro
    reg: r
    Arch: archivo secuencial de r ordenado por DNI
    
    A: arreglo de [1..12,1..23] de dato
    i: entero
    Prom: real; acum/total

    dato=registro
        Cant: N(10)
        Monto: N(15,2)
    finregistro

Proceso
    Abrir E/(Arch);Leer(Arch,reg)
  

    Para i:=1 hasta 12 hacer
        Para j:=1 hasta 23 hacer
            A[i,j]:=0
        FinPara
    FinPara

    Mientras NFDA(Arch) hacer
        i:=reg.FechaV.mm
        j:=reg.Provincia

        A[i,j].Cant:=A[i,j].Cant+1
        A[i,j].Monto:=A[i,j].Monto + reg.Monto
        A[i,23].Cant:=A[i,23].Cant+1
        A[i,23].Monto:=A[i,23].Monto + reg.Monto
        A[12,j].Cant:=A[12,j].Cant+1
        A[12,j].Monto:=A[12,j].Monto + reg.Monto
        Leer(Arch,reg)
    FinMientras
    Cerrar(Arch,reg)

    Max:=LV;Min:=HV
    Para j:=1 hasta 23 hacer
        Prom:=0  
        Para i:=1 hasta 12 hacer
            Esc("Monto:",A[i,j].Monto,"Cantidad de viajes:",A[i,j].Cant)

            Si (A[i,j].Monto < Min) entonces
                Min:= A[i,j].Monto
            FinSi
            
            Si i=11 y A[11,j].Cant > Max entonces
                Max:=A[i,j].Cant
                x:=j
            FinSi
            Prom:=Prom+A[i,j].Monto
        FinPara
        Prom:=Prom/12
        Esc("El monto del mes",A[i],"es de:",Prom)
    FinPara
    Esc("El destino",x,"en el mes de Noviembre tuvó un monto de:",Max)
    Esc("El menor monto de credito de Destino por Mes es:",Min)
FinAccion

-----------------------------------------------------------------------
Accion 2.3.12a Es
Ambiente
    Fecha=registro
        dd: 1..31
        mm: 1..12
        aa: N(4)
    finregistro

    r1=registro
        DNI: N(8)
        NumCuenta: N(8)
        Crédito: N(10)
        UltCarga: Fecha
    finregistro
    reg1: r1
    ArchI1: archivo indexado de r1 ordenado por r1

    r2=registro
        DNI: N(8)
        Nombre: AN(100)
        FechaN: Fecha
        Telefono: AN(100)
        valido: booleano
    finregistro
    reg2: r2
    ArchI2: archivo indexado de r2 ordenado por r2

    r3=registro
        lave=registro
           Nro: N(10)
           DNI: N(8)
        inregistro
        dservicio: N(10)
        onto: N(2)
        echaC: Fecha
    finregistro
    reg3: r3
    ArchS: archivo secuencial de r3 ordenado por Clave

    A: arreglo de [1..200] de entero
    i: entero

Proceso
    Abrir E/S(ArchI1)
    Abrir E/S(ArchI2)
    Abrir E/(ArchS);Leer(ArchS,reg3)

    Mientras NFDA(ArchS) hacer
        reg2.DNI:=reg3.Clave.DNI
        Leer(ArchI2,reg2)
        Si existe entonces
            reg1.DNI:=reg2.Clave.DNI
            Leer(ArchI1,reg1)
            Si existe entonces
                reintegro:=0
                Mientras NFDA(ArchS) y (reg3.Clave.DNI=reg1.DNI) hacer
                    Si (reg3.FechaC.dd >= 01) y (reg3.Fecha.mm =7) y (reg3.FechaC <=9) entonces
                        i:=reg3.idservicio
                        Si A[i] = 1 entonces
                            reintegro:=reintegro+reg3.Monto
                            aux:=reg3.FechaC
                        FinSi
                    sino
                        Cont:=Cont+1
                    FinSi
                    Leer(ArchS,reg3)
                FinMientras
                reintegro:=reintegro/50
                Si reintegro < 100000 entonces
                    reg1.Crédito:=reintegro
                    reg1.UltCarga:=FechaC
                    Regrabar(ArchS,reg1)
                FinSi
            FinSi
        sino
            reg1.DNI:=reg3.DNI
            reg1.NumCuenta:=obtener_nrocuenta()
            reg1.Crédito:=0
            reg2.DNI:=reg3.DNI
            Grabar(ArchI1,reg1)
            Grabar(ArchI2,reg2)
            reintegro:=0
            Si (reg3.FechaC.dd >= 01) y (reg3.Fecha.mm =7) y (reg3.FechaC <=9) entonces
                i:=reg3.idservicio
                Si A[i] = 1 entonces
                    reintegro:=reintegro+reg3.Monto
                    aux:=reg3.FechaC
                FinSi
            sino
                Cont:=Cont+1
            FinSi
            Leer(ArchS,reg3)
            reintegro:=reintegro/50
            Si reintegro < 100000 entonces
                reg1.Crédito:=reintegro
                reg1.UltCarga:=FechaC
                Regrabar(ArchS,reg1)
            FinSi
        FinSi
    FinMientras
    Esc("El total de facturas que no cumplieron con el plazo son:",Cont)
    Cerrar(ArchI1)
    Cerrar(ArchI2)
    Cerrar(ArchS)
FinAccion

Accion PUnto 2 Es
Ambiente
    Fecha=registro
        dd: 1..31
        mm: 1..12
        aa: N(4)
    finregistro

    r=registro
        DNI: N(8)
        FechaV: Fecha
        Provincia: N(2)
        Monto: N(10)
    finregistro
    reg: r
    Arch: archivo secuencial de r ordenado por DNI
    
    A: arreglo de [1..12,1..23] de dato
    i: entero
    Prom: real; acum/total

    dato=registro
        Cant: N(10)
        Monto: N(15,2)
    finregistro
Proceso
    Abrir E/(Arch);Leer(Arch,reg)
    Prom:=0

    Para i:=1 hasta 23 hacer
        Para j:=1 hasta 12 hacer
            A[i,j]:=0
        FinPara
    FinPara

    Mientras NFDA(Arch) hacer
        i:=reg.Provincia
        j:=reg.FechaV.mm

        A[i,j].Cant:=A[i,j].Cant+1
        A[i,j].Monto:=A[i,j].Monto + reg.Monto
        A[i,23].Cant:=A[i,23].Cant+1
        A[i,23].Monto:=A[i,23].Monto + reg.Monto
        A[12,j].Cant:=A[12,j].Cant+1
        A[12,j].Monto:=A[12,j].Monto + reg.Monto
        Leer(Arch,reg)
    FinMientras
    Cerrar(Arch,reg)

    Max:=LV;Min:=HV
    Para i:=1 hasta 12 hacer
        Prom:=A[i,j].Monto
        Para j:=1 hasta 23 hacer
            Esc("Monto:",A[i,j].Monto,"Cantidad de viajes:",A[i,j].Cant)

            Si (A[i,j].Monto < Min) entonces
                Min:= A[i,j].Monto
            FinSi
            
            Si A[i]="Noviembre" y A[11,j].Monto > Max entonces
                Max:=A[i,j]
                x:=j
            FinSi

        FinPara
        Prom:=Prom/12
        Esc("El monto del mes",A[i],"es de:",Prom)
    FinPara
    Esc("El destino",x,"en el mes de Noviembre tuvó un monto de:",Max)
    Esc("El menor monto de credito de Destino por Mes es:",Min)
FinAccion











                





