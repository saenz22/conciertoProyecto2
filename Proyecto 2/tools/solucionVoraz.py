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
    raise NotImplementedError