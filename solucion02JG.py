def solucion02JG():
  #inicioJG
  print("Bono por desempeño")
  #ingreso de datosJG
  puntosJG=int(input("Ingrese los puntos totales que tiene:"))
  salariominJG=int(input("Ingrese el salario mínimo en dolares de su país:"))
  #definir varJG
  bonoJG=0
  mensajeJG=""
  #Proceso
  if puntosJG>=50 and puntosJG<=100:
    bonoJG=salariominJG*0.10
    mensajeJG=f"El bono que recibirá sera de: {bonoJG} dolares"
  elif puntosJG>=101 and puntosJG<=150:
    bonoJG=salariominJG*0.40
    mensajeJG=f"El bono que recibirá sera de: {bonoJG} dolares"
  elif puntosJG>=151:
    bonoJG=salariominJG*0.70
    mensajeJG=f"El bono que recibirá sera de: {bonoJG} dolares"
  else:
    mensajeJG="Usted no tiene un bono que recibir"
  #salidaJG
  print (mensajeJG)
solucion02JG()