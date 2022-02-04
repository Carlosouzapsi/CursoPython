n1 = 999  # Inicializa o primeiro númro
res = 0  # Armazena o número do palíndromo

while n1 != 0:
    n2 = n1
    # Esse loop realiza 999 * n2, 998 * n2, ...
    while n2 != 0:
        # Esse loop realiza n1 * 999, n1 * 998, n1 * 997, ...
        numero = str(n1 * n2)
        inverte_numero = numero[::-1]
        if inverte_numero == numero:
            num = int(numero)
            if res < num:
                res = num
                n2 -= 1
            else:
                n2 -= 1
        else:
            n2 -= 1
    n1 -= 1
print(res)
