from time import sleep

def contador(i, f, p):
    ### Passando o PASSO para número positivo:
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('Contagem de {} até {} de {} em {}'.format(i, f, p, p))
    if i < f:
        cont = i
        while cont <= f:
            print('{} '.format(cont), end='', flush=False)
            sleep(0.5)
            cont+=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print('{} '.format(cont), end='', flush=False)
            sleep(0.5)
            cont-=p
        print('FIM!')

### PROGRAMA PRINCIPAL
contador(1, 10, 2)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
