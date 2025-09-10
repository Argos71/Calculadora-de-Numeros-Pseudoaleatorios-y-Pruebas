"""
Generador de números pseudoaleatorios mediante multiplicación de dos semillas.
"""

def multiplicacion_semillas(x0, y0, n):
    """
    Genera una lista de n números pseudoaleatorios usando la multiplicación de dos semillas.
    Similar al método de cuadrados medios:
        - multiplicar x0 * y0
        - tomar los dígitos del medio
        - normalizar en [0,1)
    """
    numeros = []
    x, y = x0, y0
    for _ in range(n):
        prod = x * y
        prod_str = str(prod).zfill(8)  # rellenar con ceros a la izquierda si es necesario
        # Tomar los 4 dígitos centrales
        medio = int(prod_str[2:6])
        numeros.append(medio / 10000)  # normalizar a [0,1)
        # Actualizar semillas: rotar valores
        x, y = y, medio
    return numeros
