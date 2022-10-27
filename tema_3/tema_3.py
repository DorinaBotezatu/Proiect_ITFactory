# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# Afișeaz-o.
print(note_muzicale)
# Inversează ordinea folosind slicing și suprascrie această listă.
# Printează varianta actuală (inversată).
note_muzicale_inversta = note_muzicale[::-1]
print(note_muzicale_inversta)
# Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
note_muzicale_inversta.reverse()
print(note_muzicale_inversta)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# prima varianta de unire
lista1.extend(lista2)
# adoua varianta de unire
lista3 = lista1 + lista2
print(lista1)
print(lista3)
# 4.Sortează și afișează lista generată la exercițiul anterior.
lista3.sort()
print(lista3)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.

if lista3:
    print('lista nu este goala')
else:
    print('Lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista3.clear()
print(lista3)
# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if lista3:
    print('lista nu este goala')
else:
    print('Lista este goala')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
elevi = dict1.keys()
print(f'Elevii:  {elevi}')

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print(f'Ana a luat nota: {dict1["Ana"]}')
print(f'Gigel a luat nota: {dict1["Gigel"]}')
print(f'Dorel a luat nota: {dict1["Dorel"]}')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1['Dorel'] = 6
print(f'Dorel a luat nota: {dict1["Dorel"]}')

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# Exerciții Opționale
"""1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișază a intrat x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’"""

jucatori_de_fotball = ['Ion', 'Marin', 'Radu', 'Sergiu', 'Vanea']
jucatori_de_rezerva = ['Valeriu', 'Simion', 'Andrei']
schimbari_disponibile = 3
x = 1
while x <= 3:
    jucator_cautat = input('Ce jucator se schimba: ')
    jucator_de_schimb = input('Ce jucator din rezerva intra pe teren: ')
    if jucatori_de_fotball.count(jucator_cautat) > 0:
        jucatori_de_fotball.remove(jucator_cautat)
        jucatori_de_fotball.append(jucator_de_schimb)
        jucatori_de_rezerva.remove(jucator_de_schimb)
        jucatori_de_rezerva.append(jucator_cautat)
        print(f'A intrat jucatorul {jucator_de_schimb}, a iesit jucatorul {jucator_cautat}, mai ai {schimbari_disponibile - 1} schimbari')
        schimbari_disponibile -= 1
    else:
        print(
            f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_cautat} nu e în teren’\n Mai ai {schimbari_disponibile - 1} schimbari')
    x +=1


