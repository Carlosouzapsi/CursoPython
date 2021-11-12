while True:
    try:
        som = int(input('Informe um valor em DCB: '))
    except ValueError:
        print('Erro, valor informado é inválido!')
        print('Informe um valor inteiro.')
    else:
        break
def verifica_som(s):
    if s > 106 and s < 130:
        print('O som possui frequencia entre JackHammer e Gas Lawnmower')
    if s == 130:
        print('O som possui somente frequencia JackHammer')
    if s == 106:
        print('O som possui somente frequencia Gas Lawnmower')
    if s > 40 and s < 70:
        print('O som possui frenquencia entre Alarm clock e Quiet Room')
    if s == 40:
        print('O som possui somente frequencia Alarm clock')
    if s == 70:
        print('O som possui somente frequencia Quiet Room')
    if s > 130:
        print('Faixa de som acima do especificado.')
    if s < 40:
        print('Faixa de som abaixo do especificado')

verifica_som(som)
