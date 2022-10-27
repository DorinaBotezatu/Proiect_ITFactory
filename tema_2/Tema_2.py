# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.
# dupa if urmeaza o conditie care daca este adevarata va rula urmatorul pas, daca este fals va rula dupa else.

# 2. Verifică și afișează dacă x este număr natural sau nu.
numar = int(input('Introdu un numar x : '))
numar_y = int(input('Introdu un numar y: '))
numar_z = int(input('Introdu un numar z: '))
if numar >= 0:
    print(f'{numar} - este un numar natural!')
else:
    print(f'{numar} - nu este un numar natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if numar > 0:
    print(f'{numar} - este un numar pozitiv!')
elif numar < 0:
    print(f'{numar} - este un numar negativ!')
else:
    print(f'{numar} -este in numar neutru!')

# 4. Verifică și afișează dacă x este între -2 și 13.
if -2 <= numar <= 13:
    print(f'{numar} - este intre valorile -2 si 13')
else:
    print(f'{numar} -este mai mic de -2 sau mai mare de 13')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

if numar - numar_y < 5:
    print(f'Diferenta numerelor {numar} si {numar_y} este mai mica de 5')
else:
    print(f'Diferenta numerelor {numar} si {numar_y} este mai mare de 5')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

if not 5 <= numar <= 27:
    print(f'{numar} - nu se afla intre valorile 5 si 27')
else:
    print(f'{numar} - se afla intre valorile 5 si 27')

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.

if numar == numar_y:
    print(f'Numarul {numar} este egal cu numarul {numar_y}')
elif numar > numar_y:
    print(f'Numarul {numar} este mai mare decat {numar_y} ')
else:
    print(f'Numarul {numar_y} este mai mare decat {numar}')

# 8.X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

if numar == numar_y or numar_z == numar_y or numar == numar_z:
    print(f'Acesta este un triunghi isoscel cu laturile de: {numar}, {numar_z}, {numar_y} ')
elif numar == numar_y == numar_z:
    print(f'Acesta este un triunghi echilateral cu laturile de: {numar}, {numar_z}, {numar_y} ')
else:
    print(f'Acesta este un triunghi oarecare cu laturile de: {numar}, {numar_z}, {numar_y} ')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.

litera = input('Introduceti o litera: ')
if litera in ('a', 'e', 'i', 'o', 'u'):
    print(f'Litera -{litera}- este o vocala!')
else:
    print(f'Litera -{litera}- este o consoana!')

"""10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F"""

nota = float(input('Introduceti nota: '))
if nota >= 9:
    print('Nota ta este: A')
elif 8 <= nota < 9:
    print('Nota ta este: B')
elif 7 <= nota < 8:
    print('Nota ta este: C')
elif 6 <= nota < 7:
    print('Nota ta este: D')
elif 5 <= nota < 6:
    print('Nota ta este: E')
else:
    print('Nota ta este: F')

# Exerciții Opționale
# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

numar_x = int(input('introduceti un numar x: '))
numar_y = int(input('Introdu un numar y: '))
numar_z = int(input('Introdu un numar z: '))
if 1000 <= numar_x < 10000:
    print(f'Numarul {numar_x} are minim 4 cifre')
elif numar_x > 10000:
    print(f'Numarul {numar_x} are mai mult de  4 cifre')
else:
    print(f'Numarul {numar_x} are mai putin de  4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
if 10000 <= numar_x < 1000000:
    print(f'Numarul {numar_x} are exact 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
if numar_x % 2 == 0:
    print(f'Numarul {numar_x} este un numar par')
else:
    print(f'Numarul {numar_x} este un numar impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?

if numar_x > numar_y and numar_x > numar_z:
    print(f'Numarul {numar_x} este cela mai mare')
elif numar_y > numar_x and numar_y > numar_z:
    print(f'Numarul {numar_y} este cela mai mare')
else:
    print(f'Numarul {numar_z} este cela mai mare')

# 5.X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

unghi_1 = int(input('introduceti unghiul 1 al triunghiului: '))
unghi_2 = int(input('Introdu unghiul 2 al triunghiului: '))
unghi_3 = int(input('Introdu unghiul 3 al triunghiului: '))

if unghi_1 + unghi_2 + unghi_3 == 180:
    print('Triunghiul este valid: are 180 de grade')
else:
    print('Triunghiul este invalid')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citește de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'

ultimele_caractere = int(input('Introduceti o cifra: '))
string_1 = 'Coral is either the stupidest animal or the smartest rock'
fara_caractere = string_1[-ultimele_caractere:]
string_modificat = string_1.replace(fara_caractere, '')
print(string_modificat)

# 7. Același string. Declară un string nou care să fie format din primele 5
# caractere + ultimele 5.

string_nou = string_1[:6] + string_1[-5:]
print(string_nou)

#8. Același string.
#● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
#este o funcție care te ajuta sa faci asta)
#● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
#● output: 'Coral is either the stupidest animal or the smartest'

start_index = string_1.index('rock')
print(start_index)
string_2 = string_1[:start_index]
print(string_2)


#Exerciții Bonus
#Joc ghicit zarul

from random import randint
dice_roll = randint(0,6)

numar_utilizator = int(input('Ghiceste numarul zarului: '))

if dice_roll == numar_utilizator:
    print(f'Ai ghicit. Felicitări! Ai ales {numar_utilizator} si zarul a fost {dice_roll}.')
elif numar_utilizator > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_utilizator} dar a fost {dice_roll}.')
else:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_utilizator} dar a fost {dice_roll}.')


