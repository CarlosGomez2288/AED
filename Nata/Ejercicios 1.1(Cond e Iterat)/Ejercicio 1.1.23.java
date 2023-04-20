Ejercicio 1.1.23
Escriba un algoritmo para calcular cada renglón de una factura (valor unitario * cantidad vendida) y el total de la misma,
suponiendo que el número de renglones es variable. Emitir un mensaje de error si el valor unitario es <= 0.
Realizar la prueba de escritorio con los siguientes valores: Cantidad de renglones: 4

Valor Unitario	Cantidad Vendida
    2	                10
    1	                25
    3	                15
    2	                8.5

Accion 1.1.23 Es
Ambiente
    VU,CV,Total,SubT:real
    renglones:entero
Proceso
    Escribir("Ingrese la cantidad de renglones de la factura")
    Leer(renglones)
    Total
    Para i:=1 hasta renglones Hacer
        Escribir("Ingrese el valor unitario y la cantidad vendida")
        Leer(VU,CV)
        Si VU<=0 Entonces
            Escribir("Error")
        Sino
            SubT:=VU*CV
        FinSi
        Total:=Total+SubT
    FinPara
    Escribir("El total de la factura es:",Total)
FinAccion



        