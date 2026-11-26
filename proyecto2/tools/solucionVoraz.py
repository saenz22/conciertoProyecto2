def resolver_fuerza_bruta(instancia, criterio: str):
    # Evalúa todos los puntos libres del cuadrado usando distancias Manhattan.
    #
    # Entrada: instancia con el tamaño del cuadrado y al menos una ciudad.
    # Criterio: minimax minimiza la distancia máxima, rango minimiza la
    #            diferencia entre la máxima y la mínima, suma minimiza la suma,
    #            y minimax_rango usa el rango para desempatar la distancia máxima.
    # Salida: lista de pares (x, y) óptimos, incluidos los empates.
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