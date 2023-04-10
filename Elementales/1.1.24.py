accion 1.1.24 es
    ambiente
        impu, total, ingreso:Entero
    proceso
        
        Mientras (ingreso <> 99999) hacer
            Esc("Ingresar Importe ");
            leer(ingreso);

            impu:= ingreso * 1,10;

            segun (ingreso) hacer 
                <501:
                    Esc("El total pagar es $", ingreso + impu, "en una couta") 
              < 1001:
                    Esc("El total pagar es $", ingreso + impu, "en dos couta") 
                > 1000
                    Esc("El total pagar es $", ingreso + impu, "en tres couta") 
        finmientras
finaccion