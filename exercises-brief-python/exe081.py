### https://www.w3resource.com/python-exercises/math/python-math-exercise-31.php

binario = list(input("Input a binary number: "))
### Inicializando a variável:
valor_convertido = 0

for i in range(len(binario)):
    digit = binario.pop()
    print(digit)
    if digit == '1':
        valor_convertido = valor_convertido + pow(2, i)

print("O valor binário convertido para decimal é: ", valor_convertido)
