conjunto = set({})
for numero in range(1, 10):
    if numero % 2 == 0:
        conjunto.add(numero ** 2)
    else:
        conjunto.add('Sou')
        conjunto.add('Impar')
print(conjunto)

conjunto = {numero == 2 if numero % 2 == 0 else 'Sou' if num == 0 else 'Impar' for num in range(0, 2) for numero in
            range(1, 10)}
print(conjunto)
