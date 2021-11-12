'''
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
'''
refeicao = float(input('Informe o valor da refeição: '))
def calcTotal(r):
    gorjeta = (r * 18) / 100
    imposto = (r * 10) / 100
    total = gorjeta + imposto + r
    print(f'Gorjeta: R$ {gorjeta:.2f}')
    print(f'Imposto: R$ {imposto:.2f}')
    print(f'Total:   R$ {total:.2f}')

calcTotal(refeicao)



