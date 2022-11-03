"""
4. Folosind TDD, rezolvati urmatoarea problema: Sa se scrie o ierarhie de clase pentru
forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc.
FormaGeometrica este interfata, adice clasa abstracta cu doar metode astracte. Metode:
arie(), perimetru().
Sa se mosteneasca interfata, si sa se implementeze cele 2 metode pentru fiecare din
cele 3 forme geometrice.
"""

from abc import ABC, abstractmethod
import pytest


class Formageometrica(ABC):
    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


class Patrat(Formageometrica):
    def __init__(self, latura):
        self.latura = latura

    def arie(self):
        if type(self.latura) is str:
            return "Error! Not necessary a string"
        if self.latura < 0:
            return "Error! the value must be positive"
        if self.latura == 0:
            return "Error! Zero not allowed"
        return self.latura ** 2

    def perimetru(self):
        if type(self.latura) is str:
            return "Error! Not necessary a string"
        if self.latura < 0:
            return "Error! the value must be positive"
        if self.latura == 0:
            return "Error! Zero not allowed"
        return self.latura * 4


class Dreptunghi(Formageometrica):
    def __init__(self, latime, lungime):
        self.latime = latime
        self.lungime = lungime

    def arie(self):
        if type(self.latime) is str or type(self.lungime) is str:
            return "Error! Not necessary a string"
        if self.latime == 0 or self.lungime == 0:
            return "Error! Zero not allowed"
        if self.latime < 0 or self.lungime < 0:
            return "Error! the value must be positive"

        return self.latime * self.lungime

    def perimetru(self):
        if type(self.latime) is str or type(self.lungime) is str:
            return "Error! Not necessary a string"
        if self.latime == 0 or self.lungime == 0:
            return "Error! Zero not allowed"
        if self.latime < 0 or self.lungime < 0:
            return "Error! the value must be positive"

        return (self.latime * 2) + (self.lungime * 2)


class Cerc(Formageometrica):
    def __init__(self, raza):
        self.raza = raza

    def arie(self):
        pi = 3.14
        if type(self.raza) is str:
            return "Error! Not necessary a string"
        if self.raza < 0:
            return "Error! the value must be positive"
        if self.raza == 0:
            return "Error! Zero not allowed"
        return pi * self.raza ** 2

    def perimetru(self):
        pi = 3.14
        if type(self.raza) is str:
            return "Error! Not necessary a string"
        if self.raza < 0:
            return "Error! the value must be positive"
        if self.raza == 0:
            return "Error! Zero not allowed"
        return 2 * pi * self.raza


class Test_FormeGeometrice():
    def test_patrat_when_aria_calculated_result_returned(self):
        patrat = Patrat(5)
        expected = 25
        actual = patrat.arie()
        assert expected == actual

    def test_patrat_when_aria_calculated_negative_value_returned_error(self):
        patrat = Patrat(-5)
        expected = "Error! the value must be positive"
        actual = patrat.arie()
        assert expected == actual

    def test_patrat_when_aria_calculated_null_value_returned_error(self):
        patrat = Patrat(0)
        expected = "Error! Zero not allowed"
        actual = patrat.arie()
        assert expected == actual

    def test_patrat_when_aria_calculated_is_string(self):
        patrat = Patrat('abc')
        expected = "Error! Not necessary a string"
        actual = patrat.arie()
        assert expected == actual

    def test_patrat_when_perimetrul_calculated_result_returned(self):
        patrat = Patrat(5)
        expected = 20
        actual = patrat.perimetru()
        assert expected == actual

    def test_patrat_when_perimetrul_calculated_negative_value_returned_error(self):
        patrat = Patrat(-5)
        expected = "Error! the value must be positive"
        actual = patrat.perimetru()
        assert expected == actual

    def test_patrat_when_perimetrul_calculated_null_value_returned_error(self):
        patrat = Patrat(0)
        expected = "Error! Zero not allowed"
        actual = patrat.perimetru()
        assert expected == actual

    def test_patrat_when_perimetrul_calculated_is_string(self):
        patrat = Patrat('abc')
        expected = "Error! Not necessary a string"
        actual = patrat.perimetru()
        assert expected == actual

    def test_dreptunghi_when_aria_parameters_are_positive_numbers(self):
        dreptunghi = Dreptunghi(10, 20)
        expected = 200
        actual = dreptunghi.arie()
        assert expected == actual

    def test_dreptunghi_when_aria_parameters_are_negative_numbers(self):
        dreptunghi = Dreptunghi(-10, -20)
        expected = "Error! the value must be positive"
        actual = dreptunghi.arie()
        assert expected == actual

    def test_dreptunghi_when_aria_parameters_are_string(self):
        dreptunghi = Dreptunghi("a", 15)
        expected = "Error! Not necessary a string"
        actual = dreptunghi.arie()
        assert expected == actual

    def test_dreptunghi_when_aria_parameters_are_null(self):
        dreptunghi = Dreptunghi(0, 0)
        expected = "Error! Zero not allowed"
        actual = dreptunghi.arie()
        assert expected == actual

    def test_dreptunghi_when_perimetrul_parameters_are_positive_numbers(self):
        dreptunghi = Dreptunghi(10, 20)
        expected = 60
        actual = dreptunghi.perimetru()
        assert expected == actual

    def test_dreptunghi_when_perimetrul_parameters_are_negative_numbers(self):
        dreptunghi = Dreptunghi(-10, -20)
        expected = "Error! the value must be positive"
        actual = dreptunghi.perimetru()
        assert expected == actual

    def test_dreptunghi_when_perimetrul_parameters_are_string(self):
        dreptunghi = Dreptunghi("a", 15)
        expected = "Error! Not necessary a string"
        actual = dreptunghi.perimetru()
        assert expected == actual

    def test_dreptunghi_when_perimetrul_parameters_are_null(self):
        dreptunghi = Dreptunghi(0, 25)
        expected = "Error! Zero not allowed"
        actual = dreptunghi.perimetru()
        assert expected == actual

    def test_cerc_when_aria_calculated_result_returned(self):
        cerc = Cerc(5)
        expected = 78.5
        actual = pytest.approx(cerc.arie())
        assert expected == actual

    def test_cerc_when_aria_calculated_negative_value_returned_error(self):
        cerc = Cerc(-5)
        expected = "Error! the value must be positive"
        actual = cerc.arie()
        assert expected == actual

    def test_cerc_when_aria_calculated_null_value_returned_error(self):
        cerc = Cerc(0)
        expected = "Error! Zero not allowed"
        actual = cerc.arie()
        assert expected == actual

    def test_cerc_when_aria_calculated_is_string(self):
        cerc = Cerc('abc')
        expected = "Error! Not necessary a string"
        actual = cerc.arie()
        assert expected == actual

    def test_cerc_when_perimetrul_calculated_result_returned(self):
        cerc = Cerc(5)
        expected = 31.4
        actual = pytest.approx(cerc.perimetru())
        assert expected == actual

    def test_cerc_when_perimetrul_calculated_negative_value_returned_error(self):
        cerc = Cerc(-5)
        expected = "Error! the value must be positive"
        actual = cerc.perimetru()
        assert expected == actual

    def test_cerc_when_perimetrul_calculated_null_value_returned_error(self):
        cerc = Cerc(0)
        expected = "Error! Zero not allowed"
        actual = cerc.perimetru()
        assert expected == actual

    def test_cerc_when_perimetrul_calculated_is_string(self):
        cerc = Cerc('abc')
        expected = "Error! Not necessary a string"
        actual = cerc.perimetru()
        assert expected == actual
