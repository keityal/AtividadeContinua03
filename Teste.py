from unittest import result
from Calculadora import Calculadora
import unittest


class Teste(unittest.TestCase):

    def test_soma(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(1, 1, 'soma')
        self.assertEqual(resultado, 2)

    def test_substracao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(1, 1, 'subtracao')
        self.assertEqual(resultado, 0)

    def test_multiplicacao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(1, 1, 'multiplicacao')
        self.assertEqual(resultado, 1)

    def test_divisao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(100, 10, 'divisao')
        self.assertEqual(resultado, 10)


if __name__ == '__main__':
    unittest.main()
