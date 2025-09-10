def prueba_uniformidad(numeros, k=10):
    """
    Prueba de uniformidad Chi².
    Retorna valor chi², resultado y tabla detallada por intervalo.
    """
    n = len(numeros)
    intervalos = [0]*k
    for x in numeros:
        idx = min(int(x*k), k-1)
        intervalos[idx] += 1

    freq_esperada = n/k
    chi2_val = sum((f - freq_esperada)**2 / freq_esperada for f in intervalos)
    resultado = "Aceptado" if chi2_val < 16.92 else "Rechazado"

    tabla = []
    for i in range(k):
        inicio = i/k
        fin = (i+1)/k
        tabla.append({
            "intervalo": f"[{inicio:.2f}-{fin:.2f})",
            "frecuencia_observada": intervalos[i],
            "frecuencia_esperada": freq_esperada,
            "diferencia_cuadratica": (intervalos[i]-freq_esperada)**2
        })

    return {"chi2": chi2_val, "resultado": resultado, "tabla": tabla}
