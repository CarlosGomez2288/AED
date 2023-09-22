accion corte 2.11 es
    ambiente
        Productos  = Registro
            clave = Resgistro
                sex:["F","M"];
                carrera:{"ISI","IEM","IQ"};
                nro_leg:N(5);
            finRegistro
            fecha_ing:fecha;
            to_mateAprobada:N(4);
        finRegistro

        archi: archivo de Productos ordenado por clave
        reg: Productos

        resg_care:{"ISI","IEM","IQ"};
        resg_sex:{"F","M"};

        sex_Mas20,sex_Men20,care_mas20,care_men20:N(4);
        total_mas,total_men:N(4);

        Procedimiento corte_Care() es
            Esc("El total de alumnos con mas de 20 materia aprobada de", resg_care,"es : ",care_mas20);
            Esc("El total de alumnos con menos de 20 materia aprobada de", resg_care,"es : ",care_men2020);
            sex_Mas20:= sex_Mas20 + care_mas20;
            sex_me20:= sex_me20 + care_men20;

            care_mas20:=0;
            care_men20:=0:
            resg_care:= reg.carrera;
        finProcedimiento

        Procedimiento corte_Sex() es
            corte_Care();
            Esc("El total de alumnos con mas de 20 materia aprobada del sex0", resg_sex,"es : ",sex_Mas20);
            Esc("El total de alumnos con menos de 20 materia aprobada de", resg_sex,"es : ",sex_me20);
            total_mas:= total_mas + sex_Mas20;
            total_me:= total_me + sex_me20;

            sex_Mas20:=0;
            sex_me20:=0:
            resg_sex:= reg.sex;
        finProcedimiento
    proceso
        sex_Mas20,sex_Men20,care_mas20,care_men20:=0;
        total_mas,total_men:=0;

        resg_care:= reg.carrera;
        resg_sex:=reg.sex;

        abrir E(archi); leer(archi,reg);

        Mientras  NFDA(archi) hacer
            si( resg_sex <> reg.sex) entonces
                corte_Sex();
            sino
                si(resg_care <> reg.carrera) entonces
                    corte_Care();
                finsi
            finsi

            si(reg.fecha_Ing.aa = 2009) entonces
                si( reg.to_mateAprobada > 20) entonces
                    care_mas20:= care_mas20 + 1;
                sino
                    si(reg.to_mateAprobada <  20) entonces
                        care_men20:= care_men20 + 1;
                    finsi
                finsi
            finsi
            leer(archi,reg);
        finMientas
        Esc("El total de alumno con mas de 20 aprobadas es: ", total_mas);
        Esc("El total de alumno con menos de 20 aprobadas es: ", total_me);
        cerar(archi);
finaccion

accion 2.14 es
    ambiente
        censo=Registro
            clave= Registro
                radio:N(2);
                manza:N(4);
                nro_vivi:N(4);
            finRegistro
            cond_vivi:{"Muy bueno","bueno","mala"}
            cant_habi:N(4);
        finRegistro

        archi:archivo de censo ordenado por clave;
        reg:censo;

        cant_rad,cant_man,total_ci;
        resg_rad:N(2);
        resg_man:N(4);

        Procedimiento corte_Manza() es
            Esc("El total de habitante de la manzana ",resg_ma," es: ",cant_man);
            cant_rad:= cant_rad + cant_man;
            cant_man:=0;
            resg_ma:= reg.manza;
        proceso

        Procedimiento corte_rad() es
            Esc("El total de habitante del radio ",resg_ra," es ",cant_rad);
            total_ci:= total_ci+cant_rad;
            cant_rad:=0;
            resg_rad:= reg.radio;
        finProcedimiento
    proceso
        cant_rad,cant_man,total_ci:=0;

        abrir E(archi); leer(archi,reg);
        resg_rad:=reg.manza;
        resg_man:=reg.radio;

        Mientras NFDA(archi) hacer
            si(resg_ra <> reg.radio)entonces
                corte_rad();
            sino
                si(resg_man <> reg.manza)entonces
                    corte_Manza();
                finsi
            finsi

            si( reg.cond_vivi = "Muy buena")entonces
                cant_man.= cant_man + reg.cant_habi;
            finsi
            leer(archi,reg);
        finMientas
        corte_rad();
        Esc("El total de habitante con condiciones muy buena es", total_ci);
        cerar(archi);
finaccion

accio