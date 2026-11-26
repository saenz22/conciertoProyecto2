import unittest

from entrada import Ciudad, Instancia
from generador import (
    cargar_plantilla,
    formatear_arreglo,
    formatear_arreglo_texto,
    generar_minizinc,
)


class PruebasGenerador(unittest.TestCase):
    # Pruebas del formato de los datos y de la generación de modelos MiniZinc.
    def test_formatea_arreglo_numerico(self):
        # Comprueba la representación de una lista de enteros en MiniZinc.
        self.assertEqual(formatear_arreglo([2, 10, 11]), "[2, 10, 11]")

    def test_escapa_arreglo_de_nombres(self):
        # Comprueba que se escapan las comillas y las barras invertidas de los nombres.
        self.assertEqual(
            formatear_arreglo_texto(['La "Union"', "Rio\\Frio"]),
            '["La \\"Union\\"", "Rio\\\\Frio"]',
        )

    def test_carga_plantilla_y_genera_minizinc(self):
        # Comprueba que la plantilla del proyecto se completa con los datos de la instancia.
        instancia = Instancia(
            12,
            (Ciudad("Palmira", 2, 3), Ciudad("Cali", 10, 2)),
        )

        codigo = generar_minizinc(instancia, cargar_plantilla())

        self.assertIn("int: N = 12;", codigo)
        self.assertIn("array[1..M] of int: ciudadX = [2, 10];", codigo)
        self.assertIn('array[1..M] of string: nombres = ["Palmira", "Cali"];', codigo)
        self.assertNotIn("__", codigo)

    def test_rechaza_plantilla_vacia(self):
        # Comprueba que una plantilla con solo espacios produce un ValueError.
        with self.assertRaisesRegex(ValueError, "vacía"):
            generar_minizinc(Instancia(2, (Ciudad("A", 0, 0),)), "  ")

    def test_detecta_marcador_sin_reemplazar(self):
        # Comprueba que el generador lanza un ValueError si queda un marcador en el modelo.
        instancia = Instancia(2, (Ciudad("A", 0, 0),))

        with self.assertRaisesRegex(ValueError, "marcadores"):
            generar_minizinc(
                instancia,
                "int: N = __N__; int: M = __M__; int: otro = __OTRO__;",
            )


if __name__ == "__main__":
    unittest.main()