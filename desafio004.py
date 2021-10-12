a = input('digite algo:')
### comando para verificar o tipo primitivo:
print('O tipo primitivo desse valor é ', type(a))
### comando para verificar se o que foi digitado é só 'espaços'
print('Só tem espaços? ', a.isspace())
#### comando para verificar se o que foi digitado é numérico:
print('É um número? ', a.isnumeric())
#### comando para verificiar se o que foi digitado é um caractere alfabético:
print('É alfabético ', a.isalpha())
#### comando para verificar se o que foi digitado é alfanumérico:
print('É alfanumérico?', a.isalpha())
#### comando para verificar se os caracteres são maiúsculos:
print('Está em maiúsculas? ', a.isupper())
#### comando para verificar se os caracteres são minúsculos:
print('Está em minúsculos? ', a.islower())
#### comando nem maiuscula nem minuscula == capitalizada:
print('Está capitalizada: ', a.istitle())