Accion 5.1.4 Es{
	Function Par(n:entero):boolean{
		if n Mod 2 <> 0{
			Par=false
		}else{
			if n < 10{
				Par:=true
			}else{
				Par=Par(n DIV 10)
			}
		}
	}
}
			