#Cifrado RSA.
import time

#Función de cifrado.
def cifrar(cadena, e, n):
    mensaje=[]
    for i in range(len(cadena)):
        M=ord(cadena[i])
        C=(M**e)%n
        mensaje.append(C)
    return mensaje

#Recepción de mensaje y clave pública.
lineas = int(input('Ingrese la cantidad de mensajes desea cifrar: '))
print()
for i in range(lineas):
  cadena = input('Ingrese la cadena de texto que desea cifrar: ')
  e = int(input('Ingrese el valor e de la clave pública (e,n): '))
  n = int(input('Ingrese el valor n de la clave pública (e,n): '))
  x = time.time()*1000
  print("Su mensaje cifrado es:", cifrar(cadena, e, n))
  y = time.time()*1000
  print("El tiempo de cifrado fue de:", y-x, "milisegundos")
  print()
