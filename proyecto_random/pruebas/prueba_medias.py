import math

def prueba_medias(numeros, confianza=0.95):
    """
    Calcula media y verifica si está dentro del intervalo de confianza
    para la media de números pseudoaleatorios uniformes [0,1].
    Límites calculados dinámicamente según tamaño de muestra n.
    """
    n = len(numeros)
    media = sum(numeros)/n

    # Valor crítico z para 95% de confianza
    z = 1.96  # para confianza del 95%
    std_error = 1 / math.sqrt(12*n)  # desviación estándar de la media
    limite_inferior = round(0.5 - z * std_error, 4)
    limite_superior = round(0.5 + z * std_error, 4)

    resultado = "Aceptado" if limite_inferior <= media <= limite_superior else "Rechazado"
    diferencia = media - 0.5

    tabla = [{
        "nombre": "Media",
        "valor": round(media, 4),
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "diferencia": round(diferencia, 4),
        "resultado": resultado
    }]

    return {"valor": media, "resultado": resultado, "tabla": tabla}
