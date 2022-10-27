"""2.
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return  f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime}, culoarea {self.culoare}"

    def aria(self):
       return f"Aria dreptunghiuliu este {self.lungime * self.latime}"

    def perimetrul(self):
        return f"Perimetrul dreptunghiului {2 * (self.latime + self.lungime)}"

    def schimba_culoare(self, culoare_noua):
        self.culoare = culoare_noua


if __name__ == "__main__":
    dreptunghi1 = Dreptunghi(20, 10, "alba")
    dreptunghi2 = Dreptunghi(30, 10, "rosie")

    print(dreptunghi1.descriere())
    print(dreptunghi1.aria())
    print(dreptunghi1.perimetrul())
    dreptunghi1.schimba_culoare("neagra")
    print(dreptunghi1.descriere())
    print("=========================")
    print(dreptunghi2.descriere())
    print(dreptunghi2.aria())
    print(dreptunghi2.perimetrul())
    dreptunghi2.schimba_culoare("albastra")
    print(dreptunghi2.descriere())
    print("=========================")
