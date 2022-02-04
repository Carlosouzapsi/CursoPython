"""

- A palavra Raise significa levantar, em programação é utilizada para apresentar/levantar
erros no código que nós mesmos identificamos.
- A palavra raise é uma palavra reservada como outras do python
- Caso você usar o raise dentro de uma função, assim que o programa
reconhecer irá acusar o erro e sair da função.
Como declarar?
raise tipo_do_erro('Mensagem que você quer que apareça')

"""

# Cadastro em um site:
# Adaptar de maneira que login aceite apenas strings e senha só inteiros

def cadastrar(login, senha):
    if type(login) is not str: # is compara tipos primitivos, n valores.
       raise TypeError('Login deve ser string.')
    if type(senha) is not str:
        raise TypeError('Senha deve ser inteiro.')
    print(f'Login: {login} e Senha{senha}')
    
cadastrar(123, 123)
