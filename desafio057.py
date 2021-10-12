#
# sexoFlag = False
# while sexoFlag != True:
#     sexo = str(input('Informe o sexo da pessoa [M/F]')).upper().strip()[0]
#     if sexo == 'M':
#         sexoFlag = True
#     else:
#         print('Sexo inválido, tente novamente!')
# print('Sexo validado com sucesso!!!!')

#### Outra resolução
# sexo = str(input('Informe se sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso'.format(sexo))