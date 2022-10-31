"""
Alegeti 2 clase din cele implementate la tema anterior, si scrieti unit teste pentru toate
metodele folosind unittest.
"""

import unittest
from tema_6 import clasa_angajat
from tema_6 import clasa_cerc

angajat = clasa_angajat.Angajat("Alexandru", "Roian", 2100)
cerc = clasa_cerc.Cerc(20, "rosie")


class Test_1(unittest.TestCase):

    def test_descriere_angajat(self):
        self.assertEqual(angajat.descriere(), "Nume: Alexandru, Prenume: Roian, Salariu: 2100")

    def test_nume_complet(self):
        self.assertEqual(angajat.nume_complet(), "Alexandru Roian")

    def test_salariu(self):
        self.assertEqual(angajat.salariu_lunar(), "salariul lunar 2100")

    def test_salariu_anul(self):
        self.assertEqual(angajat.salariul_anual(), "Salariul anual este 25200")

    def test_marire_salariu(self):
        self.assertEqual(angajat.marire_salariu(10), 2310)


class Test_2(unittest.TestCase):
    def test_descriere_cerc(self):
        self.assertEqual(cerc.descriere_cerc(), "Raza cercului este 20,culoarea rosie ")

    def test_aria_cerc(self):
        self.assertEqual(cerc.aria(), "Aria cercului 1256.0")

    def test_diametrul_cerc(self):
        self.assertEqual(cerc.diametrul(),"Diametrul cercului 40")

    def test_circumferinta_cerc(self):
        self.assertAlmostEqual(cerc.circumferinta(),125.60,places=2)