"""
5.Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000

"""
""" def schimba_propr(self, catitate=0, pret=0, nume=""):
        if catitate:
            self.cantitate = catitate
        if pret:
            self.pret_buc = pret
        if nume:
            self.nume_produs = nume"""
from datetime import date
from prettytable import PrettyTable


class Factura:
    SERIA = "AA3"

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitatea):
        self.cantitate = cantitatea

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        today = date.today()
        x = PrettyTable()
        print(f"Factura seria {Factura.SERIA} numar {self.numar}\nData: {today}")
        x.field_names = ["Produs", "Cantitate", "Pret bucata", "Total"]
        x.add_row([self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc])
        print(x)


if __name__ == "__main__":
    factura1 = Factura(2023, "jeans", 10, 30)

    factura1.genereaza_factura()
    factura1.schimba_pretul(12)
    factura1.genereaza_factura()