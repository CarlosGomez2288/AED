Ejercicio 1.1.12
Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000,
y muestre como está compuesto (unidades, decenas y centenas) y si es múltiplo de 3
(Recordar: todo número cuya suma de sus dígitos sea múltiplo de 3, lo es también).

Acción 1.1.12 Es
Ambiente
    Num,Unidad,Decena,Centena: Numerico
Proceso
    Esc("Ingrese un número mayor a 100 y menor a 1000")
    Leer(Num)
    Si Num>100 y Num<1000 Entonces //346
        Unidad:=(Num MOD 100) MOD 10 //Unidad:=3
        Decena:=(Num MOD 100) DIV 10 // Decena:=23 div 10 //Decena:= 2
        Centena:=(Num MOD 100) // Centena:=23 mod 10// Centena:= 1
        Escribir("Su numero esta compuesto por",Unidad,Decena,Centena)
    FinSi
    Multiplo:=Unidad+Decena+Centena
    Si Multiplo MOD 3 = 0 Entonces
        Escribir("El numero es multiplo de 3")
    Sino 
        Escribir("El numero no es multiplo de 3")
    FinSi
FinAccion