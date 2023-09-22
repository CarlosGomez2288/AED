accion parcial1.2 es
    ambiente
        sec:Secuenciasde de caracteres;
        v1,zona:caracter

        sal:Secuencias de enteros;

        bandera:Booleano
        cant_E,cant_P,_cant_Y,cont_reserva:entero
    proceso 
        arr(sec);avz(sec,v1);
        crear(sal);

        Esc("ingresar zona a buscar")
        leer(zona);

        Mientras NDFS(sec) hacer
            cont_reserva:= 0; cant_reserva:= 0;
            cant_E,cant_P,_cant_Y,cont_reserva:=0;
            bandera:=false;

            Mientras(v1 <> "@") hacer
                Mientras ( v1 <> "%")hacer
                    avz(sec,v1);
                finMientas
                avz(sec,v1);

                Mientras(v <> "#") hacer
                    avz(sec.v1);
                finMientas
                avz(sec,v1);

                segun ( v1) hacer
                    "E": cant_E:= cant_E + 1;
                    "P": cant_P:= cant_P + 1;
                    "Y": cant_Y:= cant_Y + 1;
                finsegun

                Mientras ( v1 <> "%") hacer
                    avz(sec,v1);
                finMientas
                avz(sec,v1);
            
                Mientras ( v <> "-") hacer
                    cant_reserva:= cant_reserva + 1;
                    si( v1 = zona) es
                        cont_reserva:= cont_reserva + 1;
                    finsi

                    para i:= 1  hasta 3 hacer 
                        avz(sec,v1); 
                    finapara

                finMientas
                avz(sec,v1);
            finMientas
            Esc(sal,cant_reserva);
            Esc("La cantida de reversa del tipo E", cant_E);
            Esc("La cantida de reversa del tipo P", cant_P);
            Esc("La cantida de reversa del tipo Y", cant_Y);
            Esc("La cantida de reserva en la zona ", zona, "es de: ", cont_reserva);
            avz(sec,v1);
        finMientasc
        cerrar(sal);cerrar(sec);
finaccion

##Corte
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
            nivel_hotel:1..5;
            cod_hotel:N(4);
            nom_hotel:AN(50);
            cant_habi:N(4);
        finRegistro

        archi_sal:archivo salida;
        reg_Sal:salida;

        cont_habi,cont_nivel, to_Gral:Entero

        procedimiento corte_nivel() es
            Esc("La cantidad hoteles con mas de 300 habitaciones del nivel ". res_nivel ," es ", cont_nivel);
            cont_cadena:= cont_cadena + cont_nivel;

            cont_nivel:= 0;
            resg_nivel:=reg.nivel_hotel;
        finProcedimiento

        procedimiento corte_cadena() es
            corte_nivel();
            Esc("La cantidad hoteles con mas de 300 habitaciones de la cadena ", resg_cadena, "es de ", cont_cadena);
            total_gral:= to_Gral + cont_cadena;
            
            cont_cadena:= 0;
            resg_cadena:=reg.cod_cadena;
        finProcedimiento

        procedimiento copiar() es
            reg_Sal.cod_cadena:=reg.cod_cadena;
            reg_Sal.nivel_hotel:=reg.nivel_hotel;
            reg_Sal.cod_hotel:=reg.cod_hotel;
            reg_Sal.nom_hotel:=reg.nom_hotel;
            reg_Sal.cant_habi:=reg.cant_habi;
            Esc(salida,reg_Sal);
        finProcedimiento

    proceso
        total_gral:=0,cont_cadena:=0,cont_nivel:=0;
        abrir E/(archi); leer(archi,reg);
        abrir S/(archi_sal);

        resg_cadena:=reg.cod_cadena;
        resg_nivel:=reg.nivel_hotel;


        Mientras NFDA(archi) hacer
            si(resg_cadena <> reg.cod_cadena) entonces
                corte_cadena();
            sino
                si(resg_nivel <> reg.nivel_hotel) entonces
                    corte_nivel();
                finsi
            finsi


            si(reg.es_ciud_sede = true) entonces
                si( reg.cant_habitacion > 300) entonces
                    cont_nivel := cont_nivel + 1;
                finsi
                copiar();
            finsi

            leer(archi,reg);
        finMientas
        corte_cadena();
        Esc("El total de hoteles con mas de 300 habitaciones  es: " total_gral);
        cerrar(archi);
        cerrar(archi_sal);
finaccion