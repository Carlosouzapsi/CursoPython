sequencia = list()
print(sequencia)
proximo_termo = 0
while True:
    num = str(input('Informe um número: '))
    if num != "":
        num = int(num)
        if not sequencia:
            sequencia.append(num)
        else:
            if num % 2 == 0:
                proximo_termo = num // 2
                sequencia.append(proximo_termo)
            else:
                proximo_termo = (sequencia[-1] * 3) + 1
                sequencia.append(proximo_termo)
    else:
        break
print(sequencia)
