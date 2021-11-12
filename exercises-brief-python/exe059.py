import datetime
#### procurar modulo na internet!

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

data = datetime.date(ano, mes, dia)
print(data)
data_amanha = data + datetime.timedelta(days=1)
print(data_amanha)













