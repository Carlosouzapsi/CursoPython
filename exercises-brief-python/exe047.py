while True:
    try:
        mes = str(input('Informe o nome do mês: ')).upper().strip()
        dia = int(input('Informe o dia do mês: '))
    except ValueError:
        print('Erro, valor digitado inválido!')
        print('É necessário digitar uma string no nome do mês!')
        print('É necessário digitar um número inteiro no dia do mês!')
    else:
        break

def verifica_estacao(m, d):
    estacao = ' '
    if m in 'JANEIRO' or m in 'FEVEREIRO':
        estacao = 'VERÃO'
    elif m in 'MARÇO':
        if d < 20:
            estacao = 'VERÃO'
        else:
            estacao = 'OUTONO'
    elif m in 'ABRIL' or m in 'MAIO':
        estacao = 'OUTONO'
    elif m in 'JUNHO':
        estacao = 'OUTONO'
        if d < 21:
            estacao = 'OUTONO'
        else:
            estacao =  'INVERNO'
    elif m in 'JULHO' or m in 'AGOSTO':
            estacao = 'INVERNO'
    elif m in 'SETEMBRO':
        if d < 23:
            estacao = 'INVERNO'
        else:
            estacao = 'PRIMAVERA'
    elif m in 'OUTUBRO' or m in 'NOVEMBRO':
            estacao = 'PRIMAVERA'
    elif m in 'DEZEMBRO':
        if d < 23:
            estacao = 'PRIMAVERA'
        else:
            estacao = 'VERAO'
    return estacao

print(verifica_estacao(mes, dia))











