"""
3.Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos,
definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual
que se lee b de derecha a izquierda, y viceversa.
"""
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