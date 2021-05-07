def solucion04JG():
  #entradaJG
  print("::Calculador de operaciones aritméticas::")
  #ingreso de datosJG
  primerJG=float(input("Ingrese el primer número:"))
  segundoJG=float(input("Ingrese el segundo número:"))
  signoJG=input("Ingrese el signo de la operación sea +(suma), -(resta), *(multiplicación), /(división) y ^(potencia):").lower()
  #def variablesJG
  respuestaJG=0
  mensajeJG=""
  #proceso
  if signoJG=="+":
    respuestaJG=primerJG+segundoJG
    mensajeJG=f"La suma total es {respuestaJG}"
  elif signoJG=="-":
    respuestaJG=primerJG-segundoJG
    mensajeJG=f"La resta total es {respuestaJG}"
  elif signoJG=="*":
    respuestaJG=primerJG*segundoJG
    mensajeJG=f"La multiplicación total es {respuestaJG}"
  elif signoJG=="/":
    respuestaJG=primerJG/segundoJG
    mensajeJG=f"La división total es {respuestaJG}"
  elif signoJG=="^":
    respuestaJG=primerJG**segundoJG
    mensajeJG=f"La potencia total es {respuestaJG}"
  else:
    mensajeJG="Ingreso una operación o número incorrecto"
  print(mensajeJG)
solucion04JG()