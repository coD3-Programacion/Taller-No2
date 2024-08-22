# Se usa try por si el usuario pone un valor que no es valido.
try: 
    num = int(input("Por favor ingrese un número entero: "))#Se le pide un numero al usuario 
    y:int= 0
    cifras = len(str(num))#Se usa len para ver cuantas cifras tiene el numero.
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