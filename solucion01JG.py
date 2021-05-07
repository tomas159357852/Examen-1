def solucion01JG():
  #inicioJG
  print ("Cual es la nota final del curso")
  #ingreso de datosJG
  nota1JG=float(input("Ingrese la nota de la primera unidad:"))
  nota2JG=float(input("Ingrese la nota de la segunda unidad:"))
  nota3JG=float(input("Ingrese la nota de la tercera unidad:"))
  notaFJG=float(input("Ingrese la nota del trabajo final:"))
  #definir varJG
  primeranotaJG=0
  segundanotaJG=0
  terceranotaJG=0
  cuartanotaJG=0
  promedioJG=0
  mensajeJG=""
  #proceso
  if 0<=nota1JG<=20 and 0<=nota2JG<=20 and 0<=nota3JG<=20 and 0<=notaFJG<=20:
    primeranotaJG=nota1JG*0.20
    segundanotaJG=nota2JG*0.15
    terceranotaJG=nota3JG*0.15
    cuartanotaJG=notaFJG*0.50
    promedioJG=primeranotaJG+segundanotaJG+terceranotaJG+cuartanotaJG
    mensajeJG=f"Tu promedio final es: {promedioJG}"
  else:
    mensajeJG="Un digito que ingresó es incorrecto, negativo o mayor a 20"
  #salidaJG
  print (mensajeJG)
solucion01JG()