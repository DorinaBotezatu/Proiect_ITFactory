from calendar import monthrange
from datetime import datetime
from collections import Counter
from datetime import date
from dateutil import tz
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
def nr_zile_din_luna(luna):
    today = datetime.date.today()
    year = today.year
    return monthrange(year, luna)[1]


nr_zile_din_luna(3)
nr_zile_din_luna(10)


# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

def calculator(a, b):
    suma = a + b
    diferenta = a - b
    imultirea = a * b
    impartirea = a / b
    print(f'Suma dintre {a} si {b}, este {suma}')
    print(f'Diferenta dintre {a} - {b}, este {diferenta}')
    print(f'Imultirea intre {a} si {b}, este {imultirea}')
    print(f'Imbartirea {a} la {b}, este {impartirea}')
    return suma, diferenta, imultirea, impartirea


calculator(100, 10)
calculator(50, 25)


# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
def nr_de_cifre(lista_de_cifre):
    d = Counter(lista_de_cifre)
    return d


nr_de_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5])


# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele

def nr_maxim(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c


nr_maxim(20, 50, 25)
nr_maxim(40, 50, 80)


# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
def suma_numerelor(numar):
    suma = 0
    for i in range(0, numar + 1):
        suma += i
    return suma


suma_numerelor(3)
suma_numerelor(100)


# BONUS:

# 16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune

# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
def nr_comune(lista1, lista2):
    lista3 = []
    for i in lista1:
        for k in lista2:
            if i == k:
                lista3.append(i)
    return lista3


nr_comune([1, 2, 3, 5, 6, 9], [1, 2, 6, 5, 8, 10])


# 17. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida

def reducere_pret(pretul, reducerea):
    if float(reducerea) > 99:
        print(f'Reducerea de {reducerea} este invalida!')
    else:
        x = pretul - (pretul * reducerea / 100)
        print(f'Pretul vechi este de {pretul} lei, cu reducerea de {reducerea} %, pretul nou este de {x} lei')
    return x

reducere_pret(100,10)
reducere_pret(56,50)

# 18. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)
def data_ora_Romania():
    acum = datetime.now()
    d_o = acum.strftime("%d/%m/%Y %H:%M:%S")
    return d_o

data_ora_Romania()

def data_ora_China():

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Shanghai')
    utc = datetime.utcnow()
    # Tell the datetime object that it's in UTC time zone
    utc = utc.replace(tzinfo=from_zone)
    # Convert time zone
    local = utc.astimezone(to_zone)
    print(datetime.strftime(local, "%Y-%m-%d %H:%M:%S"))
    return local

data_ora_China()

# 19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
def zile_pana_la_Craciun():
    azi = date.today()
    anul_acesta = azi.year
    craciunul = date(anul_acesta, 12, 25)
    zile = (craciunul - azi).days
    print(str(zile) + " zile pana la Craciun!")
    return zile

zile_pana_la_Craciun()

def zile_pana_la_ziua_mea():
    azi = date.today()
    anul_viitor = date(2023, 0o6, 17)
    zile = (anul_viitor - azi).days
    print(str(zile) + " zile pana la ziua mea!")
    return zile

zile_pana_la_ziua_mea()