### EXERCICIO 01:
numero = int(input('Informe um número inteiro: '))


def soma_nums(n):
    divisor = 1
    soma = 0
    while True:  # loop que descobre a quantidade de algarismos
        if (numero // divisor) == 0:  # 25 // 1 = 25; 25 // 10 = 2; 25 // 100 = 0
            break
        else:
            soma += 1
            divisor *= 10
    somatorio_digitos = 0
    for valor in range(soma):
        somatorio_digitos += ((numero // (10 ** valor)) % 10)
    return somatorio_digitos


if numero > 0:
    print(soma_nums(numero))
else:
    print('Valor digitado é inválido!')
