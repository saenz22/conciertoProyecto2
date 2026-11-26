import unittest

from entrada import Ciudad, ErrorEntrada, Instancia, parsear_entrada


class PruebasEntrada(unittest.TestCase):
    # Pruebas del formato de entrada y de los números de línea en los errores.
    def test_ejemplo_del_enunciado(self):
        # Comprueba que el ejemplo se convierte en la instancia esperada.
        instancia = parsear_entrada(
            "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\n"
            "Tulua 0 3\nRioFrio 1 2\n"
        )

        self.assertEqual(
            instancia,
            Instancia(
                12,
                (
                    Ciudad("Palmira", 2, 3),
                    Ciudad("Cali", 10, 2),
                    Ciudad("Buga", 11, 0),
                    Ciudad("Tulua", 0, 3),
                    Ciudad("RioFrio", 1, 2),
                ),
            ),
        )

    def test_ignora_espacios_y_lineas_en_blanco(self):
        # Comprueba que el lector admite espacios alrededor de los datos y líneas vacías.
        instancia = parsear_entrada(" 12 \n\n 1 \n\n Palmira 2 3 \n\n")

        self.assertEqual(instancia.ciudades, (Ciudad("Palmira", 2, 3),))

    def test_errores_indican_linea(self):
        # Comprueba que los errores de formato indican la línea correspondiente.
        casos = (
            ("", "Línea 1"),
            ("12", "Línea 2"),
            ("abc\n1\nCiudad 0 0", "Línea 1"),
            ("12\nabc", "Línea 2"),
            (
                "12\n5\nCiudad1 0 0\nCiudad2 0 0\nCiudad3 0 0\nCiudad4 0 0",
                "Línea 7",
            ),
            ("12\n1\nCiudad 0", "Línea 3"),
            ("12\n1\nCiudad 2.5 0", "Línea 3"),
            ("12\n1\nLa Unión 1 9", "Línea 3"),
            ("12\n0\nCiudad 0 0", "Línea 3"),
            ("12\n1\nCiudad 0 0\nOtra 1 1", "Línea 4"),
        )
        for texto, linea in casos:
            with self.subTest(texto=texto):
                with self.assertRaisesRegex(ErrorEntrada, linea):
                    parsear_entrada(texto)

    def test_coordenadas_no_enteras_reportan_linea_original(self):
        # Comprueba que una coordenada inválida se reporta en su línea original aunque haya líneas vacías.
        with self.assertRaisesRegex(ErrorEntrada, "Línea 5"):
            parsear_entrada("12\n\n1\n\nCiudad x 0\n")

    def test_acepta_n_y_m_negativos_para_validacion_posterior(self):
        # Comprueba que el análisis admite N y M negativos y construye una instancia sin ciudades.
        instancia = parsear_entrada("-1\n-2\n")

        self.assertEqual(instancia.n, -1)
        self.assertEqual(instancia.ciudades, ())


if __name__ == "__main__":
    unittest.main()