#3. Alegeti una din temele de mai sus, si convertiti testele din unittest in pytest

import pytest
from tema_6 import clasa_angajat
from tema_6 import clasa_cerc

angajat = clasa_angajat.Angajat("Alexandru", "Roian", 2100)
cerc = clasa_cerc.Cerc(20, "rosie")


class Test_1():

    def test_descriere_angajat(self):
       assert angajat.descriere() == "Nume: Alexandru, Prenume: Roian, Salariu: 2100"

    def test_nume_complet(self):
        assert angajat.nume_complet() == "Alexandru Roian"

    def test_salariu(self):
        assert angajat.salariu_lunar() == "salariul lunar 2100"

    def test_salariu_anul(self):
       assert angajat.salariul_anual() ==  "Salariul anual este 25200"

    def test_marire_salariu(self):
        assert angajat.marire_salariu(10) == 2310


class Test_2():
    def test_descriere_cerc(self):
        assert cerc.descriere_cerc() == "Raza cercului este 20,culoarea rosie "

    def test_aria_cerc(self):
       assert cerc.aria() == "Aria cercului 1256.0"

    def test_diametrul_cerc(self):
        assert cerc.diametrul() == "Diametrul cercului 40"

    def test_circumferinta_cerc(self):
        assert cerc.circumferinta() == pytest.approx(125.60)

