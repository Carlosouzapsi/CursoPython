n = 0
s = 0
q = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s+=n
    q+=1
print('A soma dos números digitados é: {} '.format(s))
print('A quantidade de números digitados foi: {} '.format(q))
