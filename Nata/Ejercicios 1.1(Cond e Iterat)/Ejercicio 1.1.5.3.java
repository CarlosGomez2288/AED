Ejercicio 1.1.5.3
Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma de los precios de costos,
los porcentajes de ganancia del vendedor y un 21% de IVA. Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora.
Se leen los costos y se imprimen el precio total de ventas.

Accion 1.1.5.3 Es
Ambiente
    C_imp,C_pc,p_imp,p_pc,Total: entero
    IVA=1.21
    P_Imp=0,07
    P_pc=0,12
Proceso
    Escribir("Ingrese el precio de la impresora que desea comprar")
    Leer(C_Imp)
    Escribir("Ingrese el precio de la Pc que desea comprar")
    leer(C_pc)
    Total:=((C_pc+(P_pc*C_pc))+(C_imp+(P_imp*C_imp)))*IVA
    Escribir("El precio total de la impresora y pc es:",Total)
FinProceso

