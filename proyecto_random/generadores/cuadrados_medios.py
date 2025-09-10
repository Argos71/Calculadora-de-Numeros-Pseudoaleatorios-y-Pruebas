"""
Generador de números pseudoaleatorios usando el algoritmo de Cuadrados Medios.
"""

def cuadrados_medios(semilla, n):
    numeros = []
    valor = semilla
    for _ in range(n):
        cuadrado = str(valor ** 2).zfill(8)  # cuadrado con relleno de ceros
        valor = int(cuadrado[2:6])  # tomar los 4 dígitos del medio
        numeros.append(valor / 10000)  # normalizar en [0,1)
    return numeros
