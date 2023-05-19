#ambiente
#declaro variables  y secuencia a utilizar 
# Proceso
# Inicializar secuencias y contadores
Mientras NFDS(sec) hacer
    #Tratar consigna 2 -> cuenta opinion registradas.
    Mientras ( v <> ".") hacer
        # Trato incio de inicio de numero opinion
        para i= 1 hasta 10 hacer
            #avanzo numero de opinion
        finpara

        #verifica si ventana es "*" entonces no tiene num de cliente 
        si ( v = "*") entonces
            # Trato consigna 3 -> cuenta los clientes no registrados.
            #avanzo

            #Trato inicio de mail
            Mientras ( v <> "#") hacer
                #avanzo el mail.
            fimientras
            #Trato fin de mail
            #Avanzo

            #Trato inicio de fecha
            para i= 1 hasta 9 hacer
                #avanzo fecha.
            finpara
            #Trati fin de fecha
            #avanzo 

            #Trato inicio de opinion
            Mientras ( v <> $ ) hacer
                # Trato consigna 4 -> copio opinion a la sec de salida
            finMientras
            #avanzo 

            #Trato consigna 1 -> copio valoracion
            #Trato consigna 5 -> verifica si es opiniones malas y cuenta.

        sino
            # Trato consigna 1 ->Trata el inicio de numero de cliente. 
            Mientras ( v <> "*") hacer
                #Copia el numero de cliente a la sec1 de salida
            fimientras

            #Trato inicio de mail
            Mientras ( v <> "#") hacer
                #avanzo el mail.
            fimientras
            #Trato fin de mail
            #Avanzo

            #Trato inicio de fecha
            para i= 1 hasta 9 hacer
                #avanzo fecha.
            finpara
            #Trati fin de fecha
            #avanzo 

            #Trato inicio de opinion
            Mientras ( v <> $ ) hacer
                # Trato consigna 4 -> copio opinion a la sec de salida
            finMientras
            #avanzo 
        finsi
    fimientras
        #avanzo al siguiente opionion o fin de secuencia
fimientras   
# Muesta por pantalla  contadores
# cerrar secuencias