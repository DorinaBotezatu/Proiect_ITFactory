from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @classmethod
    def descrie(self):
        print("Cel mai probabil am colturi")

    @abstractmethod
    def aria(self):
        print('1')


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def get_latura(self):
        return self.__latura

    def set_latura(self, value):
        self.__latura = value

    def del_latura(self):
        del self.__latura

    def aria(self):
        return self.__latura ** 2

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, value):
        self.__raza = value

    def del_raza(self):
        del self.__raza


    def aria(self):
        return self.PI*self.__raza ** 2

    def descrie(self):
       print('Eu nu am colturi')


"""patrat = Patrat(10)
print(patrat.aria())
print(patrat.get_latura())
print(patrat.set_latura(15))
print(patrat.get_latura())
print(patrat.del_latura())
patrat.descrie()
print("====================")
cerc = Cerc(20)
cerc.descrie()
print(cerc.get_raza())
print(cerc.aria())
print(cerc.set_raza(30))
print(cerc.get_raza())
print(cerc.del_raza())
print(cerc.get_raza())"""