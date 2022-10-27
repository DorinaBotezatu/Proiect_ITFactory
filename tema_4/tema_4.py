# 1.Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in masini:
    print(f'Masina mea preferata este {i}')

for each in masini:
    print(f'Masina mea preferata este {each}')

x = 0
while x <= len(masini) - 1:
    print(f'Masina mea preferata este {masini[x]}')
    x += 1

# 2.Aceeasi lista
# Folositi un for in for
# Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

lista_2 = []
lista_2.append(masini[0])
lista_2.append(masini[len(masini) - 1])
lista3 = []
for masina in lista_2:
    cuvant = ''
    for litera in masina:
        cuvant += litera.lower()
    lista3.append(cuvant)
    print(cuvant)

masini[0] = lista3[0]
masini[len(masini) - 1] = lista3[1]

print(masini)

# 3. Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
# Printam ‘am gasit masina dorita de dvs’
# Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
# Printam Am gasit masina X. Mai cautam

for elem in masini:
    if elem is 'Mercedes':
        print('Am gasit masina dorita de dvs')
        break
    else:
        print(f'Am gasit masina {elem}. Mai cautam')

# 4.Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
# Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

for car in masini:
    if car == 'Trabant' or car == 'Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {car}')

# 5. Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

masini_vechi = []
for j in range(len(masini) - 1):
    if masini[j] == 'Trabant':
        masini_vechi.append(masini[j])
        masini[j] = 'Tesla'
    elif masini[j] == 'Lastun':
        masini_vechi.append(masini[j])
        masini[j] = 'Tesla'

print(f'Modele vechi: {masini_vechi}\nModele noi: {masini}')

# 6. Avand dict
# pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
masini_sub_15000 = []
for pret in pret_masini.items():
    masini_sub_15000.append(pret)
for t in range(len(masini_sub_15000) - 1):
    if masini_sub_15000[t][1] <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {masini_sub_15000[t]}')

# 7.Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
var = 1
for number in range(len(numere) - 1):
    if numere[number] == 3:
        var += 1
print(f'Lista are numarul 3 de {var} ori')

# 8. Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

suma = 0
for k in range(len(numere)):
    suma += numere[k]
print(f'Suma numerelor este {suma}')

# 9. Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

maxi = numere[0]
for x in numere:
    if x > maxi:
        maxi = x
print(f'Cel mai mare numar este {maxi}')

# 10.Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
lista_nr_negative = []
for n in numere:
    if n > 0:
        x = 0 - n
        lista_nr_negative.append(x)
    else:
        lista_nr_negative.append(n)
print(lista_nr_negative)

# c. Optionale
# 11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for l in alte_numere:
    if l % 2 == 0:
        numere_pare.append(l)
    else:
        numere_impare.append(l)
    if l > 0:
        numere_pozitive.append(l)
    else:
        numere_negative.append(l)
print(f'numere pare: {numere_pare}')
print(f'numere impare: {numere_impare}')
print(f'numere pozitive: {numere_pozitive}')
print(f'numere negative: {numere_negative}')

# 12.Aceeasi lista
# Ordonati crescator lista fara sa folositi sort

lista_crescatoare = []

while alte_numere:
    minim = alte_numere[0]
    for mi in alte_numere:
        if mi < minim:
            minim = mi
    lista_crescatoare.append(minim)
    alte_numere.remove(minim)
print(lista_crescatoare)

# 13.Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#   User alege un numar
#   Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

from random import randint

nr = 1
while nr <= 10:
    nr_utilizator = int(input('Introduceti un numar de la 1 la 30: '))
    nr_random = randint(1, 30)
    if nr_utilizator < nr_random:
        print(f'Numar secret {nr_random} este mai mare decat {nr_utilizator} nr ales')
    elif nr_utilizator > nr_random:
        print(f'Numar secret {nr_random} este mai mic decat {nr_utilizator} nr ales')
    else:
        print(f'Felicitari! Ai reusit! Nr ales {nr_utilizator} este nr secret {nr_random}')
        break
    nr += 1

"""14. Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777"""

alege_nr = int(input('Alegetio un numar: '))
for element in range(1, alege_nr + 1):
    for d in range(1, element + 1):
        print(element, end=' ')
    print()


"""15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
"""

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for c in tastatura_telefon:
    for k in c:
        print(f'Cifra curenta este {c}')
    print('')

