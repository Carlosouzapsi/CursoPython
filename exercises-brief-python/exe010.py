import math
# Exercise 10: Arithmetic
# (Solved, 22 Lines)
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))

def out_put(num1, num2):
    soma = num1 + num2
    print(f'Soma dos números {num1} e {num2} é: {soma}')
    diferenca = num1 - num2
    print(f'Diferença dos números {num1} e {num2} é: {diferenca}')
    produto = num1 * num2
    print(f'Produto dos números {num1} e {num2} é: {produto}')
    divisao = num1 / num2
    print(f'O quociente da divisão entre os números {num1} e {num2} é: {divisao}')
    modulo = num1 % num2
    print(f'Resto da divisão dos números {num1} e {num2} é: {modulo}')
    log10 = math.log(num1, 10)
    print(f'O log de {num1} é: {log10}')
    pot = math.pow(num1, num2)
    print(f'A potência de base {num1} e expoente {num2} é igual à: {pot}')

out_put(n1, n2)









