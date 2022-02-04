login = False
print('Bem-vindo(a) ao cadastro do site!')
user = input('Crie seu nome de usuário: ')
senha = input('Crie sua senha: ')

print('\n_________LOGIN_____________')
if input('Usuário: ') == user and input('Senha: ') == senha:
    ### Usuário deve conseguir logar:
    login = True
# if login:
#     print(f'\nBem vindo(a) {user}')
# else:
#     print('Tente novamente!')

#### 2) Desenvolvendo o teste de login de outras formas:
# if not login:
#     print('\nTente novamente!')
# else:
#     print(f'\nBem vindo(a) {user}')

#### 3) Desenvolvendo o teste de login de outras formas:
if login is True:
    print(f'\nBem vindo(a)')
else:
    print(f'Tente novamente!')
