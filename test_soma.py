from unittest import TestCase, main

from operacoes import soma, sub, mult, div


class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(1, 1), 2)

    def test_sub(self):
        self.assertEqual(sub(2, 2), 0)

    def test_mult(self):
        self.assertEqual(mult(2, 2), 4)

    def test_div(self):
        self.assertEqual(div(2, 2), 1)
