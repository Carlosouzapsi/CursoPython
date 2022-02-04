string = str(input('Informe uma string: ')).strip().upper()
string = string.replace(" ", "").replace(".", "")
print(string)

eh_palindromo = True
cont = 0

while cont < len(string) / 2 and eh_palindromo:
    if string[cont] != string[len(string) - cont - 1]:
        eh_palindromo = False
    cont += 1
if eh_palindromo:
    print(f'é palíndromo.')
else:
    print(f'não é palíndromo.')
