accion bioqumica es
    ambiente
        sec_bio,sal:secuencias de caracteres;
        v_bio:caracter;


        promedio,total,cont_paciente:Entero;
        cont_A,cont_E,cont_I,nro,nro1,nro2:Entero;

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

        procedimiento transformar() es
            nro1:=convertir(v)*10;
            avz(sec_bio,v_bio);
            nro2:=convertir(v);
            nro:= nro1 + nro2;
        finprocedimiento
    proceso
        promedio:=0,total:=0,cont_paciente:=0,cant_estudio:=0;
        cont_A:=0;cont_E:=0;cont_I:=0;
        arr(sec_bio); avz(sec_bio,v_bio);
        crear(sal);

        Mientras NFDS(sec_bio) hacer
            cont_paciente:= cont_paciente + 1;
            Mientras ( v_bio<> "*") hacer
                segun ( v_bio) hacer
                    "A":cont_A:= cont_A + 300;
                    "E":cont_E:= cont_E + 420;
                    "I":cont_I:= cont_I + 670;
                finsegun
                resg_tipo:= v_bio;
                
                Mientras( v<> ",") hacer
                    avz(sec_bio,v_bio);
                finMientras

                avz(sec_bio,v_bio);
                transformar();
                Si(resg_tipo = "A")entonces
                    si(nro2 > 2) entonces
                        #copiar datos a la sec salida.
                    finsi
                finsi

                Mientras ( v<> "*") hacer
                    avz(sec_bio,v_bio);
                finMientras
            finMientras
            cant_estudio:= cant_estudio + nro;
            avz(sec_bio,v_bio);
        finMientras
        total:= (cont_A +cont_E + cont_I);
        promedio:= cant_estudio/cont_paciente;
        Esc("El total recaudado en el dia es: ",total);
        Esc("El promedio de estudio por paciente es: ",promedio);
        cerrar(sec_bio); cerrar(sal);
finaccion
accion corte es
    ambiente
        servicio = Registro
            clave = Registro
                suc:N(4);
                area:N(1);
                id_serv:N(6);
            finRegistro
            desc:AN(45);
            cant_cli:N(4);
            monto:N(6.2);
        finRegistro

        archi:archivo de servicios ordenados por clave;
        reg:servicio;

        cont_suc,cont_are,total_suc,cont_area1,total_area1:N(4);
        cant_noContrado,total_gral:N(4);
        porcentaje:(2.2);

        procedimiento corte_area() es
            Esc("El area", resg_area,"facturo un total",cont_are);
            cont_suc:= cont_suc + cont_are;
            total_area1:=total_area1 + cont_area1;

            Si( total_area1 > 2000000)entonces
                Esc("El area 1 supero el monto 2000000");
            finsi

            cont_are:=0;
            total_area1:=0;
            resg_area:reg.clave.area;
        finprocedimiento

        procedimiento corte_suc() es
            Esc("La sucursal", resg_suc,"facturo un total",cont_suc);
            total_gral:= total_gral + cont_suc;
            
            cont_suc:=0;
            resg_suc:reg.clave.suc;
        finprocedimiento

        resg_area:N(1);
        resg_suc:N(4);

    proceso
        abrir E/(archi); leer(archi,reg);

        resg_area:=reg.clave.area;
        resg_suc.=reg.clave.suc;

        Mientras NFDA(archi) hacer
            si( resg_suc <> reg.clave.suc)entonces
                corte_suc();
            sino
                si(resg_area <> reg.clave.area)entonces
                    corte_area();
                finsi
            finsi

            si(reg.cant_cli > 100) entonces
                cont_are.= cont_are + reg.monto;
            finsi

            si(reg.cant_cli <10)entonces
                cant_noContrado:= cant_noContrado + 1;
            finsi

            si(reg.clave.area = 1)entonces
                cont_area1:=cont_area1 + reg.monto
            finsi
            
            si(reg.clave.area = 1)entonces
                total_suc1:=total_suc1 + reg.monto;
            finsi
            leer(archi,reg);
        finMientras
        porcentaje:= (total_gral*0.20)
        
        Esc("El total facturado es: ",total_gral);
        Esc("La cantidad de contrataciones es ", cant_noContrado);

        si(total_suc1 > porcentaje) entonces
            Esc("El monto total de la sucursal 1 representa mas del 20%");
        sino
            si(total_suc1 < porcentaje)entonces
                Esc("El monto total de la sucursal 1 representa menor del 20%");
            finsi
        finsi
        cerrar(archi);
finaccion   