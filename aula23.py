#### TRATAMENTO DE EXCEÇÕES EM PYTHON:
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro: ### recebe o tipo de erro
#     print(f'Problema encontrado foi: {erro.__class__}')
# else:
#     print('O resultado é: {}'.format(r))
# #### finally e else são opcionais e finally acontece sempre!
# finally:
#     print('Volte sempre muito obrigado!')

#### PERSONALIZANDO MAIS AS EXCEPTIONS EM PYTHON:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos problema com o tipo de dado que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print('O resultado é: {}'.format(r))
#### finally e else são opcionais e finally acontece sempre!
finally:
    print('Volte sempre muito obrigado!')