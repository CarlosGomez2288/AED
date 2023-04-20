Accion Preguntados Es
Ambiente
    PREG_NOV=registro


Proceso
    Abrir E/(PREGUNTADOS);LeerMae
    Abrir S/(Act)
    Abrir E/(PREG_NOV);leermov

    Mientras (reg1.Clave<>HV) o (reg2.Clave<>HV) hacer
        Si reg1.Clave < reg2.CLave entonces
            reg3:=reg1
            GRABAR(Act,reg3)
            leermov
        Sino
            Si reg1.Clave = reg2.CLave entonces
                Según reg2.Novedad hacer
                ="M":reg3:=reg1
                    reg3.Detalle:=reg2.Detalle
                    reg3.op1:=reg2.op1
                    reg3.op2:=reg2.op2
                    reg3.op3:=reg2.op3
                    reg3.op4:=reg2.op4
                    reg3.Resp:=reg2.Resp
                ="B":Esc("Se elimino la pregunta")
                ="A":Esc("N")
                FinSegún
                GRABAR(Act,reg3)
                LeerMae
                LeerMov
            Sino
                reg1.Clave:=reg2.Clave
                reg3.Detalle:=reg2.Detalle
                reg3.op1:=reg2.op1
                reg3.op2:=reg2.op2
                reg3.op3:=reg2.op3
                reg3.op4:=reg2.op4
                reg3.Resp:=reg2.Resp
                GRABAR(Act,reg3)
                LeerMov
            FinSi
        FinSi
    FinMientras
    CERRAR(PREGUNTADOS);CERRAR(PREG_NOV);CERRAR(Act)
FInMientras

                