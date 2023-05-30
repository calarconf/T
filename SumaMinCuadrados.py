import math

def suma_cuadrados_minima(n):
    # Se crea una lista para almacenar las soluciones parciales
    soluciones = [float('inf')] * (n + 1)
    
    # El caso base: el número 0 no requiere sumar ningún cuadrado
    soluciones[0] = 0
    
    # Calcular las soluciones para todos los números hasta n
    for i in range(1, n + 1):
        # Comprobar si i es un cuadrado perfecto
        if math.isqrt(i) ** 2 == i:
            soluciones[i] = 1
        else:
            # Calcular la solución mínima para i
            for j in range(1, int(math.sqrt(i)) + 1):
                soluciones[i] = min(soluciones[i], 1 + soluciones[i - j**2])
    
    # La solución final se encuentra en soluciones[n]
    return soluciones[n]

# Ejemplo de uso
numero = 27
resultado = suma_cuadrados_minima(numero)
print(f"El número {numero} se puede expresar como la suma de {resultado} cuadrados.")
