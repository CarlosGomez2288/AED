Accion BlackMesa es
    AMbiente
        clave =Registro
            Cod_Dep: N(10);
            Cod_Exp: N(10);
        finregistro

        Experimento= Registro
          Clave: clave;
          CodigoMuestra:N(10);
          Nombre: AN[50];
          Riqueza: real;
          Propiedades: AN[100];
          Peso: real;
        finregistro

        Salida = Registro
            Nombre:AN(50);
            Propiedades:AN(100);
        finRegistro
        
        Archi_sal: Archivo de salida;
        Reg_Sal:salida

        archi_Expe: Archivo de experimento ordenado por Clave;
        Reg_Expe:experimento;

        Sec_sal: secuencia de caracter

        cadena:caracter;

        Res_Departamento, Res_Experimento, CantMuestraDep, CantMuestraEx, TotalExpe:Entero;
        p_efe:real;
        bol:booleano;

        procedimiento corteExperimento() es
            Esc("|",res_Departamento,"|",res_Experimento,"|",cantMuestraEx,"|");
            cantMuestraDep:=cantMuestraDep + cantMuestraEx;
            cantMuestraEx:=0;
            Res_Experimento:= Reg_Expe.Clave.Cod_Exp;
        finProcedimiento

        procedimiento corteDepartamento() es
            corteExperimento();
            Esc("|",res_Departamento,"|",cantMuestraDep,"|");
            Esc('|--------------|-------------|--------|---------|');
            totalExpe:=totalExpe + cantMuestraDep;
            cantMuestraDep:=0;
            res_Departamento:= reg_expe.Clave.Cod_Dep;
        finProcedimiento

        procedimiento leer (var arch_Expe:Experimento;  reg:Experimento;  bol:boolean);
            Si NFDA (arch_Expe) entonces
                leer (arch_Expe,reg);
                bol:=false;
            sino
                bol:=true;
            finsi
        finProcedimiento
        procedimiento Copiar() es
                cadena:=IntToStr(Reg_Expe.clave.Cod_Dep) + '-' + IntToStr(Reg_Expe.clave.Cod_Exp);
                cadena:=cadena + '-' + IntToStr(Reg_Expe.CodigoMuestra);
                Esc(archivo,cadena);
        finProcedimiento

        procedimiento PrintHeader() es;
            Esc('_________________________________________________');
            Esc('| Departamento | Experimento | Cantidad Muestra |');
            Esc('|              |             | Depa   | Expe    |');
            Esc('|--------------|-------------|--------|---------|');
        finProcedimiento
    proceso
        cantMuestraDep,cantMuestraEx,totalExpe:=0;

        abrir E/ (Archi_Expe); leer(Archi_Expe,Reg_Expe);
        abrir S/(Archi_sal); crear(Sec_sal);

        leer(arch_Expe,Reg_Expe,bol);

        Res_Departamento := Reg_Expe.Clave.Cod_Dep;
        Res_Experimento := Reg_Expe.Clave.Cod_Exp;


        Esc("ingresar un peso efectvo");
        leer(p_efe);
        
        PrintHeader();
        
        Mientras NFDA(archi_Expe) hacer
            si( Res_Departamento <> Reg_Expe.Clave.Cod_Dep)entonces
                corteDepartamento();
            sino
                si(Res_Experimento <> Reg_expe.Clave.Cod_Exp) entonces
                    corteExperimento();
                finsi
            finsi

            cantMuestraEx:= cantMuestraEx + 1;

            #consigna 2
            si(Reg_Expe.Riqueza > 95.00) entonces
                Copiar();
                Esc(Sec_sal,Reg_Expe.Nombre);
                Esc(Sec_sal,"*");
            finsi

            #consigna 3
            si(p_efe <= reg_expe.Riqueza ) entonces
                Reg_sal.Nombre:=Reg_Expe.Nombre;
                Reg_sal.Propiedades:=Reg_Expe.Propiedades;
                Esc(archi_sal,Reg_Expeeg_Sal);
            finsi

            leer (arch_Expe,Reg_Expe,bol);
        finMiestras
        corteDepartamento();
        cerrar(Archi_sal); crear(archi_Expe); cerrar(Sec_sal);
finaccion
