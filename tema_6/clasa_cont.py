"""
4.Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)

"""

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont}, are in contul {self.iban}, suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold = self.sold - suma


    def creditare_cont(self, suma):
        self.sold = self.sold + suma


titular1 = Cont(2659763158, "Oleg vasilievici", 265.36)
titular1.afisare_sold()
titular1.debitare_cont(263)
titular1.afisare_sold()
titular1.creditare_cont(520)
titular1.afisare_sold()