Accion CallCenter Es
Ambiente

    Fecha=registro
        AA: N(4)
        MM: 1..12
        DD: 1..31
    finregistro

    reclamo = registro
        Clave=registro
            Region: N(2)
            CodRecl: N(10)
        finregistro
        FecRecl: Fecha
        MailCLiente: AN(20)
        Urgencia: An(1)
        Detalle: AN(100)
    finregistro
    reg1: reclamo
    Reclamos: archivo de reclamo ordenado por Clave

    reporte = registro
        Region: N(2)
        UltFecRecl: Fecha
        UrgAlta: N(6)
        UrgMedia: N(6)
        UrgBaja: N(6)
        NueAud: {"S","N"}
    finregistro
    reg2: reporte
    Reporte: archivo indexado de reporte indexado por Region

    A: arreglo de [20] ordenado por entero
    i: entero

Proceso

    Abrir E/(Reclamos);Leer(Reclamos,reg1)
    Abrir E/S(Reporte)

    Cont:=0
    Mientras NFDA(Reclamos) hacer
        reg2.Region:=reg1.Clave.Region
        Leer(Reporte,reg2)

        Si existe entonces
            i:=reg1.Clave.Region

            reg2.UltFecRecl:=reg2.FecRecl

            Según reg1.Urgencia hacer
                ="A":UrgAlta:= UrgAlta + 1
                ="M":UrgMedia:= UrgMedia + 1
                ="B":UrgBuja:= UrgBaja + 1
            Finsegún
            
            Si ((reg2.UrgAlta > (reg2.UrgBaja *2 )) y (A[i] < 10) y (reg2.NueAud = "N") entonces
                reg2.NueAud:="S"
                Cont:=Cont+1
            FinSi
            Regrabar(Reporte,reg2)
        Sino
            Esc("No se encotro la region")
        FInSi

        
        Leer(Reporte,reg2)
    FInMientras

    Cerrar(Reclamos); Cerrar(Reporte)
    Esc("La cantidad de veces que se modifico la auditoria son:",Cont)
FinAccion

-------------------------------------
Accion CallCenter2 Es
Ambiente
    Fecha=registro
        AA: N(4)
        MM: 1..12
        DD: 1..31
    finregistro

    reclamo = registro
        Clave=registro
            Region: N(2)
            CodRecl: N(10)
        finregistro
        FecRecl: Fecha
        MailCLiente: AN(20)
        Urgencia: An(1)
        Detalle: AN(100)
    finregistro
    reg1: reclamo
    ArchR: archivo de reclamo ordenado por Clave

    A: arrglo de [1..13,1..4] de entero
    i,j: entero

Proceso
    Abrir E/(ArchR);Leer(ArchR,reg1)

    Para:=1 hasta 13 hacer
        Para j:=1 hasta 4 hacer
            A[i,j]:=0
        FinPara
    FinPara

    Max:=LV;Cont:=0


    Mientras NFDA(ArchR) hacer
        i:=reg1.FecRecl.MM

        Según reg1.Urgencia hacer
        ="A":j:=1
        ="M":j:=2
        ="B":j:=3
        Finsegún

        A[i,j]:=A[i,j] + 1
        A[13,j]:=A[13,j] + 1
        A[i,4]:=A[i,4] + 1
        
        Leer(ArchR,reg1)
    FInMientras

    Cerrar(ArchR)

    Para i:=1 hasta 13 hacer
        Si A[i,4] > Max entonces
            Max:=A[i,4]
            x:=i
        FinSi
        Si A[i,2] < 10 enrtonces
            Cont:=Cont + 1
        FinSi
    FinPara
    Esc("En enero se registraron reclamos de urgencias de altas de:",A[1,1])
    Según x hacer
        =1:mes:="Enero"
        =2:mes:="Febrero"
        =3:mes:="Marzo"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
        =4:mes:="Abril"
    Finsegún
    Esc("El mes con mayor cantidad de reclamos es:",mes)
    Esc("La cantidad de reclamos registrados por Urgencia alta son:",A[13,1])
    Esc("La cantidad de reclamos registrados por Urgencia alta son:",A[13,2])
    Esc("La cantidad de reclamos registrados por Urgencia alta son:",A[13,3])
    Esc("La cantidad de meses donde se registraron una cantidad menos de 10 reclamos son:",Min)
    Cerrar(ArchR)
FinAccion




