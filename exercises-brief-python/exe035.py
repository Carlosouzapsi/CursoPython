num = int(input('Informe o primeiro número: '))

def par_ou_impar(n):
    if num % 2 == 0:
        print(f'O número {n} é par.')
    else:
        print(f'O número {n} é ímpar.')

par_ou_impar(num)