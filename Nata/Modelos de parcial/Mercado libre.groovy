Accion MercadoLibre Es
AMbiente

Proceso
	Abrir E/(Ventas);Leer(Ventas,reg1)
	Abrir E/(Transacciones);Leer(Transacciones,reg2)
	Abrir E/S(Vendedores)
	Abrir /S(VentasAct)


	Mientras (reg1.Clave <> HV) o (reg2.Clave <> HV) Hacer
		reg4:=reg1
		reg3.Nu_vendedor:=reg1.Nu_vendedor
		Leer(Vendedores,reg3)
		Mientras 


