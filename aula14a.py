c = 1
# while c < 10:
#     print(c)
#     c+=1
# print('Fim')
### while é importante para flags e validações!!!
# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('Fim!')
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N]')).upper()
# print('Fim!')
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par+= 1
    else:
        impar+= 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))