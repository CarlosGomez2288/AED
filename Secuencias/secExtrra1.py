accion 2.2.1 es
    ambiente
        sec1,sec2:secuencia de caracteres
        v:caracter

        contImpar,contpar,total,num:Entero;
        porcen:Real;
        numeros={"1","2","3","4","5","6","7","8","9"}
        funcion convertidor(cara:caracter):Entero es
            segun (cara) hacer
                "1":convertidor:= 1;
                "2":convertidor:= 2;
                "3":convertidor:= 3;
                "4":convertidor:= 4;
                "5":convertidor:= 5;
                "6":convertidor:= 6;
                "7":convertidor:= 7;
                "8":convertidor:= 8;
                "9":convertidor:= 9;
            de otro modo:
                Esc("Error");
            finsegun
        finfuncion

    proceso
        contpar:=0;contImpar:=0;total:=0;
        arr(sec1); crear(sec2); avz(sec1,v);

        Mientras NFDS(sec1) hacer #A125EB%

            si(v en numeros) Entonces
                num:=convertidor(v);
                total:= total + 1; 

                si(num mod 2 <> 0 ) entonces
                    Esc(sec2,v); 
                    contImpar:= contImpar + 1; 
                sino
                    contpar:= contpar + 1;
                finsi
            finsi
            avz(sec1,v); 
        finMientras
        Esc("El total es ",total);
        Esc("Porcentaje de Pares", total/contpar);
        Esc("Porcentaje de Impares", total/contImpar);
        cerrar(sec1);
        cerrar(sec2);
    finproceso
finaccion