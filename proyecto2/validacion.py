from entrada import Ciudad, Instancia


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
        errores.append("N debe ser mayor o igual que 1.")

    if instancia.m < 1:
        errores.append("M debe ser mayor o igual que 1.")

    puntos = set()
    nombres = set()
    for indice, ciudad in enumerate(instancia.ciudades, start=1):
        if not ciudad.nombre or ciudad.nombre.strip() == "":
            errores.append(f"La ciudad {indice} debe tener nombre.")
        elif ciudad.nombre in nombres:
            errores.append(f"El nombre de ciudad '{ciudad.nombre}' está repetido.")
        nombres.add(ciudad.nombre)

        if ciudad.x < 0 or ciudad.x > instancia.n:
            errores.append(
                f"La ciudad '{ciudad.nombre}' tiene X = {ciudad.x}; "
                f"debe estar entre 0 y {instancia.n}."
            )
        if ciudad.y < 0 or ciudad.y > instancia.n:
            errores.append(
                f"La ciudad '{ciudad.nombre}' tiene Y = {ciudad.y}; "
                f"debe estar entre 0 y {instancia.n}."
            )

        punto = (ciudad.x, ciudad.y)
        if punto in puntos:
            errores.append(
                f"Hay ciudades repetidas en la posición ({ciudad.x}, {ciudad.y})."
            )
        puntos.add(punto)

    cantidad_puntos = (instancia.n + 1) * (instancia.n + 1)
    if instancia.m >= cantidad_puntos:
        errores.append(
            "No existe ningún punto libre para el concierto: todas las "
            f"{cantidad_puntos} posiciones están ocupadas."
        )

    return errores