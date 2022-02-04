fatores = list()
dividendo = list()
#### LISTA IMPROVISADA DE VALORES PRIMOS:
primo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
cont = 0
while True:
    try:
        num = float(input('Informe um número inteiro: '))
    except ValueError:
        print('É necessário informar um número inteiro')
    else:
        if num < 2:
            print('Valor digitado inválido. O valor precisa ser maior que 2.')
        else:
            print('Fatorando o número:')
            while num != 1:
                if num in primo:
                    dividendo.append(num)
                    fatores.append(num)
                    print('Agora sim!')
                    num = 1
                else:
                    if (num % primo[cont] == 0):
                        dividendo.append(num)
                        fatores.append(primo[cont])
                        num = num / primo[cont]
            print(dividendo)
            print(fatores)
            break
