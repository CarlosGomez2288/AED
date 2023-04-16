accion tp1 es
    ambiente
        funcion edad(diaN, mesN,anioN:Entero):Entero
            diaA, mesA, anioA,edadOct:Entero
            # suponiendo que la funcion get_fecha_sistema() ya tiene los datos de dia,mes y año actual cargados
            diaA:= get_fecha_sistema().getDay();
            mesA:=get_fecha_sistema().getMonth();
            anioA:=get_fecha_sistema().getYear();

            edadOct:= (anioA - anioN) ; 
            si(mesA <= mesN) entonces 
                si(diaA <= diaN)entonces 
                    edadOct:= edadOct - 1; 
                Finsi
            Finsi

            edad:=edadOct;
        finFuncion

        procedimiento Combos(diaN,mesN,anioN,nPersonas, cantDias:Entero):Alfanumerico
            confirmacion:booleano
            edad_user:= edad(diaN,mesN,anioN);
            confirmacion:= Verdadero;

            si (cantDias= 15) y (edad_user>= 21 ) y (nPersonas>= 5) Entonces
                Esc("El combo recomendado es:");
                Esc("Combo 1: Europa");
                Esc("Duración del viaje: 15 días");
                Esc("Edad mínima: 21 años");
                Esc("Grupo mínimo: 5 personas");
            SiNo
                si (cantDias= 10) y (edad_user>= 18 ) y (nPersonas>= 2) Entonces
                    Esc("El combo recomendado es:");
                    Esc("Combo 2: Patagonia");
                    Esc("Duración del viaje: 15 días");
                    Esc("Edad mínima: 21 años");
                    Esc("Grupo mínimo: 5 personas");
                SiNo
                    si (cantDias= 20) y (edad_user>= 25 ) y (nPersonas>= 1) Entonces
                        Esc("El combo recomendado es:");
                        Esc("Combo 3: Asia");
                        Esc("Duración del viaje: 15 días");
                        Esc("Edad mínima: 21 años");
                        Esc("Grupo mínimo: 5 personas");
                    SiNo
                        si (cantDias= 14) y (edad_user>= 18 ) y (nPersonas>= 4) Entonces
                            Esc("El combo recomendado es:");
                            Esc("Combo 4: Sudamérica");
                            Esc("Duración del viaje: 15 días");
                            Esc("Edad mínima: 21 años");
                            Esc("Grupo mínimo: 5 personas");
                        SiNo
                            Esc("Lo siento segun lo datos ingresado no tenemos ningun combos para ofrecerle...")
                            confirmacion:= falso;
                        finsi
                    finsi
                finsi
            FinSi
            si (edad_user > 60) y (confirmacion)  entonces
                Esc("Felicitaciones! Usted obtiene un descuento del 20% en el paquete seleccionado");
            finsi
        finProcedimiento

        procedimiento solicitar_datos():alfanumerico
            diaN, mesN, anioN, nPersonas, cantDias:Entero

            Esc("Ingrear fecha de Nacimiento dd/mm/aa");
            leer(diaN, mesN, anioN);
            Esc("¿Cuantas personas viajaran?");
            leer(nPersonas);
            Esc("Ingrear los dias de viajes");
            leer(cantDias);

            combos(diaN,mesN,anioN,nPersonas, cantDias);
        finProcedimiento
    proceso

    solicitar_datos();
finaccion

# <----- CODIGO PSEINT----->
Funcion return <- edad ( diaN, mesN,anioN)
		definir  diaA, mesA, anioA,edadOct como Entero;

		diaA:= 10;
		mesA:=4;
		anioA:=2023;
		
		edadOct:= (anioA - anioN) ; 
		si(mesA <= mesN) entonces 
			si(diaA <= diaN)entonces 
				edadOct:= edadOct - 1; 
			Finsi
		Finsi
		return:=edadOct;
Fin Funcion

Funcion   Combos ( diaN,mesN,anioN,nPersonas, cantDias )
	Definir  confirmacion como logico;
	Definir  edad_user Como Entero;
	edad_user:= edad(diaN,mesN,anioN);
	confirmacion:= Verdadero;
	
	si (cantDias= 15) y (edad_user>= 21 ) y (nPersonas>= 5) Entonces
		Escribir "Combo 1: Europa";
	SiNo
		si (cantDias= 10) y (edad_user>= 18 ) y (nPersonas>= 2) Entonces
			Escribir "Combo 2: Patagonia";
		SiNo
			si (cantDias= 20) y (edad_user>= 25 ) y (nPersonas>= 1) Entonces
				Escribir "Combo 3: Asia";
			SiNo
				si (cantDias= 14) y (edad_user>= 18 ) y (nPersonas>= 4) Entonces
					Escribir "Combo 4: Sudamérica";
				SiNo
					Escribir "Lo siento segun lo datos ingresado no tenemos ningun combos para ofrecerle...";
					confirmacion:= falso;
				finsi
			finsi
		finsi
	FinSi
	si (edad_user > 60) y (confirmacion)  entonces
		Escribir"Felicitaciones! Usted obtiene un descuento del 20% en el paquete seleccionado";
	finsi
Fin Funcion

Funcion  datos (  )
	definir diaN, mesN, anioN, nPersonas, cantDias Como Entero;
	
	Escribir ("Ingrear fecha de Nacimiento dd/mm/aa");
	leer diaN, mesN, anioN;
	Escribir ("¿Cuantas personas viajaran?");
	leer nPersonas;
	Escribir ("Ingrear los dias de viajes");
	leer cantDias;
	
	Combos(diaN,mesN,anioN,nPersonas, cantDias);
Fin Funcion

Algoritmo sin_titulo
	datos();
FinAlgoritmo
