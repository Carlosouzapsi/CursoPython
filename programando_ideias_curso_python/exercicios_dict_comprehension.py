# resultado = {}
# for number in range(1, 100):
#     list = []
#     for divisor in range(1, 10):
#         if number % divisor == 0:
#             list.append(divisor)
#     resultado[number] = max(list)
# print(resultado)

resultado = {number: max([divisor for divisor in range(1, 10) if number % divisor == 0]) for number in range(1, 100)}
print(resultado)
