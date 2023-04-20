Ejercicio 1.1.30

Escriba un algoritmo para resolver el siguiente problema:
Una empresa de transportes desea conocer el sueldo de sus 100 choferes.
Estos se calculan teniendo en cuenta la categoría (1 o 2) y la asistencia (perfecta: si o no).
El sueldo se obtiene sumando el sueldo básico, más el 2% de antigüedad por cada año trabajado y $200 de premio por asistencia.
El sueldo básico es de $700 para choferes de categoría 1 y de $500.- para los de categoría 2.

Accion 1.1.30 Entonces
Ambiente
    Sueldo: real
    antigüedad: entero
    Cat,Asist: alfanumerico
    Sueldo1= 700
    Sueldo=500
Proceso
    Para i:=1 hasta 100,1 hacer
        Escribir("Ingrese la categoria")
        Leer(Cat)
        Si (Cat = "1") Entonces
            Escribir("Ingrese si el conductor tiene asistencia perfecta")
            Leer(Asist)
            Si (Asist = "Si") Entonces
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad) //15
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))+200 //
            Sino
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))
            FinSi
        Sino
            Escribir("Ingrese si el conductor tiene asistencia perfecta")
            Leer(Asist)
            Si (Asist = "Si") Entonces
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo2+(Sueld2*(antiguedad*0.02))+200
            Sino
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))
            FinSi
        FinSi
    FinPara
FinAccion

o

Proceso
    Para i:=1 hasta 100,1 hacer
        Escribir("Ingrese la categoria")
        Leer(Cat)
        Si (Cat = "1") Entonces
            Escribir("Ingrese si el conductor tiene asistencia perfecta")
            Leer(Asist)
            Si (Asist = "Si") Entonces
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad) //15
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))+200 //
            Sino
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))
            FinSi
        Sino
            Escribir("Ingrese si el conductor tiene asistencia perfecta")
            Leer(Asist)
            Si (Asist = "Si") Entonces
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo2+(Sueld2*(antiguedad*0.02))+200
            Sino
                Escribir("Ingrese la antiguedad del conductor")
                Leer(antiguedad)
                Sueldo:=Sueldo1+(Sueld1*(antiguedad*0.02))
            FinSi
        FinSi
    FinPara
FinAccion


