def calcular_poblacion(region):
    return sum(region)

def encontrar_region_mayor_poblacion(regiones):
    if len(regiones) == 1:
        return regiones[0]
    
    mitad = len(regiones) // 2
    izquierda = encontrar_region_mayor_poblacion(regiones[:mitad])
    derecha = encontrar_region_mayor_poblacion(regiones[mitad:])
    
    if calcular_poblacion(izquierda) > calcular_poblacion(derecha):
        return izquierda
    else:
        return derecha

# Ejemplo
regiones = [
    [417, 346, 420, 432], [294, 308, 371, 452], [393, 333, 108, 246], 
    [376, 136, 213, 174], [434, 422, 247, 307], [314, 272, 204, 293], 
    [480, 186, 304, 223], [436, 426, 444, 366], [108, 150, 495, 418], 
    [395, 491, 307, 422]
]

region_mayor_poblacion = encontrar_region_mayor_poblacion(regiones)
poblacion_mayor = calcular_poblacion(region_mayor_poblacion)

print("Región con mayor población:", region_mayor_poblacion)
print("Población:", poblacion_mayor)

# La tecnica que utilice es "Divide y venceras". Esta tecnica fue elegida porque permite dividir el problema en subproblemas mas pequenos,
# resolver cada subproblema de manera recursiva y luego combinar las soluciones para obtener la solución final. 
# Ademas es mas eficiente que el algoritmo de fuerza bruta, porque reduce el tamano del problema en cada paso.

