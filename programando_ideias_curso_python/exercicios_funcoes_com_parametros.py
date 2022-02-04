### exer 01:

# listaSF = list()
# stop = 0
#
# def fibonacci(stop, a, b, aux):
#     global listaSF
#     listaSF.append(a)
#     a, b = b, a + b
#     aux += 1
#     if stop == aux:
#         print(listaSF)
#         return 0
#     else:
#         return fibonacci(stop, a, b, aux)
#
# while stop < 1:
#
#     stop = int(input('Digite a quantidade de termos: '))
#
# ### PRIMEIRA CHAMADA DA FUNÇÃO
# fibonacci(stop, a=1, b=1, aux=0)

### exer 02:

def menu_opt_sistema():
    print('=' * 30)
    print('    BEM VINDO AO SISTEMA     ')
    print('=' * 30)
    print('ESCOLHA UMA DAS OPÇÕES ABAIXO')
    print('1 - REALIZAR CADASTRO')
    print('2 - REALIZAR LOGIN')
    print('3 - REALIZAR LOGOUT')
    print('4 - ALTERAR SENHA')
    print('5 - SAIR DO SISTEMA')


def opcao_escolhida(opt):
    while True:
        if opt == 1:
            cadastrar_usuario()
        elif opt == 2:
            realizar_login()
        elif opt == 3:
            logout = str(input('Deseja deslogar do sistema? [S/N]: ')).upper().strip()
            deslogar(logout)
        elif opt == 4:
            nova_senha = str(input('Informe sua nova senha: '))
            alterar_senha(nova_senha)
        elif opt == 5:
            print('PROGRAMA ENCERRADO PELO USUÁRIO!')
            break
        menu_opt_sistema()
        opcao = int(input('OPÇÃO ESCOLHIDA: '))
        return opcao_escolhida(opcao)


lista_usuario = list()
i = 0
logado = False


def alterar_senha(senha):
    global logado
    while True:
        if logado:
            lista_usuario[i]['senha'] = senha
            print('SENHA ALTERADA COM SUCESSO!')
            break
        else:
            print('USUÁRIO PRECISA ESTAR LOGADO PARA TROCAR A SENHA!')
            break


def cadastrar_usuario():
    global lista_usuario
    if lista_usuario:
        print('NÃO É POSSÍVEL CADASTRAR OUTRO USUÁRIO')
    else:
        print('CADASTRAR USUÁRIO: ')
        dict_usuario = dict()
        dict_usuario['username'] = str(input('Informe o nome de usuário: '))
        dict_usuario['senha'] = str(input('Informe a senha: '))
        lista_usuario.append(dict_usuario)
        print('USUÁRIO CADASTRADO COM SUCESSO!')


def realizar_login():
    global logado
    while True:
        login_username = str(input('Informe o seu usuário: '))
        login_senha = str(input('Informe a sua senha: '))
        if login_username in lista_usuario[i]['username'] \
                and login_senha in lista_usuario[i]['senha']:
            logado = True
            print('USUÁRIO LOGADO COM SUCESSO')
            break
        else:
            print('Erro, credenciais inválidas!')


def deslogar(opt):
    global logado
    if logado:
        while True:
            if 'S' in opt:
                print('USUÁRIO DESLOGOU DO SISTEMA')
                break
            if 'N' in opt:
                print('USUÁRIO CONTINUA LOGADO NO SISTEMA')
    else:
        print('USUÁRIO PRECISA ESTAR LOGADO PARA DESLOGAR!')


### FUNÇÃO DE CABECALHO
menu_opt_sistema()
opcao = int(input('OPÇÃO ESCOLHIDA: '))
opcao_escolhida(opcao)
