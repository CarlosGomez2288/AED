Ejercicio 1.1.31
Una fábrica textil produce telas de dos calidades distintas (primera y segunda) y de dos materiales distintos (seda y algodón).
Generar un algoritmo que calcule el peso de varias piezas de tela, el cual está dado por la suma del peso neto, más un porcentaje por el apresto,
más el peso del núcleo de cartón. Para realizar el cálculo, tener en cuenta la siguiente información, para cada pieza:

El peso del m2 y la longitud de cada pieza.
Al peso neto de la tela hay que sumarle un porcentaje por cada pieza, debido al apresto,
el cual es del 2% para las telas de seda y del 7% para las de algodón.
También se debe considerar el núcleo de cartón, que es de 400 gr. para los rollos de telas de primera y de 300 gr. en los de segunda.
Finalizar cuando la variable FIN sea igual a 'SI'.

Accion 1.1.31 Es
Ambiente
    calidad,material,FIN,Sum: alfanumerico
    peso,longitud,pesoN,pesotot:numerico
Proceso
    Escribir("Ingrese si desea realizar el calculo SI/NO")
    Leer(FIN)
    Mientras (FIN = "NO") Hacer
        Escribir("Ingrese la calidad de la tela: Primera/Segunda")
        Escribir("Ingrese el material de la tela: Seda/Algodón")
        
