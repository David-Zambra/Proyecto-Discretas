#Generador de claves

#Función para saber si el número es primo
def es_primo(n):
  if (n==1):
    return False
  elif (n==2):
    return True
  else:
    tope = int(n/2)+1
    for i in range(2,tope):
      if n%i == 0:
        return False
    return True

#Función para hallar M.C.D.
def mcd(a, b):
	residuo = 0
	while(b > 0):
		residuo = b
		b = a % b
		a = residuo
	return a

#Función para encontrar un inverso multiplicativo.
def inv_mul(a, n):
  for i in range(n):
    if (a*i)%n == 1:
        return i

#Recepción de valores y devolución de claves.
lineas = int(input('Ingrese cuántas claves desea generar: '))
print()
for i in range(lineas):
  cond = True; p = 1; q = 1; e = 1;
  while (cond==True):
    p = int(input('Ingrese un número primo: '))
    if (es_primo(p)):
      cond = False
    else:
      print("Este no es un número primo.")
  while (cond==False):
    q = int(input('Ingrese otro número primo: '))
    if (es_primo(p)):
      cond = True
    else:
      print("Este no es un número primo.")
  n = p*q
  phi_n = (p-1)*(q-1)
  while (cond==True):
    print("Ingrese un valor que sea menor y primo relativo de " +
          str(phi_n) + ":")
    e = int(input())
    if (mcd(e, phi_n) == 1 and e<phi_n):
      cond = False
    else:
      print('Este valor no cumple con las condiciones dadas.')
  d = inv_mul(e, phi_n)
  print("Su clave pública (e,n) es: (" + str(e) + ", " + str(n) + ")")
  print("Su clave privada (d,n) es: (" + str(d) + ", " + str(n) + ")")
  print()
