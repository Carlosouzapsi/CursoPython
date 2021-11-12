cedula = int(input('Informe o valor da nota em U$: '))

george = 'George Washington'
jefferson = 'Thomas Jefferson'
lincoln = 'Abraham Lincoln'
hamilton = 'Alexander Hamilton'
jackson = 'Andrew Jackson'
grant = 'Ulysses S. Grant'
franklin = 'Benjamin Franklin'

def verifica_cedula(c):
    if cedula == 1:
        print(george)
    elif cedula == 2:
        print(jefferson)
    elif cedula == 5:
        print(lincoln)
    elif cedula == 10:
        print(hamilton)
    elif cedula == 20:
        print(jackson)
    elif cedula == 50:
        print(grant)
    elif cedula == 100:
        print(franklin)
    else:
        print('Essa nota não existe!')




verifica_cedula(cedula)


