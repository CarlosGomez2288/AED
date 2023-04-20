Accion PRINT Es
Ambiente
	sec,sal: secuencia de alfanumerico
	v,Día,Modal: alfanumerico
	ContMes,FraseLarga,ContPal: alfanumerico

	Subaccion Mes Es
		Según i Hacer
		=1:Esc("Enero")
		=2:Esc("Febrero")
		...
		FinSegún
	FinSubaccion

Proceso
	ARR(sec);AVZ(sec,v)
	Crear(sal)
	Mientras NFDS(sec) Hacer
		Para i:=1 hasta 12 Hacer
			Mes
			Mientras v<>"$" y NFDS(sec) Hacer
				Mientras v<>"#" Hacer
					Modal:=v
					AVZ(sec,v)
					Día:=v
					AVZ(sec,v)
					Si Modal = "F" Entonces
						Si Día = "4" Entonces
							Mientras v<>"#" Hacer
								ContPal:=0
								Mientras v=" " HACER
									Esc(v)
									ContPal:=ContPal+1
								FinMientras
								AVZ(sec,v)
								Esc(v)
							FinMientras
							Esc("La cantidad de palabras de la frase son:",ContPalabras)
							Si ContPal > FraseLarga
								FraseLarga:=ContPal
							FinSi
							AVZ(sec,v)
						Sino
							AVZ(sec,v)
							Mientras v<>"#" hacer
								Esc(sal,v)
								AVZ(sec,v)
							FinMientras
							Esc(sal,v)
							AVZ(sec,v)
						FinSi
					Sino
						AVZ(sec,v)
						AVZ(sec,v)
						Mientras v<>"#" Hacer
							Esc(sal,v)
							AVZ(sec,v)
						FinMientras
						Esc(sal,v)
						AVZ(sec,v)
					FinSi
				FinMientras
				Esc(sal,v)
				AVZ(sec,v)
			FinMientras
			Esc(sal,v)
			AVZ(sec,v)
		FinPara
	FinMientras
	Cerrar(sec)
	Cerrar(sal)
FinAccion
		









