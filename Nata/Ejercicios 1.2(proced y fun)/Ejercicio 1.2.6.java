Ejercicio 1.2.6
Escribir una función que lea desde el teclado las unidades
y el precio de un producto que se quiere comprar, y en función
de las unidades introducidas calcule un descuento o no,
según corresponda: cuando las unidades excedan media docena
se aplicará 4% y el 10% cuando excedan la docena. La función
debe devolver como resultado el valor del descuento o cero,
en caso de que no corresponda.

Accion 1.2.6 Es
Ambiente
    Precio,Total:real
    Cantidad:entero
    Función Descuento (Unid:entero,Plata:real):numerico
        Según Unid Hacer
            <=6:Descuento:=0
            >6 o =12:Descuento:=(Plata*Unid)*0.04
            >12:Descuento:=(Plata*Unid)*0.1
        FinSegún
    FinFunción
Proceso
    Escribir("Ingrese la cantidad de productos")
    Leer(Cantidad)
    Escribir("Ingrese el precio de sus productos")
    Leer(Precio)
    Total:=(Precio*Cantidad) - Descuento(Precio,Cantidad)
    Escribir("El total final a pagar es:",Total)
FinAcción


