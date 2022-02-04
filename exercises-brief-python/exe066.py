# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up.

total = 0
cont = 0

while True:
    cont += 1
    preco = float(input(f'Informe o preço do produto {cont}:'))
    total += preco
    if preco == 0:
        break

print(f"O valor total dos produtos é: R$ {total:2.f}")
### Pulei as partes de arredondamento por não manjar da unidade de medida pedida.
