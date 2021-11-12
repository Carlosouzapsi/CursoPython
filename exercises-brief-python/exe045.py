while True:
    try:
        mes = str(input('Mês: ')).strip().upper()
        dia = int(input('Dia: '))
    except ValueError:
        print('Erro, valor digitado inválido.')
        print('É necessário informar o nome do mês e o valor númerico do dia.')
    else:
        break

def verifica_feriado(m, d):
    if m == 'JANEIRO' and d == 1:
        print('Feriado de ano novo.')
    elif m == 'JULHO' and d == 1:
        print('Aniversário do Canadá.')
    elif m == 'DEZEMBRO' and d == 25:
        print('Natal.')
    else:
        print('Feriado informado não foi encontrado!')

### PROGRAMA PRINCIPAL:
verifica_feriado(mes, dia)