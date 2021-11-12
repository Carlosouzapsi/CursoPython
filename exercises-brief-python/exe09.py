'''
Exercise 9: Compound Interest
(19 Lines)
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
'''
deposito = float(input('Informe o valor a ser depositado'))

def calcValorFinal(c=0):
    j = (c * 4) / 100
    for a in range(1, 4):
        c+=j
        print(f'Valor Economizado em {a} anos: {c:.2f}')

calcValorFinal(deposito)






