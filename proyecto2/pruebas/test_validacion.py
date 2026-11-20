import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from entrada import Ciudad, Instancia
from tools.solucionVoraz import resolver_fuerza_bruta
from validacion import validar


class PruebasValidacion(unittest.TestCase):
    def test_instancia_valida(self) -> None:
        instancia = Instancia(
            n=5,
            ciudades=(Ciudad("A", 1, 1), Ciudad("B", 4, 3)),
        )
        self.assertEqual(validar(instancia), [])

    def test_reporta_todos_los_errores(self) -> None:
        instancia = Instancia(
            n=2,
            ciudades=(
                Ciudad("A", -1, 3),
                Ciudad("A", -1, 3),
                Ciudad("C", 5, -2),
            ),
        )
        errores = validar(instancia)

        self.assertGreaterEqual(len(errores), 5)
        self.assertTrue(any("repetido" in error for error in errores))
        self.assertTrue(any("repetidas" in error for error in errores))

    def test_rechaza_cuadrado_sin_punto_libre(self) -> None:
        puntos = tuple(
            Ciudad(f"C{i}", x, y)
            for i, (x, y) in enumerate(
                ((0, 0), (0, 1), (1, 0), (1, 1))
            )
        )
        errores = validar(Instancia(n=1, ciudades=puntos))
        self.assertTrue(any("ningún punto libre" in error for error in errores))

    def test_verificador_de_fuerza_bruta_encuentra_empate(self) -> None:
        instancia = Instancia(n=2, ciudades=(Ciudad("A", 1, 1),))
        puntos = resolver_fuerza_bruta(instancia, "minimax")
        self.assertIn((0, 1), puntos)
        self.assertTrue(all(
            punto not in {(1, 1)} for punto in puntos
        ))


if __name__ == "__main__":
    unittest.main()