import math
from scipy.stats import chi2

def prueba_varianza(numeros, confianza=0.95):
    """
    Calcula varianza y verifica si está dentro del intervalo de confianza
    para números pseudoaleatorios uniformes [0,1].
    Límites calculados dinámicamente según tamaño de muestra n usando Chi².
    """
    n = len(numeros)
    media = sum(numeros)/n
    varianza = sum((x - media)**2 for x in numeros)/n

    # Nivel de significancia alfa
    alfa = 1 - confianza
    chi2_inf = chi2.ppf(alfa/2, df=n-1)
    chi2_sup = chi2.ppf(1-alfa/2, df=n-1)

    limite_inferior = round((n-1)*varianza / chi2_sup, 4)
    limite_superior = round((n-1)*varianza / chi2_inf, 4)

    resultado = "Aceptado" if limite_inferior <= varianza <= limite_superior else "Rechazado"
    diferencia = varianza - 1/12  # diferencia con valor esperado teórico

    tabla = [{
        "nombre": "Varianza",
        "valor": round(varianza, 4),
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "diferencia": round(diferencia, 4),
        "resultado": resultado
    }]

    return {"valor": varianza, "resultado": resultado, "tabla": tabla}
