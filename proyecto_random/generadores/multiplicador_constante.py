def multiplicador_constante(semilla_fija, semilla_variable, n):
    """
    Genera números pseudoaleatorios usando multiplicador constante.
    Semilla fija se mantiene, semilla variable se actualiza.
    Se extraen 4 dígitos centrales como en Cuadrados Medios.
    """
    numeros = []
    x = semilla_variable
    for _ in range(n):
        mult = semilla_fija * x
        # Tomamos los 4 dígitos centrales
        mult_str = str(mult).zfill(8)  # rellena con ceros si es necesario
        centro = int(mult_str[2:6])    # extrae los 4 dígitos centrales
        u = round(centro / 10000, 4)   # normaliza a [0,1]
        numeros.append(u)
        x = centro  # actualizar semilla variable
    return numeros
