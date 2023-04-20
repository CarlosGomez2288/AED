Ejercicio 1.1.9
Una persona decide realizar un viaje a Europa, para lo cual necesita una determinada cantidad de euros.
La persona tiene ahorrada una cierta suma en dólares y desea saber si es suficiente y,
en caso de haber diferencia (de más o de menos) a cuantos pesos equivale. Realice un algoritmo que solucione el problema,
para lo cual deberá prever que se ingresen las equivalencias de monedas que considere necesarias (por ejemplo la cotizacion en pesos de dólar y/o del euro,
o a cuantos euros equivale un dólar).

Acción 1.1.9 Es
Ambiente
    DolarCot,EuroDolar,DolarEuro,CantDolar,Dolares,Resultado,diferencia: numericos
Proceso
    Esc("Ingrese la cotización del euro actual en pesos")
    Leer(EuroPeso)
    Esc("Luego ingrese la cotización del euro en dolares")
    Leer(EuroDolar)
    Esc("Ingrese la cantidad de dolares necesarios")
    Leer(CantDolar)
    Esc("Ingrese la cantidad de dolares DISPONIBLES")
    Leer(Dolares)
    Resultado:=Dolares*EuroDolar
    Si Resultado = CantDolar Entonces
        Esc()
    Sino
        Si Resultado > CantDolar Entonces
            Diferencia:=(Resultado-CantDolar)*EuroPeso //100*
            Esc()
        Sino
            Diferencia:=(CantDolar-Resuultado)*EuroPeso
            Esc()
        FinSi
    FinSi
FinAcción
     //


        
