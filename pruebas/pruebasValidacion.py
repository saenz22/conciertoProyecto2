import unittest

from entrada import Ciudad, Instancia
from validacion import validar


class PruebasValidacion(unittest.TestCase):
    def test_instancia_valida(self):
        instancia = Instancia(
            3,
            (Ciudad("Cali", 0, 0), Ciudad("Buga", 3, 3)),
        )

        self.assertEqual(validar(instancia), [])

    def test_reporta_n_y_m_invalidos(self):
        self.assertEqual(
            validar(Instancia(0, ())),
            ["N debe ser al menos 1.", "Debe haber al menos una ciudad (M >= 1)."],
        )

    def test_reporta_coordenada_fuera_del_cuadrado(self):
        errores = validar(Instancia(2, (Ciudad("Cali", 3, -1),)))

        self.assertEqual(len(errores), 1)
        self.assertIn("Cali", errores[0])
        self.assertIn("fuera del cuadrado", errores[0])

    def test_reporta_nombres_y_puntos_repetidos(self):
        instancia = Instancia(
            2,
            (Ciudad("Cali", 0, 0), Ciudad("Cali", 1, 1), Ciudad("Buga", 0, 0)),
        )

        errores = validar(instancia)

        self.assertEqual(len(errores), 2)
        self.assertTrue(any("nombre de ciudad" in error for error in errores))
        self.assertTrue(any("punto (0, 0)" in error for error in errores))

    def test_reporta_instancia_sin_puntos_libres(self):
        ciudades = tuple(
            Ciudad(f"Ciudad{i}", i % 2, i // 2)
            for i in range(4)
        )

        errores = validar(Instancia(1, ciudades))

        self.assertEqual(len(errores), 1)
        self.assertIn("No queda ningún punto libre", errores[0])

    def test_acumula_errores_en_una_sola_validacion(self):
        instancia = Instancia(
            1,
            (
                Ciudad("Cali", 2, 0),
                Ciudad("Cali", 0, 0),
                Ciudad("Buga", 1, 1),
                Ciudad("Palmira", 1, 0),
            ),
        )

        errores = validar(instancia)

        self.assertEqual(len(errores), 3)
        self.assertTrue(any("fuera del cuadrado" in error for error in errores))
        self.assertTrue(any("nombre de ciudad" in error for error in errores))
        self.assertTrue(any("No queda ningún punto libre" in error for error in errores))


if __name__ == "__main__":
    unittest.main()
