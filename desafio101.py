def voto(ano):
    #### UTILIZANDO ESCOPO DE IMPORTAÇÃO:
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade <= 60:
        return "Voto obrigatório"
    elif 16 >= idade < 18:
        return "Voto opcional"
    elif idade > 60:
        return "Voto opcional"

ano_nasc = int(input('Informe o ano de nascimento: '))
print(voto(ano_nasc))