# Definir un algoritmo de Fuerza Bruta para encontrar la Suma de Dos Números en una Lista.
# Dada una lista de números y un valor objetivo, encontrar dos números en la lista que sumen el valor objetivo.
numeros = [1, 2, 3, 4, 5, 6]
objetivo = 6

def encontrar_suma(numeros, objetivo):
    for i in range(len(numeros)): 
        for j in range(i+1, len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return numeros[i], numeros[j]
    return None

resultado = encontrar_suma(numeros, objetivo)
if resultado:
    print(f"Los números que suman {objetivo} son: {resultado[0]} y {resultado[1]}")
else:
    print("No se encontraron números que sumen el objetivo.")


