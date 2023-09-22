accion t1 es
    ambiente
        sec_vf,sec_c,sal:secuencia de caracter;
        vf,vc:caracter;

        c_real,c_nreal:entero;

        funcion coventir(v:caracter):entero
            segun(v) hacer
                ="1":convertir():= 1;
                ="2":convertir():= 2;
                ="3":convertir():= 3;
                ="4":convertir():= 4;
                ="5":convertir():= 5;
                ="6":convertir():= 6;
                ="7":convertir():= 7;
                ="8":convertir():= 8;
                ="9":convertir():= 9;
                ="0":convertir():= 0;
            finsegun
        funcion
    proceso
    crear(sal)
    arr(sec_vf) arr(sec_c);
    avz(sec_vf,vf) avz(sec_c,vc);

    c_nreal:= 0;

    Mientras NFDS(sec_vf) hacer
        para i:= 1 hasta 10  hacer
            avz(sec_vf,vf);
        finpara

        para i:= 1 hasta 6 hacer 
            avz(sec_c,vc);
        finpara

        si(vc <> "#") entonces
            c_real:= 0;

            si(vf = "T") entonces
                Minetras ( vc <> "+") hacer
                    Esc(sal,vc)
                    avz(sec_c,vc);
                finmientras
                avz(sec_c,vc)
                Esc(sal,"+");

                Minetras ( vc <> "?") hacer
                    para i:= 1 hasta 8 hacer 
                        Esc(sal,vc); 
                        avz(sec_c,vc);
                    finpara
                    Esc(sal,"+");

                    Mientras ( vc <> ".") hacer
                        avz(sec_c,vc);
                    finmientras
                    avz(sec_c,vc);
                    c_real:= c_real + 1
                finmientras
            sino
                Mientras ( vc <> "?") hacer
                    Minetras(vc <> ".") hacer
                        avz(sec_c,vc);
                    finmientras
                    avz(sec_c,vc);
                    c_real:= c_real + 1;
                finmientras
                avz(sec_c,vc);
            finsi
            avz(sec_vf,vf);

            si ( c_real <> convertir(vf)) entonces
                c_nreal:= c_nreal + 1;
            finsi
        sino
            avz(sec_vf,vf);
            avz(sec_vf,vf);
            avz(sec_c,vc);
            avz(sec_c,vc);
        finsi
    finmientras
    Esc("la cantidad de usuario que compraron una cantidad distinta a la desclarada son : " c_nreal);
finaccion


ACCION ejercicio2_T1 ES
    AMBIENTE
        formato_fecha = REGISTRO
            aaaa: N(4)
            mm: N(2)
            dd: N(2)
        finreg

        VENTAS = REGISTRO
            CLAVE = REGISTRO
                prov: AN(20)
                ciudad: AN(20)
                plat: AN(10)
                fecha: formato_fecha
            finreg
            ntradas: N(2)
        finreg

        reg: VENTAS
        arch: ARCHIVO de VENTAS ordenado por CLAVE

        SALIDA = REGISTRO
            prov: AN(20)
            ciudad: AN(20)
            entradas: N(4)
        fin_reg

        reg_sal : SALIDA
        ar_sal: ARCHIVO de SALIDA
        //se podria interpretar que cantidad de ventas es o el total de entradas vendidas o de
        transacciones de venta (contar registro)
        totgral, tot_plat, tot_ciudad: entero
        //para consigna a:
        cont_entradas: entero
        resg_prov, resg_plat, resg_ciudad: alfanumerico
        //defino del corte mas chiquito al mas grande (porque los mas grandes llaman al mas chico)
        PROCEDIMIENTO Corte_plataforma() es
            ESC("En la plataforma: ", resg_plat, "Total de ventas del 1 de julio al 1 de junio es:",
            tot_pplat)
            tot_ciudad:= tot_plat + tot_ciudad
            tot_plat := 0
            resg_plat:= reg.clave.plat
        fin_procedimiento

        PROCEDIMIENTO Corte_ciudad() es
            Corte_plataforma()
            ESC("En la ciudad: ", resg_ciudad, "Total de ventas del 1 de julio al 1 de junio es:",
            tot_ciudad)
            //como dice total de entradas y luego discriminado por, podriamos interpretar que tambien
            quiere el tot gral, si no lo incluteron tambien esta bien :)
            tot_gral := tot_gral + tot_ciudad
            tot_ciudad := 0
    //ACA GRABO EL ARCHIVO DE SALIDA (!) Recien en este punto se el tot de entradas vendidas en
        la ciudad
        SI cont_entradas > 1000 entonces
        reg_sal.prov:= resg_prov
        reg_sal.ciudad:= resg_ciudad
        reg_sal.entradas:= cont_entradas
        grabar(ar_sal, reg_sal)
        finsi
        resg_ciudad:= reg.clave.ciudad
        fin_procedimiento
        PROCEDIMIENTO Corte_provincia() es
        Corte_ciudad()
        resg_prov:= reg.clave.prov
        fin_procedimiento
        Procedimiento Inicializar() es
        ABRIR E/(arch)
        LEER(arch, reg)
        ABRIR S/(ar_sal)
        resg_prov := reg.clave.prov
        resg_ciudad := reg.clave.ciudad
        resg_plat := reg.clave.plat
        tot_gral:= 0
        tot_ciudad:= 0
        tot_prov:=0
        fin_procedimiento
        PROCESO
            Inicializar()
            MIENTRAS NFDA(arch) HACER
                SI resg_prov <> reg.clave.prov ENTONCES
                    Corte_prov()
                SINO SI resg_ciudad <> reg.clave.ciudad ENTONCES
                    Corte_ciudad()
                    SINO SI resg_plat <> reg.clave.plat ENTONCES
                        Corte_plataforma()
                    finsi
                finsi
                finsi
                //MUY importante no poner tratar_registro dentro de un SINO del tratamiento de cortes,
                el tratar registro se hace POR CADA REGISTRO
                //consigna a:
                cont_entradas := cont_entradas + reg.entradas
                //consigna b:
                SI (reg.clave.fecha.mm = 6) o (reg.clave.fecha.dd = 1 y reg.clave.fecha.mm = 7)
                ENTONCES
                tot_plat := tot_plat + 1
                finsi
                LEER(arch,reg)
            FINMIENTRAS
            ESC ("El total de ventas del 1 de junio al 1 de julio es: ", tot_gral)
            cerrar(arch)
            cerrar(ar_sal)
FINACCIO