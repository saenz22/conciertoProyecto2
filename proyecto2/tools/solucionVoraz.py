def resolver_fuerza_bruta(instancia, criterio: str):
    """Busca el punto óptimo probando todos los (N+1)^2 puntos.

    SOLO para verificar las respuestas de MiniZinc en el informe de
    pruebas. No se importa desde la aplicación.

    Args:
        instancia: la Instancia a resolver.
        criterio: 'minimax', 'rango', 'suma' o 'minimax_rango'.

    Returns:
        Lista con TODOS los puntos óptimos (x, y), para poder ver empates.
    """
    criterios_validos = {"minimax", "rango", "suma", "minimax_rango"}
    if criterio not in criterios_validos:
        raise ValueError(
            f"Criterio inválido. Opciones válidas: {sorted(criterios_validos)}."
        )

    mejores = []
    mejor_valor = None

    for x in range(instancia.n + 1):
        for y in range(instancia.n + 1):
            if any(ciudad.x == x and ciudad.y == y for ciudad in instancia.ciudades):
                continue

            distancias = [
                abs(x - ciudad.x) + abs(y - ciudad.y)
                for ciudad in instancia.ciudades
            ]
            distancia_maxima = max(distancias)
            distancia_minima = min(distancias)
            rango = distancia_maxima - distancia_minima
            suma = sum(distancias)

            if criterio == "minimax":
                valor = (distancia_maxima,)
            elif criterio == "rango":
                valor = (rango,)
            elif criterio == "suma":
                valor = (suma,)
            else:
                valor = (distancia_maxima, rango)

            if mejor_valor is None or valor < mejor_valor:
                mejor_valor = valor
                mejores = [(x, y)]
            elif valor == mejor_valor:
                mejores.append((x, y))

    return mejores