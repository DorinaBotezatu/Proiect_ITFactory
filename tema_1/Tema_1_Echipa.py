#1.Exercitiu
string = input('Introduceti un string: ')
primul_caracter = string[0]
ultimul_caracter = string[len(string)-1]
string_fara_2caractere = string[1:len(string)-1]
print(string_fara_2caractere)
capitalizat_string = string_fara_2caractere.replace(primul_caracter, primul_caracter.upper())
print(primul_caracter + capitalizat_string + ultimul_caracter )

#2.Exercitiu
user = input('Introdu numnele userului: ')
parola = input('Introdu parola: ')
parola_ascunsa = len(parola)*'*'
print(f'Parola pentru user {user} este {parola_ascunsa} si are {len(parola)} caractere')