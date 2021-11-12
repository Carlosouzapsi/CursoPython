idade = int(input())
anos = idade // 365
resto = idade - anos * 365
meses = (resto // 30)
resto2 = resto - meses * 30
dias = resto2
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')