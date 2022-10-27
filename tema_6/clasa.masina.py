"""
6.Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile,
 altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare,
daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0

"""


class Masina:
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.marca = "BMW"
        self.viteza_actuala = 0
        self.culori_disponibile = {"alb", "verde", "negru", "rosu", "galben", "albastru"}
        self.inmatriculata = False
        self.culoare = "gri"

    def descriere(self):
        print(f'Marca: {self.marca}, model: {self.model}, viteza maxima: {self.viteza_maxima}, viteza actuala {self.viteza_actuala} culoare: {self.culoare},'
              f'inmatriculata : {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print("Eroare! Culoare indisponibila")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("viteza trebuie sa fie mai mare ca zero")
        if viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


masina = Masina("X5", 250)

masina.vopseste("alb")
masina.descriere()
masina.inmatriculare()
masina.accelereaza(120)

masina.descriere()