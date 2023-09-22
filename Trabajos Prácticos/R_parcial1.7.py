accion becas es
    ambiente
        sec1,sal:secuencia de caracteres;
        sec2:secuancia de enteros;
        v_sec1:caracter;
        v_sec2:entero;

        ban_sex,ban_parPrimer,ban_parUlt,ban_imparPrimer,ban_imparlt,bandera:booleano;

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
        finfuncion

        procedimento cuit() es
            aux:=convertir(v_sec1);
            si(resg_sex = "F")entonces
                Esc(sal,"7");
            sino
                Esc(sal,"0");
            finsi

            para i= 1 hasta 7 hacer 
                si(bandera)entonces
                    Esc(sal,v_sec1);
                finsi
                avz(sec1,v_sec1);
            finpara

            Si((aux mod 2 = 0) y (convertir(v_sec1) mod 2 = 0)) Entonces
                Escribir(Sal, "1")
            finsi

            Si((aux mod 2 <> 0) y (convertir(v_sec1) mod 2 = 0)) Entonces
                Escribir(Sal, "2")
            finsi

            Si((aux mod 2 = 0) y (convertir(v_sec1) mod 2 <> 0)) Entonces
                Escribir(Sal, "3")
            finsi

            Si((aux mod 2 <> 0) y (convertir(v_sec1) mod 2 <> 0)) Entonces
                Escribir(Sal, "4")
            finsi
        finProcedimiento

        procedimento Copiar() es
            Mientras ( v_sec1<> "|") hacer
                si(bandera) entonces
                    Esc(sal,v_sec1);
                finsi
                avz(sec1,v_sec1);
            finmientras
        finmientras
    proceso
        arr(sec1); avz(sec1,v_sec1);
        arr(sec2); avz(sec2,v_sec2);
        crear(sal);
        bandera,ban_sex,ban_par,ban_impar:=false;

        Mientras NDFS(sec1) hacer
            total:=total + 1;
            Mientras ( v_sec1 <> "$") hacer

                si(convertir(v_sec1) > 10000) entonces
                    contCumple:=contCumple + 1;
                    bandera:=true;
                sino
                    contNCumple:=contNCumple + 1;
                finsi

                Mientras ( v_sec1<> "|") hacer
                    si(bandera) entonces
                        Esc(sal,v_sec1);
                    finsi
                    avz(sec1,v_sec1);
                finmientras
                avz(sec1,v_sec1);

                resg_sex:=v_sec1;
                
                avz(sec1,v_sec1);
                avz(sec1,v_sec1);

                cuit();
                avz(sec1,v_sec1);

                Copiar();

                Mientras ( v_sec1 <> "$") hacer
                    avz(sec1,v_sec1);
                finmientras
            finmientras
            Esc(sal,"$");
            avz(sec1,v_sec1);
            avz(sec2,v_sec2)
        finmientras
        Esc("El porcentaje que cumplieron"(toal/contCumple)*100);
        Esc("El porcentaje que no cumplieron"(toal/contNCumple)*100);
finaccion