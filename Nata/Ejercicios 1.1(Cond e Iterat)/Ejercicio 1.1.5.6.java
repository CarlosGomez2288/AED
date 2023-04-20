Ejercicio 1.1.5.6
Realizar un programa que lea dos número complejos, 
(
a
,
b
)
 y 
(
c
,
d
)
, y calcule su producto:

(
a
,
b
)
∗
(
c
,
d
)
=
(
a
c
−
d
b
,
a
d
+
b
c
)

Accion 1.5.6 Es
Ambiente
    a,b,c,d,Pr1,Pr2: real
Proceso
    Escribir("Ingrese el primer coeficiente real")
    Leer(a)
    Escribir("Ingrese el primer coeficiente imaginario")
    Leer(b)
    Escribir("Ingrese el segundo coeficiente real")
    Leer(c)
    Escribir("Ingrese el segundo coeficiente imaginario")
    Leer(d)
    Pr1:=a*c-d*b
    Pr2:=a*d+b*c
    Escribir("El producto de un numero complejo es:(";Pr1;",";Pr2;")")
FinAccion
