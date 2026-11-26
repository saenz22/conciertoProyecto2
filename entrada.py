# Es el modelo de la entrada de datos, contiene los atributos y métodos necesarios para manejar la información de entrada.
# También contiene el parser

from dataclasses import dataclass


class ErrorEntrada(Exception):
    # Se lanza cuando el texto de entrada no tiene el formato esperado.
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
    ciudades: tuple

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
    #     La Instancia leída (todavía sin validar reglas de negocio).
    #
    # Raises:
    #     ErrorEntrada: si faltan líneas, algún número no es entero, o una
    #         línea de ciudad no tiene exactamente 3 campos. El mensaje debe
    #         indicar el número de línea problemática.
    #
    # Las líneas en blanco se ignoran, conservando su posición original para
    # los mensajes de error. Los nombres deben ser una sola palabra.
    lineas = [
        (numero, contenido.strip())
        for numero, contenido in enumerate(texto.splitlines(), start=1)
        if contenido.strip()
    ]

    if not lineas:
        raise ErrorEntrada("Línea 1: falta el valor de N.")

    numero_n, texto_n = lineas[0]
    try:
        n = int(texto_n)
    except ValueError as error:
        raise ErrorEntrada(
            f"Línea {numero_n}: N debe ser un número entero."
        ) from error

    if len(lineas) < 2:
        raise ErrorEntrada("Línea 2: falta el valor de M.")

    numero_m, texto_m = lineas[1]
    try:
        m = int(texto_m)
    except ValueError as error:
        raise ErrorEntrada(
            f"Línea {numero_m}: M debe ser un número entero."
        ) from error

    cantidad_ciudades_esperada = max(m, 0)
    lineas_ciudades = lineas[2:]
    if len(lineas_ciudades) < cantidad_ciudades_esperada:
        numero_faltante = len(texto.splitlines()) + 1
        raise ErrorEntrada(
            f"Línea {numero_faltante}: faltan ciudades; "
            f"se esperaban {cantidad_ciudades_esperada}."
        )
    if len(lineas_ciudades) > cantidad_ciudades_esperada:
        numero_extra = lineas_ciudades[cantidad_ciudades_esperada][0]
        raise ErrorEntrada(
            f"Línea {numero_extra}: hay más ciudades de las indicadas por M."
        )

    ciudades = []
    for numero, linea in lineas_ciudades:
        campos = linea.split()
        if len(campos) != 3:
            raise ErrorEntrada(
                f"Línea {numero}: cada ciudad debe tener exactamente "
                "3 campos (nombre, x, y)."
            )

        nombre, texto_x, texto_y = campos
        try:
            x = int(texto_x)
            y = int(texto_y)
        except ValueError as error:
            raise ErrorEntrada(
                f"Línea {numero}: las coordenadas x e y deben ser "
                "números enteros."
            ) from error
        ciudades.append(Ciudad(nombre, x, y))

    return Instancia(n, tuple(ciudades))