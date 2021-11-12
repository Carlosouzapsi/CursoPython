'''
Exercise 14: Height Units
(Solved, 16 Lines)
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
'''

feet = int(input('Enter your height on feet: '))

def calc_altura(f):
    conversor = f * 2.54
    return conversor

print(f'O valor convertido para centímetros é: {calc_altura(feet)}')



