valores = []
for v in range(0, 5):
    n = int(input('Digite um número: '))
    if v == 0:
        valores.append(n)
    elif n > valores[-1]: ### Ultimo elemento!!! Condição que adiciona ao final da lista.
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos+= 1
print('=' * 30)
print('Os valores digitados em ordem foram {}'.format(valores))



