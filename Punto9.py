"""
9. Resolver el punto 7 del taller 1 usando operaciones con vectores.
"""
#Resolver el punto 7 del taller 1 usando operaciones con vectores
lista: list = []
a = float(input("Por favor ingrese un numero: "))
lista.append(a)
b = float(input("Por favor ingrese un numero: "))
lista.append(b)
c = float(input("Por favor ingrese un numero: "))
lista.append(c)
d = float(input("Por favor ingrese un numero: "))
lista.append(d)
e = float(input("Por favor ingrese un numero: "))
lista.append(e)

sum = 0 
i = 0

#Se usa un ciclo for para sumar todos los numeros y luego esto se divide en el numero de elementos, es decir, 5.
for i in range(5): 
    sum += lista[i]
promedio = sum/5
print(f"El promedio de los numeros que pusiste es: {promedio}")

#Para sacar la mediana ordenamos la lista usando el metodo sort e imprimimos el tercer elemento de la lista, el cual en este caso seria la mediana.
lista.sort()
print(f"La mediana de los numeros que ingresaste es: {lista[2]}")

#Para sacar el promedio multiplicativo se usa un ciclo for para multitplican todos los numeros de la lista y se los elevo a 1/5 que equivaldria a la raiz quinta de el producto de la multiplicacion. 
x = 1
for i in range(5):
    x *= lista[i]
promedio_multiplicativo = x**(1/5)
print(f"El promedio multiplicativo de los numeros que ingresaste es: {promedio_multiplicativo}")

#En este caso solo se imprime la lista, debido a que ya la habiamos organizado para sacar la mediana.
print(f"La lista ordenada de forma ascendente es: {lista}")

#Utilizmos slicing para imprimir la lista de atras para delante, para que quede ordenada de manea descendente.
print(f"La lista ordenada de forma descendente es: {lista[::-1]}")

#Elevamos el primer elemento de la lista al ultimo numero de la lista, debido a que la lista esta ordenada de forma descendente.
potencia = lista[0]**lista[4]
print(f"La potencia del mayor numero elevado al menor numero es: {potencia}")

#Como fue visto en clase, se aplica el metodo Newton-Raphson para encontrar la raiz cubica del numero menor.
y: float
if lista[4] == 0:
     y = 0
y = lista[4]  
for i in range(1000):
    y_anterior = y  
    y = y - (y**3 - lista[4]) / (3 * y**2)  
    if abs(y - y_anterior) < 0.00001: 
        break
print(f"La raiz cubica del numero menor es: {y}")