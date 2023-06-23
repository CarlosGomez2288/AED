Del archivo general de alumnos de la U.T.N. - Facultad Regional Resistencia, ordenado por carrera, 
se desea emitir la cantidad de alumnos correspondientes 
a cada carrera y el total general.
accion 2.2.10 es
    ambiente
        facultad = Resgistro
            carrera:{"ISI","IQ","IEM"}
            leg:N(5)
            ApeyNom:AN(20);
        finRegistro

        archi:archivo de facultad ordenado por carrera
        reg: facultad

        resg :{"ISI","IQ","IEM"}
        total, alumno:N(4);

        procedimiento corteCarrera() es
            Esc("La cantida de alumno que tiene la carrera",resg, "es de", alumno);
            total:= total +alumno ;
            alumno:= 0
            resg:= reg.carrera;
        finProcedimiento 
    proceso
        abrir E/(archi); leer(archi,reg);
        total:= 0; alumno:=0;
        resg:= reg.carrera;

        Mientras NFDA(archi) hacer
            Si( reg.carrear <> resg.carrera); entonces
                corteCarrera();
            finsi
            alumno:= alumno + 1;
            leer(archi,reg);
        finmientras
        corteCarrera();
        Esc("EL total de alumno de la UTN es: ", total);
        cerrar(archi);
    finProceso
finaccion  