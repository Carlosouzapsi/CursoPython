from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    resp = menu(['Listar Pessoas','Cadastrar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        ### OPÇÃO DE LISTAR O CONTEUDO DE UM ARQUIVO!
        lerArquivo(arq)
        # print('Opção 1')
    elif resp == 2:
        ### OPÇÃO DE CADASTRAR UMA PESSOA:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print('Opção 2')
    elif resp == 3:
        print('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')


