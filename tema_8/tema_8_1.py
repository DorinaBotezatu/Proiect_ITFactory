"""
1. Alegeti 3 functii din cele implementate la tema anterior, si scrieti unit tests pentru ele
folosind unittest.
"""
from tema_5.tema_5_obligatoriu import suma
from tema_5.tema_5_obligatoriu import aria_cerc
from tema_5.tema_5_obligatoriu import par_impar

import unittest

class Test_1(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(10,20), 30)
        self.assertNotEqual(suma(15,15),40)
        self.assertEqual(suma(-10,20), 10)

    def test_aria_cerc(self):
        self.assertEqual(aria_cerc(10), 314)
        self.assertAlmostEqual(aria_cerc(2),12.56)

    def test_par_impar(self):
        self.assertEqual(par_impar(20), True)
        self.assertEqual(par_impar(11), False)