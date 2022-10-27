# b. Dificultate: usor spre mediu

# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def suma(a, b):
    c = a + b
    print(f'Suma {a} plus {b} este egal cu {c}')
    return c


# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par_impar(number):
    if number % 2 == 0:
        return True
    else:
        return False


# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
def nume_nr_caractere(nume):
    nume = len(nume)
    print(f'Numele tau complet are {nume} caractere')
    return nume


# 4. Functie care returneaza aria dreptunghiului
def arie_dreptunghi(a, b):
    arie = a * b
    print(f'Aria dreptunghiului cu laturile de {a} si {b} este {arie}')
    return arie


# 5. Functie care returneaza aria cercului
def aria_cerc(raza):
    constanta_pi = 3.14
    aria_cerc = 3.14 * raza ** 2
    print(f'Aria cercului cu raza de {raza} este {aria_cerc}')
    return raza


# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def gaseste_caracter(caracter, string):
    if caracter in string:
        return True
    else:
        return False

    # 7. Functie fara return, primeste un string si printeaza pe ecran:
    # Nr de caractere lower case este x
    # Nr de caractere upper case exte y


def lower_upper_caractere(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if (i.isupper()):
            count_upper += 1
        if (i.islower()):
            count_lower += 1
    print(f' Nr de caractere upper case este {count_upper}')
    print(f' Nr de caractere lower case este {count_lower}')


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def nr_pozitive(lista_nr):
    lista_nr_pozitive = []
    for i in lista_nr:
        if i > 0:
            lista_nr_pozitive.append(i)
    return lista_nr_pozitive


# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def comparatie_nr(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    if x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    if x == y:
        print(f'Numerele sunt egale.')


# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def verifica_nr_in_set(nr, set_nr):
    for i in set_nr:
        if nr == i:
            print(f'Nu am adaugat numarul {nr} in set. Acesta exista deja')
            return False

    for i in set_nr:
        if nr != i:
            print(f'Am adaugat numarul {nr} nou in set')
            return True

if __name__ == "__main__":
    suma(24, 36)
    suma(22, 44)

    input_numar = int(input('Numarul ='))
    print(par_impar(input_numar))


    nume_nr_caractere('Dorina Botezatu')
    nume_nr_caractere('Alexandru Reulet')

    arie_dreptunghi(28, 96)
    arie_dreptunghi(23, 26)

    aria_cerc(10)
    aria_cerc(20)

    gaseste_caracter('s', 'ala bala ')
    gaseste_caracter('l', 'masina')

    lower_upper_caractere('Anastasia')
    lower_upper_caractere('Ana are MERE')

    nr_pozitive([200, -40, -55, 29, ])
    nr_pozitive([45, -50, 30, -55, -80])

    comparatie_nr(25, 70)
    comparatie_nr(25, 25)
    comparatie_nr(55, 2)

    verifica_nr_in_set(20, {50, 20, 60, 80})
    verifica_nr_in_set(55, {20, 50, 100, 80})
    verifica_nr_in_set(50, {50, 20, 100, 150})
