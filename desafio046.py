from time import sleep
n = int(input('Digite o número que você deseja começar a contagem: '))
for c in range(0, n + 1):
    sleep(1)
    print(c)
print('BUM! BUM! POOOW!')