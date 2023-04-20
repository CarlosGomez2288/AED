Accion 3.31 Es
Ambiente
    A: Arreglo de [1..7,1..6,1..2,1..7] de Entero
    i,j,k,l: entero
    PA:{"P1","P2","P3","P4","Blanco","Indeciso","Otro"}
    PV:{"P1","P2","P3","P4","Blanco","Indeciso","Otro"}
    Edad:N(3)
    Sexo:{"Femenino","Masculino"}
    reg: Partido
    Arch: Archivo de Partido 

Proceso
    Para l:=1 hasta 7 hacer
        Para k:=1 hasta 2 hacer 
            Para j:=1 hasta 6 hacer
                Para i:=1 hasta 7 hacer
                    A[i,j,k,l]:=0
                FinPara
            FinPara
        FinPara
    FinPara
    Esc("Quiere ingresar datos?" SI/NO)
    Mientras (Rta = "SI") hacer 
        Esc("Partido al que votara");Leer(PA)
        Segun PA Hacer
            ="P1":i:=1
            ="P2":i:=2
            ="P3":i:=3
            ="P4":i:=4
            ="Otro":i:=5
            ="En Blanco":i:=6
            ="Indeciso":i:=7
        Fin Segun

        Esc("Ingrese la edad del votatante");Leer(Edad)
        Según Edad hacer
            <26:j:=1
            <36:j:=2
            <46:j:=3
            <56:j:=4
            <66:j:=5
            =>66:j:=6
        FinSegún

        Esc("Ingrese el sexo del votante");Leer(Sex)
        Si (Sex = Masculino) Entonces
            k:=1
        Sino
            k:=2
        FinSi

        Esc("Ingresé el partido al cual voto")
        Leer(PV)
        Segun PV Hacer
            ="P1":i:=1
            ="P2":i:=2
            ="P3":i:=3
            ="P4":i:=4
            ="Otro":i:=5
            ="En Blanco":i:=6
            ="Indeciso":i:=7
        Fin Segun
        Esc("Desea cargar nuevos datos? SI/NO");Leer(Rta)
    FinMientras

    Esc("Partido al que votara");Leer(PA)
    Esc("Ingrese la edad del votatante");Leer(EdadBusq)
    Esc("Ingrese el sexo del votante");Leer(SexBusq)
    Esc("Ingresé el partido al cual voto");Leer

    Para l:=1 hasta 7 hacer
        Para k:=1 hasta 2 hacer 
            Para j:=1 hasta 6 hacer
                Para i:=1 hasta 7 hacer
                    Segun (Edadbusq) Hacer
                        Edadbusq <26:Edadbusq:=1
                        Edadbusq <36:Edadbusq:=2
                        Edadbusq <46:Edadbusq:=3
                        Edadbusq <56:Edadbusq:=4
                        Edadbusq <=65:Edadbusq:=5
                        Edadbusq >65:Edadbusq:=6
                    Fin Segun

                    Segun PA Hacer
                        ="P1":P:=1
                        ="P2":P:=2
                        ="P3":P:=3
                        ="P4":P:=4
                        ="Otro":P:=5
                        ="En Blanco":P:=6
                        ="Indeciso":P:=7
                    Fin Segun
                    //punto a
                    Si Edadbusq = j Entonces 
                        Si P = i Entonces
                            ContEPA1:=ContPA1 + 1
                        Fin Si
                        Si i <> l Entonces
                            ContEPA2:=ContEPA2 + 1
                        Fin Si
                    Fin Si

                    Si SexoBusq = "Masculino" Entonces
                        S:=1
                    Sino
                        S:=2
                    Fin Si

                    Si S = k Entonces
                        Si P = i Entonces
                            ContSPA1:=ContSPA1 + 1
                        Fin Si
                        Si i <> l Entonces
                            ContSPA2:=ContSPA2 + 1
                        Fin Si
                    Fin Si

                FinPara
            FinPara
        FinPara
    FinPara

FinAccion



