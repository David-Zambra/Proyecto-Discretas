# Proyecto Discretas
Introducción

  1. Problema a resolver

	   La pandemia de coronavirus que ha tenido lugar a lo largo del 2020 ha causado, gracias a los períodos de cuarentena, un aumento en el uso de diversas plataformas virtuales. En  consecuencia, el número de delitos cibernéticos también ha crecido de modo alarmante: para el mes de agosto, nada más en Colombia, estos habían presentado un incremento del  150% y se habían encontrado alrededor de 200 páginas con contenido malicioso [1]. Se hace evidente, entonces, una preocupación generalizada respecto a la seguridad informática en los habitantes del mundo digital. Esto se agrava más al tener en cuenta que se estas eguridad depende el dinero y la información importante de muchas personas que confían en los lugarers que visitan y las acciones que realizan. Por tal motivo, la necesidad de profundizar en áreas relacionadas, con el fin de desarrollar estrategias para la protección de los usuarios, se convierte en una nueva necesidad para los ingenieros de sistemas en formación.

  2. Estado del arte

		Existen diferentes formas o algoritmos de encriptar un mensaje, cada uno de ellos se usa de manera diferente dependiendo de lo que se desea enviar de un lugar a otro. Entre los principales se destacan dos formas de realizarlo, el cifrado simétrico y el asimétrico. [2]

	  Por parte del cifrado simétrico, los esquemas de cifrado simétrico (clave secreta) utilizan la misma clave para el cifrado y el descifrado y, por lo general, tienen longitudes de clave predefinidas. Proporcionan una alta seguridad y un alto rendimiento, pero sufren el problema del intercambio de claves. Un grupo de entidades necesita intercambiar  n(n−1)2  claves diferentes a través de canales seguros.

	  Por otro lado, en el sifrado asimétrico, los esquemas de cifrado asimétrico (clave pública) utilizan diferentes claves para el cifrado y el descifrado, y normalmente tienen longitudes de clave arbitrarias. Es importante que sea prácticamente imposible calcular la clave de descifrado a partir de la clave de cifrado. Esto reduce el número de pares de claves diferentes en un grupo de  n  entidades a  n . Los algoritmos de clave pública tienen matemáticas complejas y necesitan claves muy largas. Debido a esto, la criptografía de clave pública es mucho más lenta que la criptografía de clave secreta.

	  Uno de los algoritmos que se considera bastante seguro dentro de este último grupo es el llamado RSA. Además, al tratarse de uno de los cifrados más populares en la actualidad, ya ha sido abordado mútiples veces en estudios que buscan determinar su eficiencia y su seguridad, siendo comparado con otros algoritmos como AES, IDEA Y RC4. Como conclusión de dichos estudios se obtuvo que el RSA contaba con las mejores características para catalogarse como un buen sistema de cifrado, si bien se recomienda a usar claves grandes y, por tanto, consume mayor tiempo. [3]

	  A continuación se realizará una implementación de este algoritmo, aplicando nociones de teoría de números.
  
Materiales y Métodos.

  1. Datos utilizados.

	  Los datos que se utilzan para este proyecto consisten de cadenas de texto que serán cifradas empleando un algoritmo RSA y dos números primos seleccionados al azar, los cuales se emplearán en la generación de las claves.

  2. Descripción matemática de los métodos.

	  **2.1. Números primos relativos y algoritmo de Euclides:** Un número primo es aquel que tiene como únicos divisores al  1  y a sí mismo. Luego, se dice que dos números son primos relativos, o coprimos, si no tienen factores primos en común. Es decir, si no comparten otro divisor diferente de  1 .

	  El algoritmo de Euclides, por su parte, es un procedimiento paso a paso en el que se busca dar con el máximo común divisor de dos números. Se escribe al mayor de los números como el producto entre el menor y el cociente de ambos, más el residuo de la división. Luego, dicho cociente se escribe de la misma forma: este tomará el rol de "número mayor" y el residuo tomará el rol de "número menor" para ese caso. Se continúa así hasta que el residuo sea cero, de manera que el penúltimo residuo corresponderá con el máximo común divisor. Es decir:

      a=q1b+r1

      b=q2r1+r2

      r1=q3r2+r3

      ...

      ri−1=qi+1ri+0 

      donde  m  puede tomar distintos valores entre los enteros (ya que el algoritmo puede terminar en cualquier momento) y  ri  es el máximo común divisor de los números  a  y  b . [4]

      Este algoritmo puede ser útil para determinar si dos números son primos relativos, pues se dará el caso cuando el máximo común divisor sea igual a  1 .

		**2.2. Función  ϕ  de Euler y Teorema de Euler:** Para  n>1 , se define la función  ϕ(n)  como el número de enteros positivos menores o iguales que  n , que son primos relativos con  n . Se tiene, por tanto, que si  n  es un número primo, como sus únicos divisores serán  1  y él mismo, todos los enteros menores a  n  serán primos relativos de  n .

		En síntesis: si  n  es primo,  ϕ(n)=n−1 

		Para continuar, primero se debe definir qué es una congruencia. Sea  m  un entero positivo y  a,b  dos números enteros, se dice que  a  y  b  son congruentes módulo  m  si el residuo que resulta de dividir  a  entre  m  es el mismo que resulta de dividir  b  entre  m . Esto se denota por:

		a≡b(modm) 

		El teorema de Euler satisface que, si  n  es un entero positivo y  a  es un primo relativo de  n , entonces  aϕ(n)≡1(modn) . [4] Este teorema es de gran utilidad para la teoría, ya que de ahí se obtiene el pequeño teorema de Fermat, por ejemplo; y también para la práctica, pues de aquí parte el cifrado empleado en el algoritmo RSA.

		**2.3. Inversos multiplicativos e identidad de Bézout:** El inverso multiplicativo de  a  módulo  n  es un entero  v  tal que  av≡1(modn) . Para que este valor  v  exista, debe cumplirse que  a  y  n  sean coprimos, pues en caso contrario existirá un factor común que impida la congruencia.

		El cálculo de estos inversos suele realizarse mediante la identidad de Bézout. Esta expresa que si  a  y  b  son enteros, siendo  d  su máximo común divisor, existen dos enteros  v  y  w  tales que  av+bw=d .

		Luego, se tiene que el entero  v  es el inverso multiplicativo de  a  módulo  b  si estos son primos relativos, porque:

		av+bw=1

		av=1−bw

		av≡1(modb) 

		De manera que se puede emplear sustitución inversa del algoritmo de euclides para llegar a la respuesta. [5]

  3. Algoritmos.

		El algoritmo a utilizar (RSA) consiste de los siguientes pasos [4]:

		**3.1. Generación de clave pública y privada.**

	  - Se eligen dos números primos  p  y  q . Luego, se calcula un valor  n  dado por el producto entre ambos; es decir,  n=p⋅q .

	  - Se aplica la función  ϕ  de Euler para el  n  calculado, que al resultar de un producto entre dos primos se cumple que:  ϕ(n)=(p−1)(q−1) .

	  - Se escoge un entero  e  mayor a  1  y menor a la función  ϕ(n)  calculada, de tal manera que  e  sea primo relativo de  ϕ(n) .

	  - Se encuentra un inverso multiplicativo de  e  módulo  ϕ(n) , el cual también debe estar entre  1  y  ϕ(n) . Este se denota como  d .

	  - La salida estará conformada de: la clave pública que estará dada por  (e,n) , y la clave privada dada por  (d,n) .

		**3.2. Algoritmo de cifrado**

	  - El mensaje en forma de texto se convierte en una lista de números utilizando el código ASCII. Esta constituye la entrada, junto con la clave pública  (e,n) .

	  - Para cada número  M  se calcula, utilizando la clave, un número  C  tal que  C=Memodn .

	  - Se retorna la lista de números cifrados.

		**3.3. Algoritmo de descifrado**

	  - Entra una lista de números cifrados junto con la clave privada  (d,n) .

	  - Para cada número  C  se calcula, utilizando la clave, un número  M  tal que  M=Cdmodn .

	  - La lista de números se convierte en un mensaje de texto utilizando el código ASCII, y este es el resultado que se retorna.

  4. Configuración experimental.

- En primer lugar, deben elegirse dos números primos y calcular su producto. Por tanto, se tiene  p=61  y  q=19 , de donde se calcula un  p⋅q  igual a  n=1159 

  A continuación, se calcula  ϕ(n)=(p−1)(q−1)=(60)(18)=1080 

  Debe escogerse un número para la clave privada, el cual debe ser coprimo con  ϕ(n)  y menor a este valor. Se escoge  e=49 , pues se puede evidenciar:

  1080=22(49)+2 
  
  49=24(2)+1 
  
  2=2(1)+0 

  Esto quiere decir que, al aplicar el algoritmo de Euclides, el máximo común divisor entre  49  y  1080  es  1 , comprobando así que son primos relativos.

  El siguiente paso consiste en hallar un inverso multiplicativo de  49  módulo  1080 . Para ello, puede realizarse sustitución inversa con el fin de resolver la identidad de Bézout  49v+1080w=1 , utilizando el algoritmo anterior. De este, cada expresión (sin considerar la última) puede reformularse como:

  1=49−24(2) 
  
  2=1080−22(49) 

  Reemplazando la segunda en la primera se llega a:

  1=49−24(1080−22(49)) 
  
  1=529(49)−24(1080) 

  Ya resuleta la identidad, se tiene el inverso multiplicativo  d=529 , porque  49(529)≡1(mod1080) 

  Al conocer todos los valores  e ,  d  y  n , se definen las claves:

  Clave pública  (e,n) :  (49,1159) 
  
  Clave privada  (d,n) :  (529,1159) 

  Entonces, la expresión de cifrado está dada por  C=M49mod1159  y la expresión de descifrado está dada por  M=C529mod1159 

- Para una segunda versión del algoritmo RSA se eligieron números mayores, estos son los primos  p=131  y  q=211 . Por tanto, el producto  p⋅q  está dado por  n=27641 

  Siguiendo con los demás pasos, se calcula  ϕ(n)=(130)(210)=27300 

  Como valor de  e , puede tomarse  e=121 , el cual está dentro del rango y cumple con ser primo relativo de  ϕ(n) , tal como se observa al aplicar el algoritmo de Euclides:

  27300=225(121)+75 
  
  121=1(75)+46 
  
  75=1(46)+29 
  
  46=1(29)+17 
  
  29=1(17)+12 
  
  17=1(12)+5
  
  12=2(5)+2 
  
  5=2(2)+1 
  
  2=2(1)+0 

  Se tiene que su máximo común divisor es 1; por ende, son coprimos.

  Ahora debe encontrarse un inverso multiplicativo de  121  módulo  27300 . Es decir, se resuelve la identidad de Bézout  121v+27300w=1 . Usando el algoritmo de Euclides en la parte superior, se llega a que:

  1=11281(121)−50(27300) 

  por tanto, se tiene el inverso multiplicativo  d=11281 , porque  121(11281)≡1(mod27300) 

  Luego, las claves son:

  Clave pública  (e,n) :  (121,27641) 
  
  Clave privada  (d,n) :  (11281,27641) 

  Es decir, la expresión de cifrado está dada por  C=M121mod27641  y la expresión de descifrado está dada por  M=C11281mod27641 

- Para una última evaluación del algoritmo, se tomaron valores de números primos aún más grandes para  p  y  q , siendo estos  p=2689  y  q=3517 . Luego, el producto  p⋅q  equivale a  n=9457213 

  Ahora, tal como en las dos ocasiones anteriores, se calcula  ϕ(n)=(2688)(3516)=9451008 

  En este caso, al buscar un valor  e  tal que  1<e<ϕ(n) , y que sea coprimo con este último, se elige  e=815135 . Puede comprobarse la condición calculando el máximo común divisor mediante el algoritmo de Euclides:

  9451008=11(815135)+484523 
  
  815135=1(484523)+330612 
  
  484523=1(330612)+153911 
  
  330612=2(153911)+22790 
  
  153911=6(22790)+17171 
  
  22790=1(17171)+5619 
  
  17171=3(5619)+314 
  
  5619=17(314)+281 
  
  314=1(281)+33 
  
  281=8(33)+17 
  
  33=1(17)+16 
  
  17=1(16)+1 
  
  16=16(1)+0 

  Es así que se tiene un inverso multiplicativo  d=571871 , pues resolviendo la identidad de Bézout  815135v+9451008w=1 , se tiene que los valores  v  y  w  están dados por la expresión  1=571871(815135)−49323(9451008) 

  A continuación se describen las claves y expresiones generadas:

  Clave pública  (e,n) :  (815135,9457213)
  
  Clave privada  (d,n) :  (571871,9457213) 

  La expresión de cifrado está dada por  C=M815135mod9457213  y la expresión de descifrado está dada por  M=C571871mod9457213 .
  
Resultados.

- Para los bloques de código, en primer lugar, se escribe uno que permita generar las claves. De esta manera, el usuario puede utilizar su propia combinación numérica sin tener que recurrir a alguna preexistente, o bien a realizar cálculos como los presentados arriba. En segundo lugar se escribe el código para cifrado y descrifrado.

  En la salida de cada código se dejan los resultados de las pruebas realizadas para evaluar esta implementación del algoritmo RSA. Se utilizaron los valores de los tres pares de claves ya encontrados en la configuración experimental, y el mensaje para todos los casos es: "Universidad Nacional de Colombia". Con estos datos se mide el tiempo computacional empleado para el cifrado y el descifrado en cada caso; de manera posterior, se comparan los resultados obtenidos.
  
