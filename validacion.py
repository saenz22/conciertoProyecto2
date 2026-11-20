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
    errores = []

    if instancia.n < 1:
        errores.append("N debe ser al menos 1.")

    if instancia.m < 1:
        errores.append("Debe haber al menos una ciudad (M >= 1).")

    nombres_vistos = set()
    coordenadas_vistas = set()

    for ciudad in instancia.ciudades:
        if not (0 <= ciudad.x <= instancia.n and 0 <= ciudad.y <= instancia.n):
            errores.append(
                f"La ciudad {ciudad.nombre!r} ({ciudad.x}, {ciudad.y}) "
                f"está fuera del cuadrado [0, {instancia.n}]."
            )

        if ciudad.nombre in nombres_vistos:
            errores.append(f"El nombre de ciudad {ciudad.nombre!r} está repetido.")
        else:
            nombres_vistos.add(ciudad.nombre)

        coordenadas = (ciudad.x, ciudad.y)
        if coordenadas in coordenadas_vistas:
            errores.append(
                f"Hay más de una ciudad en el punto "
                f"({ciudad.x}, {ciudad.y})."
            )
        else:
            coordenadas_vistas.add(coordenadas)

    if instancia.n >= 1 and instancia.m >= (instancia.n + 1) ** 2:
        errores.append(
            "No queda ningún punto libre: M debe ser menor que "
            "(N + 1)^2."
        )

    return errores
