class Robo():
    def __init__(self, bateria):
        self.__bateria = bateria
        self.__estado = 'Desligado'

    def liga_desliga(self):
        if self.__bateria == 0:
            print('Robo sem bateria.')
            self.__estado == 'Desligado'
        else:
            if self.__estado == 'Desligado':
                self.__estado = 'Ligado'
                print('Robô está ligado.')
            else:
                self.__estado = 'Desligado'
                print('Robô está desligado.')

    def movimento(self, lado):
        if self.__bateria == 0:
            print('Bateria zerada, carregue o robô')
        else:
            if self.__estado == 'Desligado':
                print('Robô desligado. Ligue-o para movimentá-lo')
            else:
                self.__lado = lado
                self.__bateria -= 10
                if self.__bateria == 0:
                    self.__estado == 'Desligado'


    def status(self):
        nivel_bat = f'Nível da bateria: {self.__bateria} '
        estado = f'Estado: {self.__estado}'
        print(nivel_bat)
        print(estado)

try:
    bateria = -1
    while bateria > 100 or bateria < 0:
        bateria = int(input('Digite a bateria do robô: '))
except ValueError:
    print('Opção Inválida. Digite um valor válido para bateria.')
else:
    r2d2 = Robo(bateria)
    while True:
        try:
            print('----------------------------- MENU -------------------------')
            print('1 - Ligar ou Desligar o robô')
            print('2 - Movimentar o robô')
            print('3 - Controle de Energia do robô')
            print('4 - Finalizar o programa')
            opcao = int(input('Digite o número respectivo ao programa que deseja: '))
        except ValueError:
            print('Opção de menu inválida.')
        else:
            if opcao == 1:
                r2d2.liga_desliga()
            elif opcao == 2:
                r2d2.movimento(input('Digite o lado para qual o robô irá andar: '))
            elif opcao == 3:
                r2d2.status()
            elif opcao == 4:
                break
            else:
                print('Digite um número entre 1 e 4')
print('Programa encerrado com sucesso.')






