Escribir un algoritmo que, dado un importe dinero, permia calcular e informar cuanto corresponde pagar por un impuesto,
en cuantas cuotas y el valor de las mismas. Tener en cuenta los siguientes datos:

IMPUESTO = 10% del importe dado.
Los importes mayores que $500 y menor o igual que $1000 se pagan en dos cuotas.
Los mayores de $1000 en tres cuotas. El algoritmo debe permitir tratar varios importes finalizando cuando se ingresa 9999 como importe.

Accion 1.1.24 Es
Ambiente
    importe,impfrac: real
Proceso
    Mientras (importe<9999) hacer
        importe:=0;impfrac:=0
        Escribir("Ingrese un importe de dinero");Leer(importe)
        Si importe =>500 y importe < 1000 Entonces
            impfrac:=(importe*1.10)/2
            Escribir("Debera pagar un importe en 2 cuotas de:",impfrac)
        Sino
            Si importe>1000 Entonces
                impfrac:=(importe*1.10)/3
                Escribir("Debera pagar un importe en 3 cuotas de:",impfrac)
            FinSi
        FinSi
    FinMientras
FinAccion

