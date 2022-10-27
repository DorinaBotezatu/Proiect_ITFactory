# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
# 1. Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# ria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        return f'Raza cercului este {self.raza},culoarea {self.culoare} '

    def aria(self):
        pi = 3.14
        return f"Aria cercului {self.raza ** 2 * pi}"

    def diametrul(self):
        return f"Diametrul cercului {2 * self.raza}"

    def circumferinta(self):
        pi = 3.14
        return f"Circumferinta cercului {2 * pi * self.raza}"


if __name__ == "__main__":
    cercul_1 = Cerc(20, 'rosu')
    cercul_2 = Cerc(15, "galben")

    print(cercul_1.descriere_cerc())
    print(cercul_1.aria())
    print(cercul_1.diametrul())
    print(cercul_1.circumferinta())

    print('=======================')
    print(cercul_2.descriere_cerc())
    print(cercul_2.aria())
    print(cercul_2.diametrul())
    print(cercul_2.circumferinta())
    print('=======================')

