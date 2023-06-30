#MODELO !
accion urb es
    ambiente
        sec:Secuencias de caracteres;
        v1:caracter;

        sal_Par,sal_Impar:Secuencias de enteros;
        bandera:booleano;
        cont_1,cont_2,cont_3,cont_4,total_Mayo:Entero;
        porcen_1,porcen_2,porcen_3,porcen_4,total_local:Entero;
        
        funcion convertir(v:caracter):Entero es
            segun(v)hacer
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

        procedimiento verificar() es
            si(nro_ult mod 2 = 0) entonces
                bandera:= true;
            finsi
        finProcedimiento
    proceso
        arr(sec); avz(sec,v1);
        crear(sal_Impar); crear(sal_Par);
        bandera:= false;
        cont_1:=0;,cont_2:=0;,cont_3:=0;,cont_4:=0;,total_Mayo:=0;

        Mientras NDFS(sec) hacer
            Mientras( v1 <> "&") hacer
                #Avanzo nombre y apellido
                Mientras( v1 <> "-")hacer
                    avz(sec,v1);
                finMientas
                avz(sec,v1);

                #avanzo DNI ultimo digito verifico par o impar.
                para i= 1 hasta 9 hacer 
                    si (i = 8 )entonces
                        nro_ult:= convertir(v1);
                        verificar();
                    fisi
                    avz(sec,v1);
                finapara
                avz(sec,v1);

                segun (v1) hacer
                    "1":cont_1:= cont_1 + 1:
                    "1":cont_2:= cont_2 + 1:
                    "1":cont_3:= cont_3 + 1:
                    "1":cont_4:= cont_4 + 1:
                finsi
                avz(sec,v1);
                avz(sec,v1);

                #copio nro tramites en la sec salida.
                si(bandera) entonces
                    Mientras( v1 <> "-") hacer
                        Esc(sal_Par,v1);
                        avz(sec,v1);
                    finMientas
                    Esc(sal_Par,"#");
                sino
                    Mientras( v1 <> "-") hacer
                        Esc(sal_Impar,v1);
                        avz(sec,v1);
                    finMientas
                    Esc(sal_Impar,"#");
                finsi
                avz(sec,v1);

                para i:=1  hasta 9 hacer
                    si(i=4) y (v1= "5")entonces
                        total_Mayo:= total_Mayo + 1;
                    finsi
                     avz(sec,v1);
                finapara
            finMientas
            avz(sec,v1);
        finMientas
        total_local:=(cont_1+cont_2+cont_3+cont_4);
        porcen_1:=(cont_1*100)/total_local;
        porcen_2:=(cont_2*100)/total_local;
        porcen_3:=(cont_3*100)/total_local;
        porcen_4:=(cont_4*100)/total_local;

        Esc("El total incriptos en Resistencia es", cont_1, "porcentaje es: ", porcen_1);
        Esc("El total incriptos en Barranqueras es", cont_2, "porcentaje es: ", porcen_2);
        Esc("El total incriptos en Vilelas es", cont_3, "porcentaje es: ", porcen_3);
        Esc("El total incriptos en Fontana es", cont_4, "porcentaje es: ", porcen_4);

        Esc("Cantidad de inscriptos en mayo es ", total_Mayo);
        cerrar(sec);cerrar(sal_Impar);cerrar(sal_Par);
finaccion
#MODELO 2
accion urb2 es
    ambiente
        sec,sec_sal1,sec_sal2:Secuencia de caracteres;
        v1,resg_loca:caracter;

        cont_1,cont_2,cont_3,cont_4,total_Gral:Entero;

        procedimiento almacenar() es
            segun(resg_loca)hacer
                "1": copiar_RyV();
                     cont_1:= cont_1 + 1;
                "2": copiar_ByF();
                     cont_2:= cont_2 + 1;
                "3": copiar_RyV();
                     cont_3:= cont_3 + 1;
                "4": copiar_ByF();
                     cont_4:= cont_4 + 1;    
            finsegun
        finProcedimiento

        procedimiento copiar_RyV() es
            Mientras(v1 <> "-") hacer
                Esc(sec_sal1,v1);
                avz(sec,v1);
            finMientas
            Esc(sec_sal1,"-")
            avz(sec,v1);

            para i:=1 hasta 8 hacer
                Esc(sec_sal1,v1);
                avz(sec,v1);
            finapara
            avz(sec,v1);
            Esc(sec_sal1,"&");
        finProcedimiento

        procedimiento copiar_ByF() es
            Mientras(v1 <> "-") hacer
                Esc(sec_sal2,v1);
                avz(sec,v1);
            finMientas
            Esc(sec_sal2,"-")
            avz(sec,v1);

            para i:= 1 hasta 8 hacer
                Esc(sec_sal2,v1);
                avz(sec,v1);
            finapara
            avz(sec,v1);
            Esc(sec_sal2,"&");
        finProcedimiento
    proceso
         cont_1:=0;,cont_2:=0;,cont_3:=0;,cont_4:=0;,total_Gral:=0;
         arr(sec);avz(sec,v1);
         crear(sec_sal1);crear(sec_sal2);

         Mientras NDFS(sec) hacer
            Mientras ( v1 <> "&") hacer

                para i:= 1 hasta 2 hacer
                    Mientras(v1 <> "-") hacer
                        avz(sec,v1);
                    finMientas
                    avz(sec,v1);
                finapara

                resg_loca:=v1;
                avz(sec,v1);
                avz(sec,v1);
                almacenar();
            finMientas
            avz(sec,v1);
        finMientas
        total_Gral:=(cont_1+cont_2+cont_3+cont_4);

        Esc("El total incriptos en Resistencia es", cont_1);
        Esc("El total incriptos en Barranqueras es", cont_2);
        Esc("El total incriptos en Vilelas es", cont_3);
        Esc("El total incriptos en Fontana es", cont_4);

        Esc("Cantidad de inscriptos total es ", total_Gral);
        cerrar(sec);cerrar(sal_Impar);cerrar(sal_Par);
finaccion
