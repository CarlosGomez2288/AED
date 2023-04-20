Accion 2.26 Es
Ambiente
    Energy=registro
        Nro_F: N(15)
        Nro_U: N(15)
        Zona={"ZonaA","ZonaB","ZonaC","ZonaD"}
        Fecha=registro
            AA: N(4)
            MM: 1..12
            DD: 1..31
        FinRegistro
        Consumo: N(15,2)
    FinRegistro
    Arch: Archivo de Enery Nro_F
    reg: Energy

    A: arreglo de [1..13,1..5] de Entero
    i,j: entero
    Result: real

Proceso
    Para i:=1 hasta 13 hacer
        Para j:=1 hasta 5 hacer
            A[i,j]:=0
        FinPara
    FinPara
    
    Mientras NFDA(Arch) hacer
        i:=reg.Fecha.MM
        Según reg.Zona hacer
            ="ZONA A":j:=1;Result:=reg.consumo*0,05
            ="ZONA B":j:=2;Result:=reg.consumo*0,07
            ="ZONA C":j:=3;Result:=reg.consumo*0,09
            ="ZONA D":j:=4;Result:=reg.consumo*0,13
        FinSegún
        A[i,j].Consumo:=A[i,j].Consumo + reg.Consumo
        A[i,j].Importe:=A[i,j].Importe + Result
        
        Leer(Arch,reg)
    FinMientras
    
    Esc("Mes  ZonaA  ZonaB  ZonaC  ZonaD  Tot x Mes")
    Para i:=1 hasta 13 Hacer
        Para j:=1 hasta 5 Hacer
        //Total x Mes //
        A[13,j].Consumo:=A[13,j].Consumo + A[i,j].Consumo
        A[13,j].Importe:=A[13,j].Importe + A[i,j].Importe
        // Total x Zona //
        A[i,5].Consumo:=A[i,5].Consumo + A[i,j].Consumo
        A[i,5].Importe:=A[i,5].Importe + A[i,j].Importe
        //Total General//
        A[13,5].Consumo:=A[13,5].Consumo + A[i,j].Consumo
        A[13,5].Importe:=A[13,5].Importe + A[i,j].Importe
        FinPara
    FinPara
FinAccion
