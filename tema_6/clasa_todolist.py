"""
7. Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

"""


class TodoList:
    dict = {}

    def adauga_task(self, nume, descriere):
        self.dict.update({nume: descriere})

    def finalizeaza(self, nume):
        self.dict.pop(nume)

    def afiseaza(self):
        print(self.dict.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.dict:
            alegere = input(f"Doriti sa adaugati in dictionar {nume_task}? Yes or No ")
            if alegere == "Yes":
                detalii = input("Detalii task:")
                self.adauga_task(nume_task, detalii)
            if alegere == "No":
                print("La revedere!")
        else:
            print(self.dict.get(nume_task))


task = TodoList()
task.adauga_task("Cumparaturi", "Detalii cumparatuei: lapte")
task.adauga_task("Joc", "Te joci jocuri sociale")
task.afiseaza()
task.afiseaza_detalii_suplimentare("Gatit")
