mes = str(input('Informe o mês que você nasceu: ')).upper().strip()
dia = int(input('Informe o dia que você nasceu: '))

def verifica_signo(m, d):
    if m in 'JANEIRO':
        if d < 20:
            print('AQUARIO')
        else:
            print('CAPRICORNIO')
    if m in 'FEVEREIRO':
        if d < 19:
            print('AQUARIO')
        else:
            print('PEIXES')
    if m in 'MARÇO':
        if d < 21:
            print('PEIXES')
        else:
            print('ARIES')
    if m in 'ABRIL':
        if d < 20:
            print('ARIES')
        else:
            print('TOURO')
    else:
        print('caiu no else')





verifica_signo(mes, dia)