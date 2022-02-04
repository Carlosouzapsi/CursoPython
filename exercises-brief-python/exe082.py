binario = int(input('Informe o número binário que você deseja converter: '))


def binario_decimal(b):
    result = ""
    nova_base = 2
    q = b
    ### REPRODUZINDO 1X ANTES DO LOOP:
    r = q % nova_base
    result = str(r) + result
    q = q // nova_base
    while q > 0:
        r = q % nova_base
        result = str(r) + result
        q = q // nova_base
    print(f'{b} em decimal é {result} em binário')


binario_decimal(binario)
