num_apro = int(input('Informe o número de aproximações que você deseja visualizar: '))
n1 = 0
n2 = 0
n3 = 0
soma_termos = 0
for a in range(1, num_apro):
    n1 += 2
    n2 += 2
    n3 += 2
    primeiro_termo = 3 + (4 / (n1 * n2 * n3))
    exp_general = 4 / (2 + n1) * (2 + n2) * (2 + n3)
    if a <= 1:
        pi = primeiro_termo
        print(pi)
    if a % 2 == 0:
        exp_general = - exp_general
        soma_termos -= exp_general
    else:
        exp_general = + exp_general
        soma_termos += exp_general

print(soma_termos)
