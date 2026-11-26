import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from entrada import Ciudad, Instancia
from generador import cargar_plantilla, formatear_arreglo, generar_minizinc


class PruebasGenerador(unittest.TestCase):
    # Pruebas del formato de los datos y de la generación de modelos MiniZinc.
    def test_formatea_arreglo(self) -> None:
        # Comprueba la representación de una lista de enteros en MiniZinc.
        self.assertEqual(formatear_arreglo([2, 10, 11]), "[2, 10, 11]")

    def test_genera_minizinc_completo(self) -> None:
        # Comprueba que el modelo generado incorpora los datos de la instancia y sustituye los marcadores.
        instancia = Instancia(
            n=12,
            ciudades=(
                Ciudad("Palmira", 2, 3),
                Ciudad("Cali", 10, 2),
            ),
        )
        plantilla = cargar_plantilla()
        codigo = generar_minizinc(instancia, plantilla)

        self.assertIn("int: N = 12;", codigo)
        self.assertIn("array[1..M] of int: ciudadX = [2, 10];", codigo)
        self.assertNotIn("__", codigo)

    def test_detecta_marcador_sin_reemplazar(self) -> None:
        # Comprueba que el generador lanza un ValueError si queda un marcador en el modelo.
        instancia = Instancia(n=2, ciudades=(Ciudad("A", 0, 0),))
        with self.assertRaisesRegex(ValueError, "marcadores"):
            generar_minizinc(
                instancia,
                "int: N = __N__; int: M = __M__; int: otro = __OTRO__;",
            )


if __name__ == "__main__":
    unittest.main()