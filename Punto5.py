"""
5.Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva
tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor,
 y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
"""
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