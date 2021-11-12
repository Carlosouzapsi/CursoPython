mes = str(input('Informe o nome do mês: ')).strip().lower()

def define_mes(m):
    if m in 'janeiro' or m in 'março' or m in 'maio' or m in 'julho' or m in 'agosto' or m in 'outubro' or m in 'dezembro':
        print(f'O mês de {m} possui 31 dias')
    if m in 'abril' or m in 'junho' or m in 'setembro' or m in 'novembro':
        print(f'O mês de {m} possui 30 dias')
    if m in 'fevereiro':
        print(f'O mês de {m} possui 28 dias')

define_mes(mes)
