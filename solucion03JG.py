def solucion03JG():
  #entradaJG
  print("\t .::Que tipo de vacuna recibirás segun tu edad y sexo::.")
  #ingreso de datosJG
  edadJG=int(input("Ingrese la edad que tiene:"))
  sexoJG=input("Ingrese si es Hombre o Mujer:").lower()
  #definir varJG
  persona70JG="C"
  mujer16JG="B"
  hombre16JG="A"
  persona16JG="A"
  mensajeJG=""
  #proceso
  if sexoJG=="hombre" or sexoJG=="mujer" and edadJG>0:
    if edadJG>=70:
      mensajeJG=f"La vacuna que te corresponde es la {persona70JG}"
    elif edadJG>=16 and edadJG<=69:
      if sexoJG=="hombre":
        mensajeJG=f"La vacuna que te corresponde es la {hombre16JG}"
      elif sexoJG=="mujer":
        mensajeJG=f"La vacuna que te corresponde es la {mujer16JG}"
      else:
        mensajeJG="El sexo que indicó es incorrecto"
    elif edadJG<16:
      mensajeJG=f"La vacuna que te corresponde es la {persona16JG}"
    else:
      mensajeJG=f"Error: ingresaste un dato incorrecto"
  else:
    mensajeJG="Ingresaste incorrectamente el sexo o tu edad es negativa o 0"
  #salida
  print(mensajeJG)
solucion03JG()