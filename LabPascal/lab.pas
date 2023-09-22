program CargarDatos;

type

  RegistroMuestra = record
    Cod_Dep: integer;
    Cod_Exp: integer;
    CodigoMuestra: integer;
    Nombre: string[50];
    Riqueza: real;
    Propiedades: string[100];
    Peso: real;
  end;

var
  Archivo: file of RegistroExperimento;
  Muestra: RegistroMuestra;
  NumRegistros: integer;
  i: integer;

begin
  // Abre el archivo para escritura
  Assign(Archivo, 'experimentos.dat');
  Rewrite(Archivo);

  // Solicita la cantidad de registros a cargar
  Write('Ingrese la cantidad de registros a cargar: ');
  ReadLn(NumRegistros);

  // Carga los registros en el archivo
  for i := 1 to NumRegistros do
  begin
    // Solicita los datos del experimento
    WriteLn;
    WriteLn('Ingrese los datos del experimento ', i, ':');
    Write('Código del departamento: ');
    ReadLn(Muestra.Cod_Dep);
    Write('Código del experimento: ');
    ReadLn(Muestra.Cod_Exp);

    // Escribe los datos del experimento en el archivo
   

    // Solicita los datos de la muestra
    WriteLn;
    WriteLn('Ingrese los datos de la muestra ', i, ':');
    Write('Código de la muestra: ');
    ReadLn(Muestra.CodigoMuestra);
    Write('Nombre de la muestra: ');
    ReadLn(Muestra.Nombre);
    Write('Riqueza de la muestra: ');
    ReadLn(Muestra.Riqueza);
    Write('Propiedades de la muestra: ');
    ReadLn(Muestra.Propiedades);
    Write('Peso de la muestra: ');
    ReadLn(Muestra.Peso);

    // Escribe los datos de la muestra en el archivo
    Write(Archivo, Muestra);
  end;

  // Cierra el archivo
  Close(Archivo);

  WriteLn;
  WriteLn('Datos cargados exitosamente en el archivo experimentos.dat');
end.