mensagem = input('Informe a mensagem que deseja criptografar: ').lower()
troca = int(input('Informe o valor de troca: '))

nova_mensagem = ""

for letra in mensagem:
    if letra >= "a" and letra <= "z":
        pos = ord(letra) - ord("a")
        pos = (pos + troca) % 26
        nova_letra = chr(pos + ord("a"))
        nova_mensagem += nova_letra
    else:
        nova_mensagem += nova_letra

print(f'MENSAGEM CRIPTOGRAFADA: {nova_mensagem}')
