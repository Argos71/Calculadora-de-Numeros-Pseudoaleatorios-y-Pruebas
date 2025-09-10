"""
Módulo para exportar resultados a un archivo de texto.
"""

def exportar_resultados(nombre_archivo, resultados):
    with open(nombre_archivo, "w") as f:
        for clave, valor in resultados.items():
            f.write(f"{clave}: {valor}\n")
