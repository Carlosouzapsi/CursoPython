def desmembra_iteravel(iteravel): 
    conv_iteravel = iter(iteravel)
    while True:          
        try:
            print(next(conv_iteravel))
        except StopIteration:
            print('Chegamos ao ultimo elemento')
            break


lista = [1,2,3,4,5,6,7,8,9,10]
desmembra_iteravel(lista)

