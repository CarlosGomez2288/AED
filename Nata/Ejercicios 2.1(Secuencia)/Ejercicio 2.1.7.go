Ejercicio 2.1.7
Se tiene una secuencia de enteros que contiene todos los CUIT
de los empleados de una empresa, la misma termina con el CUIT 0.
Para evitar largas esperas en los días de pago,
la empresa necesita organizarlos de acuerdo
al último dígito de su documento,
generar una secuencia con los CUIT
de las personas que su número de documento termine con 0, 1, 2 o 3.

Acción 2.1.5 Es
Ambiente
    sec1,sec2:secuencia de enteros
    v1,v2,n,x: entero
    Rango={"0","1","2","3"}
Proceso
    ARR(sec1);AVZ(sec1,v1)  // (20445728595/20455728503/)
    Crear(sec2)
    Mientras v1<>"0" Hacer //20445728595
        n:=v1
        n:=n DIV 10
        x:=n mod 10
        Si x=Rango Entonces
            Esc(sec2,v2)
        Sino
            AVZ(sec2,v2)
        FinSi 
    FinMientras
    Cerrar(Sec1,v1);Cerrar(Sec2,v2)
FinAcción