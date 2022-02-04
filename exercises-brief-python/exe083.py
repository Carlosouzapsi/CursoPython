import random

num = 0
maior_valor = random.randint(1, 100)
print(maior_valor)
update = 0
for n in range(2, 101):
    num = random.randint(1, 100)
    if num > maior_valor:
        update += 1
        maior_valor = num
        print(f'{maior_valor} ==> UPDATE!')
    print(num)

print(f'O maior valor encontrado foi: {maior_valor}')
print(f'O número de vezes que o maior valor foi atualizado é: {update}')
