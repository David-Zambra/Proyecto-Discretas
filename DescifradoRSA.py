#Descifrado RSA.
import time

#Función de descifrado.
def descifrar(menCif,d,n):
  mensDescif=[]
  for k in menCif:
      decryp =  (int(k)**d) % n
      mensDescif.append(chr(decryp))
  return mensDescif

#Recepción de mensaje cifrado y clave privada.
lineas = int(input('Ingrese la cantidad de mensajes desea descifrar: '))
print()
for i in range(lineas):
  menCis = input('Ingrese la lista de números que desea decodificar,' +
                ' separados por coma y espacio: ').split(",")
  d = int(input('Ingrese el valor d de la clave privada (d,n): '))
  n = int(input('Ingrese el valor n de la clave privada (d,n): '))
  x = time.time()*1000
  mensajeDescifrado = descifrar(menCis,d,n)
  mensajeDescifrado="".join(mensajeDescifrado)
  print('Su mensaje descifrado es:', mensajeDescifrado)
  y = time.time()*1000
  print("El tiempo de descifrado fue de:", y-x, "milisegundos")
  print()
