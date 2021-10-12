num = 0
cont = 0
soma = 0
num = int(input('Digite um númer [999 para parar]: '))
while num != 999:
    soma+=num
    cont+=1
    ### trocando ordem de precedencia de comandos!!!
    num = int(input('Digite um númer [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {} .'.format(cont, soma))