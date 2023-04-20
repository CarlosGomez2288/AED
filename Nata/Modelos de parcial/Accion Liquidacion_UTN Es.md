Accion Liquidacion_UTN Es
Ambiente
    Novedades = Registro
        Leg:N(5)
        Cod_Novedad: N(8)
        Tipo_Novedad:
        Monto: N(15,2)
    Fin Registro
    NOVEDADES:archivo de Novedades ordenado por Leg y Cod_Novedad
    reg1:Novedades

    Empleados = Registro 
        Leg
        Nombre
        Cargo
        Basico
    Fin Registro
    EMPLEADOS:archivo de empleados indexado por Leg
    reg2:Empleados

    Sueldos = Registro
        Leg
        Mes
        Anio
        Cargo
        Neto_Cobrar
    Fin Registro
    SUELDOS:archivo de Sueldos indexado por Leg,Anio Y Mes
    reg3:Sueldos

    Fecha = Registro
        DIA:1..31
        MES:1..12
        ANIO:N(4)
    Fin Registro

    

Proceso
    Abrir E/(NOVEDADES);Leer(NOVEDADES,reg1)
    Abrir E/(EMPLEADOS);
    Abrir S/(SUELDOS);

    Esc("Legajo---Nombre---Cargo---Mes---Año---NetoCobrar")

    Mientras NFDA(NOVEDADES) hacer
        reg2.Legajo:=reg1.Clave.Legajo
        Leer(EMPLEADOS,reg2)
        Si existe entonces
            Esc("Ahora ingrese el mes actual y el año actual en formato mm/aaaa")
            Leer(Mes,Anio)
            aux.Legajo:=reg2.Legajo
            aux.Mes:=Mes
            aux.Anio:=Anio
            aux.Cargo:=reg2.Cargo
            totxD:=0
            totxNR:=0
            Mientras (reg1.Clave.Legajo = reg2.Legajo) hacer
                Si reg1.TipoNov = "D" entonces
                    totxD:=totxD+1
                Sino
                    totxNR:=totxNR+1
                FinSi
                Leer(NOVEDADES,reg1)
            FinMientras
            aux.NetoCobrar:=reg2.Basico - totxD + totxNR
            reg3:=aux
            GRABAR(SUELDOS,reg3)
        Sino
            Esc("El empleado no existe")
        FinSi
        





