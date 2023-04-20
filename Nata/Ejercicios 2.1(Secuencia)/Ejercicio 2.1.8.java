Ejercicio 2.1.8
Teniendo en cuenta el ejercicio anterior,
se solicita que la secuencia de salida sea una secuencia de caracteres
y los CUIT se separen unos de otros con el caracter "-".

Accion 2.1.8 Es
Ambiente
    sec1,sec2:secuencia de enteros
    v1,v2,n,x: entero
    c:caracter
    Rango={"0","1","2","3"}
    Función caracter(v:entero):alfanumerico
        Según v Hacer   
        =0:caracter:="0";
        =1:caracter:="1";
        =2:caracter:="2";
        =3:caracter:="3";
        =4:caracter:="4";
        =5:caracter:="5";
        =6:caracter:="6";
        =7:caracter:="7";
        =8:caracter:="8";
        =9:caracter:="9";
        FinSegún
    FinFunción
Proceso
    ARR(sec1);AVZ(sec1,v1)  // (20445728595/20455728503/)
    Crear(sec2)
    Mientras v1<>"0" Hacer //20445728595
        n:=v1 //20445728595
        x:=n mod 10
        cont:=0
        Si x=Rango Entonces
            Mientras cont<=11 Hacer
                x:=n div 10 //2

                s:=caracter(x)
            FinMientras
            Esc(sec2,"-")
        FinSi
        Esc(sec2,v2)
        AVZ(sec1,v1) 
    FinMientras
    Cerrar(Sec1,v1);Cerrar(Sec2,v2)
FinAcción   