# Taller-No2

## Grupo: CoD3

### Integrantes:

ºDavid Santiago Hoyos Mateus

ºDiego Garcés Torres

### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

```python
# Se usa try por si el usuario pone un valor que no es valido.
try: 
    num = int(input("Por favor ingrese un número entero: "))#Se le pide un numero al usuario 
    y:int= 0
    cifras = len(str(num))#Se usa el metodo len para ver cuantas cifras tiene el numero.
    y += cifras
    i = 0
    anterior_cifra = 1
    print("Sus cifras son: ")
    while i < y: 
        x = (num // 10**(cifras-1))  # Obtiene la cifra más grande
        print(x)
        num = num % 10**(cifras-1)  # Remueve la cifra mas grande del numero
        cifras -= 1  # Reduce el contador de cifras
        i += 1  # Incrementa el contador de iteraciones
except ValueError:
    print("Por favor ingrese un valor válido.") 
```

#### Explicación de la solución

*-Explicacion-*

### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

```python
""" 
2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue 
los dígitos tanto de la parte entera como de la decimal.
"""

def separar_partes_digitos(n):
    #Se halla la parte entera con int(n) y la parte decimal restando la parte entera al numero
    parte_entera = int(n) 
    parte_decimal = n - parte_entera

    #Se imprime el numero con sus partes divididas
    print("El numero es:", n)
    print("La parte entera es:", parte_entera , "y la parte decimal es:", parte_decimal)

    #Se convierte el numero a str para poder recorrerlo con un for y encontrar sus digitos
    n_str = str(n)
    digitos = []
    for i in n_str: #se recorre el numero y se pone en la lista
        digitos.append(i)

    #se halla el indice del punto en la lista para hacer slicing de los digitos de la parte decimal y los de la parte entera
    punto = digitos.index(".")
    parte_decimal = digitos[punto+1:] 
    parte_entera = digitos[:punto]
    print("Los digitos de la parte entera son:", parte_entera)
    print("Los digitos de la parte decimal son: ", parte_decimal)

if __name__ == "__main__":
    numero = float(input("Ingrese un numero para separar la parte entera de la decimal: ")) #se pide el numero
    separar_partes_digitos(numero)
```

#### Explicación de la solución

**Lo primero que se hace en la funcion es encontrar la parte entera con int() y la parte decimal, luego se convierte el numero a str para convertir todos los digitos del numero en elementos de una lista incluyendo el punto ("."), y luego se divide o
se hace slicing para separar los elementos antes del punto (la parte entera) y los elementos despues del punto que son la parte decimal*

### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```python
#Se usa try por si el usuario ingresa un valor que no es valido.
try: 
    num_1 = int(input("Por favor ingrese un numero entero: "))#Se le piden dos numeros al usuario.
    num_2 = int(input("Por favor ingrese un numero entero: ")) 
    lista: list = list(str(num_1))#Se convierten los dos numeros a listas.
    lista2: list = list(str(num_2))
    lista.sort(reverse= True)#Se invierte la primera lista.
    if lista == lista2:#Se verifica si las dos listas coinciden.
        print("Los numeros que ingresaste son numeros espejos ")
    else: 
        print("Los numeros que ingresaste no son numeros espejos.")
except ValueError:
    print("Por favor ingrese numeros enteros. ")
```

#### Explicación de la solución

*-Explicacion-*

### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$

```python
"""
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos 
de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de 
la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
"""
import math

def calculo_aprox(x, n):
    suma_total = 0
    
    for i in range(0, n): #el for es la suma de la serie de taylor
        serie_taylor = ((-1)**i)*((x)**(2*i)/(math.factorial(2*i))) #la operacion
        suma_total += serie_taylor
        i += 1

    return suma_total

if __name__ == "__main__":
    x = float(input("Escriba cualquier valor real x para la aproximacion de coseno con la serie de Taylor alrededor de 0")) #se pide el numero
    valor_real = math.cos(x) 
    n = 1 #n es la cantidad de terminos de la serie, por el momento es 1
    valor_aproximado = calculo_aprox(x, n)
    error = math.fabs(((math.fabs(valor_aproximado - valor_real))/valor_real)*100) #el porcentaje (%) de error
    print(f"Con {n} terminos el valor aprox es {valor_aproximado} el valor real es {valor_real} y el % de error es {error}%")
    
    while error>10: #mientras que el error sea mayor a 10 se va a incrementar el numero de terminos hasta que sea menor
        n += 1
        valor_aproximado = calculo_aprox(x, n)
        error = math.fabs(((math.fabs(valor_aproximado - valor_real))/valor_real)*100)
        print(f"Con {n} terminos el valor aprox es {valor_aproximado} el valor real es {valor_real} y el % de error es {error}%")
        if 1<error<10:
            print(f"Con {n} terminos se tiene un error menor al 10%")
    
    while error<10: #si el error es menor al 10% se busca el termino en el que el error sea menor al 1%, 0.1% y 0.001% 
        n += 1
        valor_aproximado = calculo_aprox(x, n)
        error = math.fabs(((math.fabs(valor_aproximado - valor_real))/valor_real)*100)
        print(f"Con {n} terminos el valor aprox es {valor_aproximado} el valor real es {valor_real} y el % de error es {error}%")
        if 0.1<error<1:
            print(f"Con {n} terminos se tiene un error menor al 1%")
        elif 0.001<error<0.1:
            print(f"Con {n} terminos se tiene un error menor al 0.1%")
        elif error<0.001:
            print(f"Con {n} terminos se tiene un error menor al 0.001%")
            break
```

#### Explicación de la solución

*Primero se pide el numero que se quiere aproximar, se saca el valor real y con la funcion el valor aproximado, esto con un for que representaria la suma de la serie de Taylor. Ahora lo que se hace es hallar el porcentaje de error teniendo en cuenta los
datos de valor aproximado y el real, para que con un ciclo while e incrementando la cantidad de terminos se terminen hallando el porcentaje de error del 10%, 1%, 0.1% y 0.001%*

### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

```python
def mcd(a: int, b: int) -> int:
    if b == 0: #Caso base: si b es 0, el mcd es a
        return a
    else:
        return mcd(b, a % b) #Llamada a si misma, intercambiando los valores por b y a%b
    
if __name__ == "__main__":
    a = int(input("Por favor ingrese un número entero: ")) #Le pide al usuario dos numeros  
    b = int(input("Por favor ingrese un número entero: ")) 
    maximo_comun_divisor = mcd(a, b) # Halla el maximo comun divisor utilizando la funcion mcd
    print(f"El máximo común divisor de los números es {maximo_comun_divisor}")
```

#### Explicación de la solución

*-Explicacion-*

### 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in.

```python
"""
6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. 
Pista: Maneje valores booleanos y utilice el operador in.
"""

def elementos_repetidos(lista_d):
    elementos_nr = [] #lista con elementos que no esta repetidos (por el momento)
    for i in lista_d:
        if i in elementos_nr: #si el elemento esta en la lista de elementos no repetidos por el momento, entonces deja de ser no repetido 
            print("El elemento repetido es ", i)
        else: #si no ocurre esto, entonces el elemento se agrega a la lista de elementos no repetidos por el momento
            elementos_nr.append(i)

if __name__ == "__main__":
    numero_elementos = int(input("Ingrese la cantidad de elementos que tiene la lista")) #Aca la cantidad de elementos de la lista
    lista = []
    for i in range(1, numero_elementos+1): #se piden los elementos de la lista y se va llenando
        elementos = input("Ingrese el elemento de la lista: ") 
        lista.append(elementos)
    print(lista)
    elementos_repetidos(lista)
```

#### Explicación de la solución

*Basicamente lo que se hace es pedir la lista (sabiendo el numero de elementos y llenandola con un bucle for) y despues se crea una lista con elementos no repetidos hasta el momento y recorriendo la lista, si el elemento no esta en la lista de no repetidos
se agrega, si si esta en la lista entonces el numero deja de ser no repetido y se convierte en repetido*

### 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

```python
```

#### Explicación de la solución

*-Explicacion-*

### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. Ejemplo:
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

```python
#8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

def funcion_listas_dif(lista1, lista2):
    for i in lista1:
        if i not in lista2:
            lista_diferente.append(i)
    print("La lista 1 es:", lista1)
    print("La lista 2 es:", lista2)
    print("La lista 3 con elementos de la 1era que no tiene la 2da es:", lista_diferente)


if __name__ == "__main__":
    n_lista1 = int(input("Escriba la cantidad de elementos que tiene la lista 1: "))
    lista1 = []
    for i in range(1, n_lista1+1):
        elementos_lista1 = input("Escriba cada uno de los elementos de la lista 1: ")
        lista1.append(elementos_lista1)

    n_lista2 = int(input("Escriba la cantidad de elementos que tiene la lista 2: "))
    lista2 = []
    for i in range(1, n_lista2+1):
        elementos_lista2 = input("Escriba cada uno de los elementos de la lista 2: ")
        lista2.append(elementos_lista2)

    lista_diferente = []
    funcion_listas_dif(lista1, lista2)
```

#### Explicación de la solución

*Lo primero que se hace es pedir las 2 listas mediante ciclos For. Se crear una funcion para encontrar las lista con elementos que tiene la primera lista pero que no tiene la segunda, lo que se hace es crear una tercera lista donde se
van a guardar todos estos elementos, y se recorre la primera lista viendo si el elemento en cada iteracion esta en la segunda lista, si no lo esta entonces es unico por lo que se pone en la lista diferenciadora, se sigue el procedimiento
con todos los elementos de la lista 1*

### 9. Resolver el punto 7 del taller 1 usando operaciones con vectores.
### Taller 1 - Punto 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
```

#### Explicación de la solución

*-Explicacion-*

### 10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?

```python
```

#### Explicación de la solución

*-Explicacion-*

## Bono

### 11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

```python
```

#### Explicación de la solución

*-Explicacion-*
