Ejercicio 1.2.4
Elaborar una función que reciba un número entero
y retorne -1 si el número es negativo. 
Si el número es positivo debe devolver una clave calculada
de la siguiente manera: Se suma cada dígito que compone el número
y a esa suma se le calcula el modulo 7.
Por ejemplo:
para la cifra 513, la clave será 5+1+3 =9; 9 mod 7 = 2.
Utilice la función para diseñar un algoritmo que permita leer
varios valores y determine, para cada uno,
si el número leído fue negativo o, si fue positivo,
que clave le corresponde.

Accion1.2.4 Es
Ambiente
    n,Rta:entero
    Función Signo(Num:entero):entero
        Si Num<0 Entonces
            Sig:= -1
        Si Num>9 Entonces
            SumDig:=0
            Mientras Num>9 Entonces
                SumDig:=Num MOD 10
                Num:= Num Div 10
            FinMientras
            SumDig:= SumDig + Num
            Signo:= SumDig MOD 7
        Signo
            Signo:= Num MOD 7
        FinSi
    FinFunción
Proceso
    Escribir("Ingrese un numero")
    Leer(n)
    


