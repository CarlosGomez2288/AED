Ejercicio 1.1.11
Dado un año ingresado por el usuario,
emitir el mensaje 'ACTUAL' si corresponde al año en curso, 'PASADO' si es menor y 'FUTURO' si es mayor.

Acción 1.1.11 Es
Ambiente
    AñoI: numerico
Proceso
    Escribir("Ingrese un año que desee")
    Leer(AñoI)
    Según AñoI Hacer
        <: Escribir("PASADO")
        =: Escribir("ACTUAL")
        >: Escribir("FUTURO")
    FinSegún
FinAccion