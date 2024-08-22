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