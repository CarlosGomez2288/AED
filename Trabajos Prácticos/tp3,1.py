accion play es
    ambiente
        playlis,canciones, sal:Secuencias de Caracter;
        vc,vp,resg_g,resg_M:carcater;

        cont_P,cont_E,cont_F,cont_R:Entero;
        nro1,nro2,nro3,nro:Entero;
        cont_play,cant_cancio,cant_M:Entero; 
        porce_R,porce_P,porce_E,porce_F:Entero

        funcion convertir(v:Caracter):Entero es
            segun (v) hacer
                "1":convertir:= 1;
                "2":convertir:= 2;
                "3":convertir:= 3;
                "4":convertir:= 4;
                "5":convertir:= 5;
                "6":convertir:= 6;
                "7":convertir:= 7;
                "8":convertir:= 8;
                "9":convertir:= 9;
                "0":convertir:= 0;
            finsegun
        finFuncion

        Procedimiento transformar() es
            nro1:=convertir(vp) * 100;
            avz(playlis,vp);
            nro2:=convertir(vp) * 10;
            avz(playlis,vp);
            nro3:=convertir(vp) ;
            nro:= nro1 + nro2 +nro3;
            avz(playlis,vp);
        finProcedimiento

        Procedimiento mayor() es 
            si ( cant_M < cant_cancio) entonces
                cant_M:= cant_cancio;
                resg_M:= resg_g;
            finsi
        finProcedimiento
    proceso
        cont_R:=0;cont_P:=0;cont_E:=0;cont_F:=0;
        nro1:=0;nro2:=0;nro3:=0;nro:=0;
        cont_play:=0,cant_cancio:=0;cant_M:=0; 
        porce_R:=0;porce_P:=0;porce_E:=0;porce_F:=0;

        arr(playlis); avz(playlis,vp);
        arr(canciones), avz(canciones,vc);
        crear(sal);

        Mientras NDFS(playlis) hacer
            cont_play:=cont_play + 1;
            resg_g:=vp;
            Mientras ( vp <> "?") hacer
                segun(vp) hacer
                    "R":cont_R:= cont_R + 1;
                    "P":cont_P:= cont_P + 1;
                    "E":cont_E:= cont_E + 1;
                    "F":cont_F:= cont_F + 1;
                finsegun

                si( vp = "R") entonces
                    Mientras ( vp <> "+") hacer
                        avz(playlis,vp);
                    finMientas
                    avz(playlis,vp);

                    Mientras( vp <> "+") hacer
                        Esc(sal,vp);
                        avz(playlis,vp);
                    finMientas
                    avz(playlis,vp);
                    Esc(sal,"+");

                    para i:= 1 hasta 3 hacer
                        Mientras ( vp <> "+") hacer
                            avz(playlis,vp);
                        finMientas
                        avz(playlis,vp);
                    finPara

                    transformar();

                    para i:= 1 hasta nro hacer
                        Mientras ( vc <> "/") hacer

                            Mientras (vc <> "#") hacer
                                Esc(sal,vc);
                                avz(canciones,vc);
                            finMientas

                            avz(canciones,vc);
                            Esc(sal,"+");

                            para i:= 1 hasta 2 hacer
                                Mientras ( vc <> "#") hacer
                                    avz(canciones,vc);
                                finMientas
                                avz(canciones,vc);
                            finPara

                            Mientras( vc <> "/")hacer
                                Esc(sal,vc);
                                avz(canciones,vc)
                            finMientas
                        finMientas
                        Esc(sal,"+");
                        avz(canciones,vc);
                    finPara
                    Esc(sal,"#");
                    cant_cancio:= cant_cancio + nro;
                    mayor();
                sino
                    avz(playlis,vp);

                    para i:= 1 hasta 4 hacer
                        Mientras ( vp <> "+") hacer
                            avz(playlis,vp);
                        finMientas
                        avz(playlis,vp);
                    finPara

                    transformar();
                    para i:= 1 hasta nro hacer
                        Mientras (vc <> "/") Hacer
                            avz(canciones,vc);
                        finMientas
                        avz(canciones,vc);
                    finPara
                    cant_cancio:= cant_cancio + nro;
                    mayor();
                finsi
            finMientas
            avz(playlis,vp);
        finMientas
        promedio:= cant_cancio / cont_play;
        porce_R:= cont_R*100/(cont_R + cont_P +cont_E+cont_F);
        porce_P:= cont_P*100/(cont_R + cont_P +cont_E+cont_F);
        porce_E:= cont_E*100/(cont_R + cont_P +cont_E+cont_F);
        porce_F:= cont_F*100/(cont_R + cont_P +cont_E+cont_F);

        ESC("los porcentajes de cada genero son: ROCK ", porcen_R, "POP ", porcen_P, "FOLKLORE", porcen_F, "ELECTRONICA", porcen_E)
        Esc("La cantidad promedio de la playlist es", promedio);
        Esc("El genero con mayor cantidad de canciones es ", resg_M);
        cerrar(sal);
        cerrar(playlis);
        cerrar(canciones);
finaccion