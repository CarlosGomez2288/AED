Ejercicio 1.1.13
escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000 que representa una suma de dinero
e indique cuantos billetes de cada denominación necesita, suponiendo que solo existen billetes de 100, 10 y 1 peso.

Acción 1.1.13 Es
Ambiente
    CIEN,DIEZ,UNO,DINERO: Numerico
Proceso
    Esscribir("Ingrese la suma de dinero que sea mayor a 100 y menor a 1000")
    Leer(DINERO)
    Si DINERO >100 y <1000 Entonces
        CIEN:=DINERO DIV 100
        DIEZ:=(DINERO MOD 100) DIV 10
        UNO:=(DINERO MOD 100) MOD 10
    FinSi
    Escribir("La cantidad de billetes de a 100 es:",CIEN,", los de 10 son:",DIEZ,"y los billetes de a 1 serán:",UNO)
FinAccion

o tambien

Proceso
    Esscribir("Ingrese la suma de dinero que sea mayor a 100 y menor a 1000")
    Leer(DINERO)
    Si DINERO >100 y <1000 Entonces
        UNO:=DINERO MOD 10
        DIEZ:=(DINERO MOD 100) - UNO
        CIEN:=DINERO DIV 100
    FinSi
    Escribir("La cantidad de billetes de a 100 es:",CIEN,", los de 10 son:",DIEZ,"y los billetes de a 1 serán:",UNO)
FinAccion
