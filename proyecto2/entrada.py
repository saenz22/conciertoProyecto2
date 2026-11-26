from dataclasses import dataclass


class ErrorEntrada(Exception):
    # Indica que el texto no cumple el formato de entrada.
    pass


@dataclass(frozen=True)
class Ciudad:
    # Una ciudad ubicada en una intersección entera del plano.
    #
    # Atributos:
    #     nombre: identificador de la ciudad.
    #     x: posición en el eje X (entero).
    #     y: posición en el eje Y (entero).
    nombre: str
    x: int
    y: int


@dataclass(frozen=True)
class Instancia:
    # Una entrada completa del problema.
    #
    # Atributos:
    #     n: lado del cuadrado que representa al departamento (en km).
    #     ciudades: tupla de Ciudad, en el orden en que se leyeron.
    n: int
    ciudades: tuple["Ciudad", ...]

    @property
    def m(self) -> int:
        # Número de ciudades.
        return len(self.ciudades)


def parsear_entrada(texto: str) -> Instancia:
    # Convierte el contenido del TextArea en una Instancia.
    #
    # Formato esperado:
    #     línea 1: entero N
    #     línea 2: entero M
    #     siguientes M líneas: 'nombre x y'
    #
    # Args:
    #     texto: contenido completo del TextArea.
    #
    # Returns:
    #     Instancia: datos de la entrada sin validar las reglas de negocio.
    #
    # Raises:
    #     ErrorEntrada: si faltan líneas, algún número no es entero, o una
    #         línea de ciudad no tiene exactamente 3 campos. El mensaje debe
    #         indicar el número de línea problemática.
    #
    # Las líneas en blanco no son válidas. Los nombres de ciudad deben tener
    # un solo campo, sin espacios.
    if not isinstance(texto, str):
        raise ErrorEntrada("La entrada debe ser texto.")

    lineas = texto.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lineas and lineas[-1].strip() == "":
        lineas.pop()

    if not lineas:
        raise ErrorEntrada("La entrada está vacía.")

    if lineas[0].strip() == "":
        raise ErrorEntrada("La línea 1 debe contener el tamaño N.")
    if len(lineas) < 2:
        raise ErrorEntrada("Falta la línea 2 con el número de ciudades M.")

    n = _leer_entero(lineas[0].strip(), "N", 1)
    m = _leer_entero(lineas[1].strip(), "M", 2)

    if m < 1:
        raise ErrorEntrada("La línea 2 debe contener M mayor o igual que 1.")

    if len(lineas) - 2 != m:
        raise ErrorEntrada(
            f"La línea 2 indica M = {m}, pero se encontraron "
            f"{len(lineas) - 2} líneas de ciudades."
        )

    ciudades = []
    for indice, linea in enumerate(lineas[2:], start=3):
        if linea.strip() == "":
            raise ErrorEntrada(f"La línea {indice} está en blanco.")

        campos = linea.split()
        if len(campos) != 3:
            raise ErrorEntrada(
                f"La línea {indice} debe tener exactamente: nombre x y."
            )

        nombre = campos[0]
        x = _leer_entero(campos[1], "X", indice)
        y = _leer_entero(campos[2], "Y", indice)
        ciudades.append(Ciudad(nombre=nombre, x=x, y=y))

    return Instancia(n=n, ciudades=tuple(ciudades))


def _leer_entero(valor: str, campo: str, numero_linea: int) -> int:
    # Lee un entero y genera un mensaje de error con su posición.
    #
    # Recibe: valor textual, nombre del campo y número de línea.
    # Hace: intenta convertir el valor a entero.
    # Devuelve: el entero leído.
    # Lanza: ErrorEntrada si la conversión falla.
    try:
        return int(valor)
    except ValueError as error:
        raise ErrorEntrada(
            f"La línea {numero_linea} debe contener un entero válido en {campo}; "
            f"se recibió '{valor}'."
        ) from error