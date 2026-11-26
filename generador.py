from pathlib import Path
import re

from entrada import Instancia

RUTA_PLANTILLA = str(
    Path(__file__).resolve().parent / "plantillas" / "modelo.mzn.tpl"
)


def cargar_plantilla(ruta: str = RUTA_PLANTILLA) -> str:
    # Lee el archivo de plantilla del modelo MiniZinc.
    #
    # Args:
    #     ruta: ubicación del archivo .tpl.
    #
    # Returns:
    #     El texto de la plantilla, con sus marcadores sin reemplazar.
    try:
        plantilla = Path(ruta).read_text(encoding="utf-8")
    except OSError as error:
        raise OSError(
            f"No se pudo leer la plantilla MiniZinc en '{ruta}'."
        ) from error
    if not plantilla.strip():
        raise ValueError(f"La plantilla MiniZinc en '{ruta}' está vacía.")
    return plantilla


def formatear_arreglo(valores: list) -> str:
    # Convierte una lista de enteros a sintaxis de arreglo MiniZinc.
    #
    # Ejemplo: [2, 10, 11] -> '[2, 10, 11]'
    #
    # Args:
    #     valores: lista de enteros.
    #
    # Returns:
    #     Texto del arreglo, listo para insertar en el modelo.
    return "[" + ", ".join(str(valor) for valor in valores) + "]"


def formatear_arreglo_texto(valores: list[str]) -> str:
    # Escapa comillas y barras invertidas para representar cadenas en MiniZinc.
    #
    # Entrada: valores, lista de cadenas.
    # Salida: texto con el arreglo de cadenas en sintaxis MiniZinc.
    elementos = []
    for valor in valores:
        escapado = valor.replace("\\", "\\\\").replace('"', '\\"')
        elementos.append(f'"{escapado}"')
    return "[" + ", ".join(elementos) + "]"


def generar_minizinc(instancia: Instancia, plantilla: str) -> str:
    # Produce el programa MiniZinc completo para una instancia.
    #
    # Reemplaza en la plantilla los marcadores de datos (por ejemplo
    # __N__, __M__, __CX__, __CY__, __NOMBRES__) por los valores de la
    # instancia. El resto del modelo no cambia entre entradas.
    #
    # Args:
    #     instancia: instancia ya validada.
    #     plantilla: texto devuelto por cargar_plantilla().
    #
    # Returns:
    #     Código MiniZinc listo para copiar y pegar.
    #
    # Raises:
    #     ValueError: si queda algún marcador sin reemplazar.
    if not plantilla.strip():
        raise ValueError("La plantilla MiniZinc está vacía.")

    x_ciudades = [ciudad.x for ciudad in instancia.ciudades]
    y_ciudades = [ciudad.y for ciudad in instancia.ciudades]
    nombres = [ciudad.nombre for ciudad in instancia.ciudades]

    reemplazos = {
        "__N__": str(instancia.n),
        "__M__": str(instancia.m),
        "__CX__": formatear_arreglo(x_ciudades),
        "__CY__": formatear_arreglo(y_ciudades),
        "__NOMBRES__": formatear_arreglo_texto(nombres),
    }

    codigo = plantilla
    for marcador, valor in reemplazos.items():
        codigo = codigo.replace(marcador, valor)

    marcadores = sorted(set(re.findall(r"__[A-Z]+__", codigo)))
    if marcadores:
        raise ValueError(
            "Quedaron marcadores sin reemplazar: " + ", ".join(marcadores)
        )
    return codigo