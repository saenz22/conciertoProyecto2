import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from entrada import ErrorEntrada, parsear_entrada


class PruebasParsearEntrada(unittest.TestCase):
    def test_lee_la_entrada_del_enunciado(self) -> None:
        texto = "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\nTulua 0 3\nRioFrio 1 2"
        instancia = parsear_entrada(texto)

        self.assertEqual(instancia.n, 12)
        self.assertEqual(instancia.m, 5)
        self.assertEqual(instancia.ciudades[0].nombre, "Palmira")
        self.assertEqual((instancia.ciudades[-1].x, instancia.ciudades[-1].y), (1, 2))

    def test_rechaza_m_alto_y_lineas_faltantes(self) -> None:
        with self.assertRaises(ErrorEntrada):
            parsear_entrada("10\n2\nA 1 1")

    def test_rechaza_nombre_con_espacios(self) -> None:
        with self.assertRaises(ErrorEntrada):
            parsear_entrada("10\n1\nNueva Ciudad 1 1")

    def test_rechaza_entero_invalido(self) -> None:
        with self.assertRaisesRegex(ErrorEntrada, "entero válido"):
            parsear_entrada("diez\n1\nA 1 1")


if __name__ == "__main__":
    unittest.main()