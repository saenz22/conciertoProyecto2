from entrada import Instancia

RUTA_PLANTILLA = "plantillas/modelo.mzn.tpl"


def cargar_plantilla(ruta: str = RUTA_PLANTILLA) -> str:
    """Lee el archivo de plantilla del modelo MiniZinc.

    Args:
        ruta: ubicación del archivo .tpl.

    Returns:
        El texto de la plantilla, con sus marcadores sin reemplazar.
    """
    raise NotImplementedError


def formatear_arreglo(valores: list) -> str:
    """Convierte una lista de enteros a sintaxis de arreglo MiniZinc.

    Ejemplo: [2, 10, 11] -> '[2, 10, 11]'

    Args:
        valores: lista de enteros.

    Returns:
        Texto del arreglo, listo para insertar en el modelo.
    """
    raise NotImplementedError


def generar_minizinc(instancia: Instancia, plantilla: str) -> str:
    """Produce el programa MiniZinc completo para una instancia.

    Reemplaza en la plantilla los marcadores de datos (por ejemplo
    __N__, __M__, __CX__, __CY__, __NOMBRES__) por los valores de la
    instancia. El resto del modelo no cambia entre entradas.

    Args:
        instancia: instancia ya validada.
        plantilla: texto devuelto por cargar_plantilla().

    Returns:
        Código MiniZinc listo para copiar y pegar.

    Raises:
        ValueError: si queda algún marcador sin reemplazar.
    """
    raise NotImplementedError