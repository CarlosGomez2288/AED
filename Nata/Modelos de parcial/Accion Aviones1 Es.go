Accion Aviones1 Es
Ambiente
    Flota=registro
        CodF
        Vigente:{"SI","NO"}
        CodEstado
        KmR
    finregistro
    reg1,act:= Flota
    MAE,SAL: archivo de CodF ordenado por CodF


    FlotaMov=registro
        CodF
        KmR
        CodEstado
    finregistro
    reg2: FlotaMov
    MOV: archivo de FlotaMov ordenado por CodF

Proceso
    Abrir E/(MAE);leerMAE
    Abrir E/(MOV);leerMOV
    Abrir S/(SAL)

    Total:=0;Cont2:=0;Cont3:=0;Cont4:=0
    Mientras (reg1.CodF<>HV o reg2.CodF<>HV) hacer
        Si reg1.CodF < reg2.CodF entonces
            act:=reg1
            Según reg2.CodEstado hacer
                =1: act.CodEstado:= "2"
                    Cont2:=Cont2+1
                =2: act.KmR:= act.KmR + reg2.KmR
                        act.Vigente:= "SI"
                        act.CodF:=reg2.CodF
                        Cont2:=Cont2+1
                =3: act.Vigente:= "SI"
                        act.KmR:= reg2.KmR
                        act.CodF:=reg2.CodF
                        Cont3:=Cont3+1
                =4: act.Vigente:= "NO"
                        Cont4:=Cont4+1
             FinSegún
            Grabar(SAL,act)
            leerMOV
        Sino
            Si reg1.CodF = reg2.CodF entonces
                Según reg2.CodEstado hacer
                    =2: act.KmR:= act.KmR + reg2.KmR
                        act.Vigente:= "SI"
                        act.CodF:=reg2.CodF
                        Cont2:=Cont2+1
                    =3: act.Vigente:= "SI"
                        act.KmR:= reg2.KmR
                        act.CodF:=reg2.CodF
                        Cont3:=Cont3+1
                    =4: act.Vigente:= "NO"
                        Cont4:=Cont4+1
                FinSegún
                Grabar(SAL,act)
                leerMAE
                leerMOV
            Sino
                act:=reg1
                Si CodEstado = "1" entonces
                    act.CodF:=reg1.CodF
                    act.Vigente:= "Si"
                    CodEstado:= "2"
                    act.KmR:=0
                    Cont2:=Cont2+1
                    Grabar(SAL,act)
                    leerMOV
                FinSi
                leerMAE
            FinSi
        FinSi
        Total:=Total+1
    FinMientras
    P2:=(Cont2*100)/Total
    P3:=(Cont3*100)/Total
    P4:=(Cont4*100)/Total
    Esc("El porcentaje de aviones de estado 2 son:",P2)
    Esc("El porcentaje de aviones de estado 3 son:",P3)
    Esc("El porcentaje de aviones de estado 4 son:",P4)
    Cerrar(MAE);Cerrar(MOV);Cerrar(SAL)
FinAccion

------------------------------------------------------

               