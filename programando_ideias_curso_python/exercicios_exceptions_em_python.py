

opcoes_viagem = {1:'EUA', 2:'Franca', 3:'Japao', 4:'Brasil'}
flag = False
while flag != True:
        nome = str(input('Digite seu nome: '))
        if nome.isalpha():
            flag = True
        else:
            print('Erro!, O valor informado deve ser uma cadeia de caracteres. Tente novamente!')   
while True:
    try:
        idade = int(input('Digite sua idade:'))
    except ValueError:
        print('Erro!, o valor informada deve ser um número inteiro. Tente novamente!')
    else:
        break
while True:
    try:
        lugar = int(input('Diite o número para escolha do lugar: \n 1 - EUA \n 2 - Franca - \n 3 - Japao \n 4 - Brasil \n'))
    except IndexError:
        print('Erro!, O pais escolhido não existe no cadastro. Tente novamente!')
    except ValueError:
        print('Erro!, o valor informado precisa ser um número inteiro!')
    else:
        
        break
    finally:
        pais = opcoes_viagem[lugar]
        print(f'O pais escolhido foi: {pais}')
        print('Obrigado por se inscrever e uma boa viagem =)')
                        
                
    
    

    