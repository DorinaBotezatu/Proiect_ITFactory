
#Exercitii obligatorii
#1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# O variabila este un loc de memorie in care sestocheaza o variabila

#2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:string,int, float, bool

var_string = "Astazi este o zi insorita"
var_int = 10
var_float = 25.6586
var_bool = True

#3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

type(var_string)
type(var_int)
type(var_float)
type(var_bool)

#4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia

var_float = round(var_float)
print(var_float)
type(var_float)

#5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
#Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'Primul string este: {var_string}')
print(f'Primul numar intreg: {var_int}')
print(f'Primul numar real: {"{:.2f}".format(var_float)}')
print(f'Prima valoare: {var_bool}')

#6. Citește de la tastatură:
#- numele;
#- prenumele.

nume = input('Introduceti numele: ')
prenume = input('Introduceti prenumele: ')
nr_caractere = len(nume) + len(prenume)
print(f'Numele complet are {nr_caractere} caractere')

#7. Citește de la tastatură:
#- lungimea;
#- lățimea.
#Afișează: 'Aria dreptunghiului este x'.

lungime = input('Introduceti lungimea dreptunghiului: ')
latime = input('Introduceti latimea dreptunghiului: ')
print(f'Aria dreptunghiului este:  {int(lungime) * int(latime)}')

#8;9.Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#Afișează de câte ori apare cuvântul 'the';
#Printează rezultatul.

stringul_1 = 'Coral is either the stupidest animal or the smartest rock'
stringul_1_cuvinte = stringul_1.split()
the_count = stringul_1_cuvinte.count('the')
print(the_count)

#10. Același string:
#Folosește un assert ca să verifici dacă acest string conține doar numere.

str_numere = stringul_1.isnumeric()
print(str_numere)


#Exerciții Opționale
#1. Exercițiu:
#citește de la tastatură un string de dimensiune impară;
#afișează caracterul din mijloc.


string_impar = input('introduceti un string impar: ')
string_impar_len = len(string_impar)
string_impar_mijloc = int(string_impar_len/2)
print(string_impar[string_impar_mijloc])

#2. Folosind o singură linie de cod :
#citește un string de la tastatură (ex: 'alabala portocala');
#salvează fiecare cuvânt într-o variabilă;
#printează ambele variabile pentru verificare.

a, b = input('Introduceti un string: ').split(); print(a); print(b)