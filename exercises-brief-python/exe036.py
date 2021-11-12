while True:
    try:
        humano = int(input('Informe a idade da pessoa: '))
    except ValueError:
        print(f'O valor informado é incorreto.')
        print(f'Informe um número inteiro.')
    else:
        break
def idade_dog(h):
    idade_dog = 0
    if h >= 2:
        idade_dog = (4 * (h - 2)) + (2 * 10.5)
    elif  h > 0 and h < 2:
        idade_dog = 10.5
    return idade_dog

print(f'Idade da pessoa é {humano} anos')
print(f'Idade do cachorro é {idade_dog(humano)} é anos')
