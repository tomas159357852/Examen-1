def solucion05JG():
  print("\t::Que tipo de algoritmo desea utilizar::")
  tipoJG=input("\nIngrese el nombre del algoritmo:\n 1. Nota promedio \n 2. Bono desempeño \n 3. Tipo vacuna \n 4. Operacion artimetica\nNombre del algoritmo: \n").lower()
  print("\nEjecutando algoritmo...\n")
  print()
  if tipoJG=="nota promedio":
    import solucion01JG
    print()
    mensaje="\nFin del algoritmo"
  elif tipoJG=="bono desempeño":
    import solucion02JG
    print()
    mensaje="\nFin del algoritmo"
  elif tipoJG=="tipo vacuna":
    import solucion03JG
    print()
    mensaje="\nFin del algoritmo"
  elif tipoJG=="operacion aritmetica":
    import solucion04JG
    print()
    mensaje="\nFin del algoritmo"
  else:
    mensaje="\nNombre del algoritmo incorrecto"
  print(mensaje)
solucion05JG()
    
