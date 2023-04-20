Ejercicio 1.1.5.7
Escriba un algoritmo que halle la media geométrica de tres valores 
X,Y,Z. Este debe emitir los tres valores por separado y luego el valor medio. La media geométrica es igual a 
(X×Y×Z)/3

Accion 1.5.7 Es
Ambiente
    X,Y,Z,Media: Numerico
Proceso
    Escribir("Ingrese un valor")
    Leer(X)
    Escribir("Ingrese un segundo valor")
    Leer(Y)
    Escribir("Ingrese un último valor")
    Leer(Z)
    Media:=(X+Y+Z)/3
    Escribir("La media geometrica de los 3 valores",X,Y,Z,"es:";Media)
FinAccion
