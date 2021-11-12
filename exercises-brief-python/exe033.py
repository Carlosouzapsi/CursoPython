n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
menor = min(n1, n2, n3)
print(f'{menor} é o menor.')
maior = max(n1, n2, n3)
print(f'{maior} é o maior.')
meio = (n1 + n2 + n3) - maior - menor
print(f'{meio} é o numero do meio.')