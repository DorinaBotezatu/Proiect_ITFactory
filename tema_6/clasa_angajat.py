"""
3.Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)

"""


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return f'Nume: {self.nume}, Prenume: {self.prenume}, Salariu: {self.salariu}'

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return f"salariul lunar {self.salariu}"

    def salariul_anual(self):
        return f"Salariul anual este {12*self.salariu}"

    def marire_salariu(self, procent):
        self.salariu =self.salariu + self.salariu*procent/100
        return self.salariu



angajat = Angajat("Vasilescu", "Ion", 1000)
print(angajat.descriere())
print(angajat.nume_complet())
print(angajat.salariu_lunar())
print(angajat.salariul_anual())
angajat.marire_salariu(10)
print(angajat.salariu)