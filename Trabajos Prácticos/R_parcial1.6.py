accion tickets es
    ambiente
        sec,sal:secuencias de caracteres;
        v,resg1:caracter;

        total,nro1,nro2.resul,cont_A,cont_C,cont_D:Entero;
        porce_A,porce_C,porce_D:real;

        funcion convertir(v1:caracter):entero es
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

        procedimiento transformar() es
            nro1:=convertir(v)*10;
            avz(sec,v);
            nro2:=convertir(v);
            resul:= nro1 + nro2;
        finprocedimiento

        procedimiento contar() es
            segun (v) hacer
                "A":cont_A:= cont_A + 1;
                "C":cont_C:= cont_C + 1;
                "D":cont_D:= cont_D + 1;
            finsegun
        finprocedimiento
    proceso
        total_A,total_C,total_D,total:=0:
        cont_A,cont_C,cont_D:=0;
        arr(sec); avz(sec,v); crear(sal);

        Esc("Ingresar horario 20 o 22");
        leer(datos);

        Mientras NFDS(sec) hacer
            Mientras ( v<> "#") hacer
                avz(sec,v);
            finMientras

            Mientras ( v<> "&") hacer
                total:=total + 1;
                Mientras ( v<> "!") hacer
                    avz(sec,v);

                    resg1:= v;
                    transformar();
                    si(datos = resul) entonces
                        Esc(sal,resg1);

                        para i = 1 hasta 12 hacer
                            Esc(sal,v);
                            avz(sec,v);
                        finpara

                        contar();

                        Mientras ( v<> "!") hacer
                            Esc(sal,v);
                            avz(sec,v);
                        finMientras
                    sino
                        para i = 1 hasta 12 hacer
                            avz(sec,v);
                        finpara

                        contar();

                        Mientras ( v<> "!") hacer
                            avz(sec,v);
                        finMientras
                    finsi
                finMientras
                avz(sec,v)
            finMientras
            avz(sec,v);
        finMientras
        porce_A:=(total/cont_A)*100;
        porce_C:=(total/cont_C)*100;
        porce_D:=(total/cont_D)*100;

        Esc("El total te tickets vendios es: "total);
        Esc("El total del sector  A es: "cont_A, "porcentaje",porce_A);
        Esc("El total del sector  C es: "cont_C_C, "porcentaje",porce_C);
        Esc("El total del sector  D es: "cont_D, "porcentaje",porce_D);
        cerrar(sec); cerrar(sal);
finaccion

accion ticketsV2 es
    ambiente
        sec_tic,sal:secuencias de caracteres;
        resg,v_tick,dato:caracter;
        tipo:{"A","C","D"}

        cont_A,cont_C,cont_D,total:Entero;
    proceso
        cont_A,cont_C,cont_D:=0,total:=0;
        arr(sec_tic); avz(sec_tic); crear(sal);

        Esc("Ingresar el oracion a buscar 0 (20:30) o 2(22:30)");
        leer(dato);
        Mientras NFDS(sec_tic) hacer
            Mientras ( v_tick <> "#")hacer
                avz(sec_tic,v_tick);
            finMientras
            avz(sec_tic,v_tick);

            Mientras ( v_tick <> "&") hacer
                total:=total + 1;
                Mientras( v_tick <> "!")hacer
                    bandera:=falso;
                    resg:=v_tick;
                    avz(sec_tic,v_tick);

                    si(dato = v_tick)entonces
                        bandera:=true;
                        Esc(sal,resg);
                    finsi

                    Mientras (no en tipo) hacer
                        si(bandera)entonces
                            Esc(sal,v_tick);
                        finsi
                        avz(sec_tic,v_tick);
                    finMientras

                    segun (v_tick) hacer
                        "A":cont_A:= cont_A + 1;
                        "C":cont_C:= cont_C + 1;
                        "D":cont_D:= cont_D + 1;
                    finsegun

                    Mientras ( v_tick <> "!")hacer
                        si(bandera)entonces
                            Esc(sal,v_tick);
                        finsi
                        avz(sec_tic,v_tick);
                    finMientras
                finMientras
                avz(sec_tic,v_tick);
            finMientras
            avz(sec_tic,v_tick);
        finMientras
        Esc("El total te tickets vendios es: "total);
        Esc("El total del sector  A es: "cont_A, "porcentaje",(total/cont_A)*100);
        Esc("El total del sector  C es: "cont_C_C, "porcentaje",(total/cont_C)*100);
        Esc("El total del sector  D es: "cont_D, "porcentaje",(total/cont_D)*100);
        cerrar(sec); cerrar(sal);
finaccion