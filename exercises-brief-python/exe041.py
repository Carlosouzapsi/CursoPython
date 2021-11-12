lado1 = int(input('Informe o primeiro lado do triângulo: '))
lado2 = int(input('Informe o segundo lado do triângulo: '))
lado3 = int(input('Informe o segundo lado do triângulo: '))

maior = 0
somaMenor = 0
if lado1 > lado2 and lado1 > lado3:
    maior = lado1
    somaMenor = lado2 + lado3
elif lado2 > lado1 and lado2 > lado3:
    maior = lado2
    somaMenor = lado1 + lado3
else:
    maior = lado3
    somaMenor = lado2 + lado1

if somaMenor > maior:
    print('É possível formar um triângulo!')
    def define_tri(l1, l2, l3):
        if l1 == l2 and l3 == l1:
            print('EQUILÁTERO')
        elif l1 != l2 and l3 != l2:
            print('ESCALENO')
        else:
            print('ISÓSCELES')
    define_tri(lado1, lado2, lado3)
else:
    print('Não é possível formar um triângulo!')





