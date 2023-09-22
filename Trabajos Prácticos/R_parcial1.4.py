accion ventas es
    ambiente
        sec_prod,sec_ventas,sal:Secuencias de caracteres;
        v_prod,v_ventas,talleMayor,resg_talle:caracter;

        cont_S,cont_M,_cont_L,cont_XL, nro1,nro2,nro2,resu1,resu2:Entero;

        funcion convertir(v:caracter):entero es
            segun (v) hacer
                "1":convertir:=1;
                "2":convertir:=2;
                "3":convertir:=3;
                "4":convertir:=4;
                "5":convertir:=5;
                "6":convertir:=6;
                "7":convertir:=7;
                "8":convertir:=8;
                "9":convertir:=9;
                "0":convertir:=0;
            finsegun
        finFuncion

        Procedimiento transDigito3() es
            nro1:=convertir(v_ventas)*100;
            avz(sec_ventas,v_ventas);
            nro2:=convertir(v_ventas)*10;
            avz(sec_ventas,v_ventas);
            nro3:=convertir(v_ventas);
            resu1:=(nro1+nro2+nro3);
            avz(sec_ventas.v_ventas);
        finProcedimiento

        Procedimiento transDigito2() es
            nro1:=convertir(v_ventas)*10;
            avz(sec_ventas,v_ventas);
            nro2:=convertir(v_ventas);
            resu2:=(nro1+nro2);
            avz(sec_ventas.v_ventas);
        finProcedimiento

        Procedimiento TratadoSec2() es
            resg_talle:=v_prod;
            avz(sec_prod,v_prod);

            transDigito2();

            segun (resg_talle) hacer
                "1":cont_S:=cont_S + resu2;
                "2":cont_M:=cont_M + resu2;
                "3":cont_L:=cont_L + resu2;
                "4":cont_XL:=cont_XL + resu2;
            finsegun

            avz(sec_ventas,v_ventas);
            transDigito3();
            avz(sec_ventas,v_ventas);

            total_monto:= resu1 * resu2;
            Mientras(v_ventas<>"!") hacer
                avz(sec_ventas,v_ventas);
            finMientas
        finProcedimiento
    proceso
        cont_S:=0;cont_M:=0;cont_L:=0;cont_XL:=0;
        nro1:=0;nro2:=0;nro2:=0;,nro:=0;
        arr(sec_prod); avz(sec_prod,v_prod);
        arr(sec_ventas); avz(sec_ventas,v_ventas);}
        crear(sal);

        Mientras NDFS(sec_prod) hacer
           Mientras(v_prod <> "&") hacer
                si(v_prod= "p") entonces

                    para i= 1 hasta 3 hacer
                        Mientras(v_prod <> "-")hacer
                            Esc(sal,v_prod);
                            avz(sec_prod,v_prod);
                        finMientas
                        Esc(sal,"-");
                        avz(sec_prod,v_prod);
                    finPara

                    TratadoSec2();
                sino
                    para i= 1 hasta 3 hacer
                        Mientras(v_prod <> "-")hacer
                            avz(sec_prod,v_prod);
                        finMientas
                        avz(sec_prod,v_prod);
                    finPara

                    TratadoSec2();
                finsi
           finMientas
           avz(sec_ventas,v_ventas);
           avz(sec_prod,v_prod);
        finMientas
        
        talleMayor = "S"

        Si cont_M > cont_S entonces
            talleMayor = "M"
        Fin Si

        Si (cont_L > cont_M) y (cont_L > cont_S) entonces
            talleMayor = "L"
        Fin Si

        Si (contadorD > cont_L) y (cont_XL > cont_M) y (cont_XL > cont_S) entonces
            talleMayor = "XL";
        Fin Si

        Esc("El talle con mas cantida de venta es: ", talleMayor);

        cerrar(sec_prod); cerrar(sec_ventas); cerrar(sal);
finaccion