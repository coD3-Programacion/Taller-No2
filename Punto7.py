"""
7.Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
"""
def contar_vocales(cadena): #Se crea una funcion que identifica cuantas vocales tiene una cadena
    vocales = 'aeiouAEIOU'
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

try: #Se usa try por si el usuario ingresa un valor que no es valido.
    cantidad = int(input("Por favor ingrese el número de elementos que va a tener su lista: ")) #Se le pide al usuario cuantos elementos va a tener la lista
    vector = []

    for _ in range(cantidad): #Se usa un ciclo for para poder poner la cantidad de elementos que desea el usuario dentro de la lista.
        x = input("Por favor ingrese un elemento: ")
        vector.append(x)

    cadena_con_vocales: list = []

    for cadena in vector: #Se usa un ciclo for para evaluar cada elemento de la lista y si se cumple la condicion se pone ese elemento dentro de una nueva lista.
        if contar_vocales(cadena) >= 2:
            cadena_con_vocales.append(cadena)
        else:
            continue

    if len(cadena_con_vocales) > 0: #Si hay un elemento o mas dentro de la nueva lista esta se imprime, es decir, se imprimen todos los elementos que tienen 2 vocales o mas.
        print(f"La o las cadenas con vocales son: {cadena_con_vocales}")
    else:
        print("No existe") #Si lo anterior no se cumple, quiere decir que no existe ningun elemento que cumpla la condicion dada.
except ValueError:
    print("Por favor ingrese un valor valido.")