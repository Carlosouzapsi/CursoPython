'''
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2
'''
n = int(input('Informe um número: '))

def expressao(numero):
    soma = (numero * (numero + 1)) / 2
    return f'A soma dos números é: {soma:.2f}'


print(expressao(n))

