"""
11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, 
de cada una de sus columnas y de cada diagonal es igual.
"""

def crear_matriz(argumento_matriz_fila, argumento_matriz_columna):#funcion para pedir y guardar los valores de una matriz
    #se crean 2 listas, la matriz final y una para las filas de la matriz
    matriz = []
    fila_matriz = []
    for i in range(argumento_matriz_fila): #ciclo que se repitira el # de filas de la matriz (recorre filas)
        for j in range(argumento_matriz_columna): #ciclo que se repitira el # de columnas de la matriz (recorre cada elemento de la fila)
            valor = float(input(f"Escriba los valores de la matriz en orden ({i+1} fila y {j+1} columna): ")) #se pide cada valor (cada j son los valores de 1 fila completa)
            fila_matriz.append(valor) #cuando termina la 1era iteración vamos a tener los valores de la primera fila (aca se van agregando a la lista "fila_matriz")
        matriz.append(fila_matriz) #despues se agregan todos los valores de la fila a la lista "matriz" (en cada i se agrega una fila completa)(el proceso es fila por fila)
        fila_matriz=[] #se vacia la lista "fila_matriz" porque aún tiene los valores de la fila anterior, y al vaciarla se reinicia el proceso con los valores de la siguiente fila
    return matriz #al final la funcion retorna la lista "matriz" cuando terminan los 2 ciclos con todas las filas y columnas completas 

def suma_filas(argumento_matriz):
    lista_suma_filas = [] #Aca van a estar las sumas de cada una de las filas de la matriz
    for i in argumento_matriz: #recorre las filas
        suma_filas_matriz = 0  
        for j in i: #recorre los elementos de cada una de las filas y los suma en la variable suma_filas_matriz
            suma_filas_matriz += j
        lista_suma_filas.append(suma_filas_matriz) #Se agrega a la lista la suma de cada una de las filas

    print("La suma de cada una de las filas son:", lista_suma_filas)

    #Aca se verifica si cada uno de los elemento de la lista (cada fila) es igual, si no la funcion retorna un False, y si son iguales un True
    for i in lista_suma_filas:
        if i != lista_suma_filas[0]:
            return False
    return True

def suma_columnas(argumento_matriz):
    lista_suma_columnas = [] #Aca van a estar las sumas de cada una de las columnas de la matriz
    suma_columnas_matriz = 0 #Aca van a estar las sumas individuales

    #Los 2 ciclos se repiten la cantidad de filas (o columnas porque tienen el mismo valor)
    for j in range(len(argumento_matriz)): 
        for i in range(len(argumento_matriz)):
            suma_columnas_matriz += matriz[i][j] #se suman los elementos correspondientes (j) de cada una de las filas
        lista_suma_columnas.append(suma_columnas_matriz) #Se agrega a la lista la suma de cada una de las columnas
        suma_columnas_matriz = 0 #La variable de las sumas vuelve a ser 0 para empezar de nuevo

    print("La suma de cada una de las columnas son:", lista_suma_columnas)

    #Aca se verifica si los elementos de lista_suma_columnas son iguales, si no la funcion retorna un False, y si son iguales un True
    for i in lista_suma_columnas:
        if i != lista_suma_columnas[0]:
            return False
    return True

def suma_diagonales(argumento_matriz):
    #Se crean 2 variables que van a ser la suma de cada una de las diagonales
    suma_primera_diagonal = 0
    suma_segunda_diagonal = 0
    
    longitud = len(argumento_matriz) #esta es cantidad de veces que se repite el ciclo for (la cantidad de filas o columnas que es lo mismo)

    #las variables "u" y "y", son para la segunda diagonal, que en cada iteracion "y" aumenta en 1 y "u" disminuye en 1 (para ir sumando los valores correctos de la 2da diagonal)
    u = matriz_filas 
    y = -1
    for i in range(longitud): 
        suma_primera_diagonal += matriz[i][i] #todos los valores de la primera matriz
        suma_segunda_diagonal += matriz[y+1][u-1] 
        #en cada iteracion "y" aumenta en 1 y "u" disminuye en 1
        y += 1
        u -= 1

    print(f"La suma de la primera diagonal es {suma_primera_diagonal}, y la de la segunda diagonal es {suma_segunda_diagonal}")

    if suma_primera_diagonal == suma_segunda_diagonal:
        return True
    
    else:
        return False

if __name__ == "__main__":
    #se pide el numero de filas y columnas de la matriz 
    matriz_filas = int(input("escriba el número de filas que tiene la primera matriz: "))
    matriz_columnas = int(input("escriba el número de columnas que tiene la primera matriz: "))

    #si la matriz no es cuadrada no sera magica
    if matriz_filas != matriz_columnas:
       print("Las matriz debe tener las mismas filas y columnas")

    else:
        matriz = crear_matriz(matriz_filas, matriz_columnas) #se crea la matriz con ayuda de la funcion

        print("La matriz dada es:") #se imprime la matriz con una forma mas "familiar"
        for i in range(len(matriz)):
            print(matriz[i])

        #El return se guarda en cada una de las variables (True or False)
        suma_f = suma_filas(matriz)
        suma_c = suma_columnas(matriz)
        suma_d = suma_diagonales(matriz)

        #Si todos los return son True, entonces significa que la matriz es magica
        if suma_f == True and suma_c == True and suma_d == True:
            print("La matriz dada es una matriz magica")

        else:
            print("La matriz dada NO es una matriz magica")