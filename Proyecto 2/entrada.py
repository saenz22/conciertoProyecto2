# Es el modelo de la entrada de datos, contiene los atributos y métodos necesarios para manejar la información de entrada.
# También contiene el parser

from dataclasses import dataclass


class ErrorEntrada(Exception):
    """Se lanza cuando el texto de entrada no tiene el formato esperado."""


@dataclass(frozen=True)
class Ciudad:
    """Una ciudad ubicada en una intersección entera del plano.

    Atributos:
        nombre: identificador de la ciudad.
        x: posición en el eje X (entero).
        y: posición en el eje Y (entero).
    """
    nombre: str
    x: int
    y: int


@dataclass(frozen=True)
class Instancia:
    """Una entrada completa del problema.

    Atributos:
        n: lado del cuadrado que representa al departamento (en km).
        ciudades: tupla de Ciudad, en el orden en que se leyeron.
    """
    n: int
    ciudades: tuple

    @property
    def m(self) -> int:
        """Número de ciudades."""
        return len(self.ciudades)


def parsear_entrada(texto: str) -> Instancia:
    """Convierte el contenido del TextArea en una Instancia.

    Formato esperado:
        línea 1: entero N
        línea 2: entero M
        siguientes M líneas: 'nombre x y'

    Args:
        texto: contenido completo del TextArea.

    Returns:
        La Instancia leída (todavía sin validar reglas de negocio).

    Raises:
        ErrorEntrada: si faltan líneas, algún número no es entero, o una
            línea de ciudad no tiene exactamente 3 campos. El mensaje debe
            indicar el número de línea problemática.

    Decisión pendiente: ¿qué pasa con líneas en blanco y con nombres
    que contengan espacios? Documenten lo que decidan.
    """
    raise NotImplementedError