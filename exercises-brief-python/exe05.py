'''
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
'''
container = int(input('Informe o tamanho do container em Litros: '))

def calcRefund(c):
    if c <= 1:
        refund = c * 0.10
    else:
        refund = c * 0.25
    return refund


print(f'O valor recebido foi de: U$ {calcRefund(container):.2f}')










