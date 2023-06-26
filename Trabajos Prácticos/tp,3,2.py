
        procedimiento  Corte_Marca() es
            #informo la marca producto
            #Informo cantidad producto tipo 2
            #informo cantidad de ventas
            #acumulo cantidad pruducto tipo 2
            #acumulo cantidad venta
            #reinicio contadores del nivel a 0
            #cambio de resguardo 
            #resguardo cantidad de ventas en venta_Mayor
            si ( venta_Mayor > 500) entonces
                #informo la marca que tiene venta mayores a 500
            finsi
        finProcedimento

        procedimiento  Corte_Sucursal() es
            #llamo al corte nivel inferior Corte_MArca()
            #informo la Sucursal
            #Informo cantidad producto tipo 2 en la sucursal
            #informo cantidad de ventas en la sucursal
            #acumulo cantidad pruducto tipo 2
            #acumulo cantidad venta
            #reinicio contadores del nivel a 0
            #cambio de resguardo 
        finProcedimento 

        procedimiento  Corte_Provincia  () es
            #llamo al corte nivel inferior Corte_Sucursal()
            #Informo provincia
            #Informo cantidad producto tipo 2 en la provincia 
            #informo cantidad de venta por provincia
            #acumulo cantidad  total pruducto tipo 2
            #acumulo cantidad total ventas
            #reinicio contadores del nivel a 0
            #cambio de resguardo
        finProcedimento 

        procedimiento tratamiento_corte() es
            si(res_provincia <> reg.clave.provincia) entonces
                 Corte_Provincia();
            sino
                si(resg_Sucursal <> reg.clave.sucursal) entonces
                    Corte_Sucursal();
                sino
                    si(resg_Marca <> reg.clave.marca) entonces
                        Corte_Marca();
                    finsi
                finsi
            finsi
        finProcedimento

        procedimiento tratar_registro() es
            si(reg.clave.tipo_Produc = 2) entonces
                #aumentos los contadores
            finsi
        finProcedimento
   
        
        #llamo los procedimientos
        #llamo al corte mayor
        #Informo los totales y cierro el archivo 

#Es necesario 3 cortes porque una provicia puede tener mas de una sucursal,la surcusal puede tener mas de una marca
#y la marca puede tener mas de un producto.
#Se necesita 5 contadores, cont_venta, cont_Prud, la primera acumula la cantidad de venta y la segunda acumula
#cantida de producto de tipo 2
#total_venta, tota_prod, estas acumulan los totales generales y ademas se necesita un contador mas venta_Mayor esta sirve
#para resguardar la venta de cada marca para despues informar las marcas  con ventas mayor a 500
#En Corte_Marca uso condicional para informar las marca con mas de 500 ventas
#En tratamiento uso condicional para aumentar los contadores solo si el tipo es igual a 2. 