from entrada import Instancia


def validar(instancia: Instancia) -> list:
    """Revisa que la instancia cumpla las reglas del problema.

    Debe revisar, como mínimo:
        - N >= 1 y M >= 1.
        - Toda ciudad tiene 0 <= x <= N y 0 <= y <= N.
        - No hay dos ciudades en el mismo punto.
        - No hay nombres repetidos.
        - Existe al menos un punto libre (M < (N+1)^2); si no, el
          problema es infactible.

    Args:
        instancia: la instancia ya parseada.

    Returns:
        Lista de mensajes de error legibles. Lista vacía si todo es válido.
        Debe reportar TODOS los errores encontrados, no solo el primero.
    """
    raise NotImplementedError