Ejercicio 1.1.8
Escriba un algoritmo que permita conocer la edad de una persona,
con solo ingresar la fecha de nacimiento y la fecha actual, ambas en el formato: DIA, MES, AÑO

Acción 1.1.8 Es
Ambiente
    DÍA_N,MES_N,AÑO_N,AÑO_A,MES_A,DÍA_A: Numerico
Proceso
    Escribir("Ingrese la fecha de nacimiento de una persona")
    Leer(DÍA_N,MES_N,AÑO_N)
    Escribir("Ingrese la fecha actual")
    Leer(DÍA_A,MES_A,AÑO_A)
    Edad:= AÑO_A - AÑO_N
    Si (Mes_A < MES_N) Entonces// 2 de febrero y 3 de marzo, 
        Edad:= Edad-1
    Sino
        Si (Mes_N = MES_A) Entonces
            Si (DÍA_N < DÍA_A) Entonces
                Edad:= Edad-1
            FinSi
        FinSi
    FinSi
    Escribir("Su edad es:",Edad)
FinAccion
    
    
