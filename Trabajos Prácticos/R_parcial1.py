accion parcial1 es
    ambiente
        sec,sal:Secuencias de caracteres:
        v1 tipo_Reserva:caracter
        nro1,nro2,nro:Entero
        to_reserva, pocentaje:Entero

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

        procedimiento transfomar() es
            nro1:convertir(v1) * 10
            avz(sec,v1);
            nro2:=convertir(v1);
            nro:=(nro1 +nro2)*1000;
            avz(sec,v1);
        finProcedimiento
    proceso
        nro1:=0;nro2:=0;nro:=0;to_reserva:=0;
        arr(sec); avz(sec, v1);
        crear(sal);

        Esc("Ingrear el tipo de reserva a buscar E-P-Y");
        leer(tipo_Reserva);

        Mientras NDFS(sec) hacer
            Mientras( v1 <> "@") hacer

                Mientras ( v1 <>"%") hacer
                    Esc(sal,v1);
                    avz(sec,v1);
                finMientas 
                avz(sec,v1);

                transfomar();
                avz(sec,v1);
                
                si(tipo_Reserva = v1) entonces
                    bandera:=true;
                finsi

                Mientras(v1<> "%") hacer
                    avz(sec,v1);
                finMientas
                avz(sec,v1);

                Mientras ( v <> "_") hacer
                    cont_reservas:= cont_reservas + 1;
                    para i:= 1 hasta 3 hacer 
                        si(banera)entonces
                            Esc(sal,v1); 
                        finsi
                        avz(sec,v1); 
                    finapara
                FinMientas
                avz(sec,v1);
            finMientas
            Esc(sal,"@"); 
            porcentaje:= (cont_reservas*100)/nro;
            Esc("La cantidad total de reservas es: "cont_reservas);
            Esc("El porcentaje de ocupacion es: ", porcentaje);
            avz(sec,v1);
        finMientas
        cerrar(sec);
        cerrar(sal);
finaccion

#Version 2 
accion parcial1 es
    ambiente
        sec,sal:Secuencias de caracteres:
        v1 tipo_Reserva:caracter

        nro1,nro2,nro:Entero
        to_reserva, pocentaje:Entero
        bandera:Booleano

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

        procedimiento transfomar() es
            nro1:convertir(v1) * 10
            avz(sec,v1);
            nro2:=convertir(v1);
            nro:=(nro1 +nro2)*1000;
            avz(sec,v1);
        finProcedimiento
    proceso
        nro1:=0;nro2:=0;nro:=0;
        bandera:=falso;
        arr(sec); avz(sec, v1);
        crear(sal);

        Esc("Ingrear el tipo de reserva a buscar E-P-Y");
        leer(tipo_Reserva);

        Mientras NDFS(sec) hacer
            cont_reserva:=0;
            porcentaje:=0;
            Mientras( v1 <> "@") hacer

                Mientras ( v1 <>"%") hacer
                    Esc(sal,v1);
                    avz(sec,v1);
                finMientas 
                Esc(sal,"%")
                avz(sec,v1);

                transfomar();
                avz(sec,v1);
                
                si ( tipo_Reserva = v1) entonces
                    bandera:=verdadero;
                finsi

                Mientras(v1<> "%") hacer
                    avz(sec,v1);
                finMientas
                avz(sec,v1);

                cont_reservas:= cont_reservas + 1;

                para i:= 1 hasta 3 hacer
                    si(bandera)entonces
                        Esc(sal,v1);
                    finsi
                    avz(sec,v1);
                finapara

                si(bandera)entonces
                    Esc(sal,"@");
                finsi
            finMientas

            porcentaje:= (cont_reservas*100)/nro;
            Esc("La cantidad total de reservas es: "cont_reservas);
            Esc("El porcentaje de ocupacion es: ", porcentaje);
            avz(sec,v1);
        finMientas
        cerrar(sec);
        cerrar(sal);
finaccion
#Corte
accion corte es
    ambiente 
        Qatar = Registro
            cod_cadena:AN(15);
            nivel_hotel:1..5;
            cod_hotel:N(4);
            nom_hotel:AN(50);
            es_ciud_sede:{false,true};
            cant_habi:N(4);
        finRegistro

        archi:archivo Qatar ordenado por cod_cadena y nivel_hotel;
        reg:Qatar

        salida = Registro
            cod_cadena:AN(15);
            cant_habitacion:N(4);
        finRegistro

        archi_sal:archivo salida;
        reg_Sal:salida;

        cont_habi,to_Gral:Entero

        procedimiento corte_nivel() es
            Esc("La cantidad de habitaaciones del nivel ". res_nivel ," es ", cont_habi);
            cont_cadena:= cont_cadena + cont_habi;

            cont_habi:= 0;
            resg_nivel:=reg.nivel_hotel;
        finProcedimiento

        procedimiento corte_cadena() es
            corte_mivel();
            Esc("La cantidad de habitaaciones de la cadena ". resg_cadena ," es ", cont_cadena);
            total_gral:= to_Gral + cont_cadena;
            to_cadena:= to_cadena + cont_habi;

            cont_cadena:= 0;

            reg_Sal.cont_cadena:=resg_cadena;
            reg_Sal.cant_habi:= to_cadena:
            Esc(archi_sal,reg_Sal);
            to_cadena:=0;
            resg_cadena:=reg.cod_cadena;
        finProcedimiento

    proceso
        total_gral:=0,cont_cadena:=0;cont_habi:=0;to_cadena:=0;
        abrir E/(archi); leer(archi,reg);
        abrir S/(archi_sal);

        resg_cadena:=reg.cod_cadena;
        resg_nivel:=reg.nivel_hotel;

        Mientras NFDA(archi) hacer
            si(resg_cadena <> reg.cod_cadena) entonces
                corte_cadena();
            sino
                si(resg_nivel <> reg.nivel_hotel) entonces
                    corte_mivel();
                finsi
            finsi


            si(reg.es_ciud_sede = true) entonces
                cont_habi:= cont_habi + reg.cant_habitacion;
            finsi
            to_cadena:=to_cadena+ reg.cant_habitacion;
            leer(archi,reg);
        finMientas
        corte_cadena();
        Esc("El total de habitaciones de hotel es: " total_gral);
        cerrar(archi);
        cerrar(archi_sal);
finaccion