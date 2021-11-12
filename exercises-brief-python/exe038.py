while True:
    try:
        lados = 0
        while lados < 3 or lados > 10:
            lados = int(input('Informe um entre 10 e 3: '))
    except ValueError:
        print('Erro, valor digitado inválido!')
        print('É necessário informar um número inteiro entre 3 e 10')
    else:
        break

def define_forma(l):
    if l == 3:
        print('A figura formada é um triângulo!')
    if l == 4:
        print('A figura formada é um quadrilátero!')
    if l == 5:
        print('A figura formada é um pentágono!')
    if l == 6:
        print('A figura formada é um Hexágono!')
    if l == 7:
        print('A figura formada é um Heptágono!')
    if l == 8:
        print('A figura formada é um Octógno!')
    if l == 9:
        print('A figura formada é um Eneágono!')
    if l == 10:
        print('A figura formada é um Decágono!')

define_forma(lados)


