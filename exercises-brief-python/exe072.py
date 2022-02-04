for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('Jogador diz Fizz e diz Buzz')
    if n % 3 == 0:
        print('Jogador diz Fizz')
    elif n % 5 == 0:
        print('Jogador diz Buzz')
