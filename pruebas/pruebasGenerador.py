import unittest

from entrada import Ciudad, Instancia
from generador import (
    cargar_plantilla,
    formatear_arreglo,
    formatear_arreglo_texto,
    generar_minizinc,
)


class PruebasGenerador(unittest.TestCase):
    def test_formatea_arreglo_numerico(self):
        self.assertEqual(formatear_arreglo([2, 10, 11]), "[2, 10, 11]")

    def test_escapa_arreglo_de_nombres(self):
        self.assertEqual(
            formatear_arreglo_texto(['La "Union"', "Rio\\Frio"]),
            '["La \\"Union\\"", "Rio\\\\Frio"]',
        )

    def test_carga_plantilla_y_genera_minizinc(self):
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
        with self.assertRaisesRegex(ValueError, "vacía"):
            generar_minizinc(Instancia(2, (Ciudad("A", 0, 0),)), "  ")

    def test_detecta_marcador_sin_reemplazar(self):
        instancia = Instancia(2, (Ciudad("A", 0, 0),))

        with self.assertRaisesRegex(ValueError, "marcadores"):
            generar_minizinc(
                instancia,
                "int: N = __N__; int: M = __M__; int: otro = __OTRO__;",
            )


if __name__ == "__main__":
    unittest.main()