'''
definição:

a) Atributo: Caracterísitcas do Objeto que a Classe irá controlar.
Ex: Uma classe Carro pode ter como atributo, a potência, numero de bancos, velocidade máxima,
dentre outros.

b)Objeto: É justamente o objeto da vida real que será controlado no programa.

Ex: Na classe Carro podemos receber com objeto: Corolla, Civic, Porsche, dentre outros.
'''

# class Carro:
#     def __init__(self): #Lembrando que o init é o método construtor.
#         print(self) ### Self objeto em si criado
#
# Jaguar = Carro() ### Criado o objeto jaguar controlado pela classe carro.
# print(Jaguar) ### Ao imprimir aparece endereço de memoria dele, que é o mesmo de self
# ### Por baixo dos planos o que ocorre?
'''
Assim que passo Carro(), como se a palavra init fosse substituido por Carro e Jaguar
passasse como primeiro atributo ficando assim: Jaguar = Carro(Jaguar), todo método
deve receber a palavra self.
'''
'''
Agora vamos aos atributos:
a)Atributos de instâncias: São os atributos declarados dentro do método construtor

Exemplo:

class Carro:
    def __init__(self, vel_maxima, potencia, num_bancos):
        self.vel_maxima = vel_maxima
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

# Jaguar = Carro() # Dá erro porque pede 3 argumentos! Pq o construtor pede os atributos para poder instanciar!
Jaguar = Carro(250, 350, 5)
print(Jaguar.potencia) # Maneira de acessar atributos de objeto!

b)Atributos de Classe: São os atributos que são declarados diretamente na classe,
fora de qualquer método!
- A principal caracteristicas, é que justamente esses atributos servem
  para todos os objetos declarados
- OBS: Vantagem de ocupar menos espaço de memória! Pois requer apenas 1 espaço para
  todos os objetos
- Exemplo: 

  class Carro:

    ##Atributo de classe:
    nitro = 1.1 ## Aumentar a velocidade máxima de cada objeto em 10%

    def __init__(self, vel_maxima, potencia, num_bancos):
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa var usa classe.nomeatributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

Jaguar = Carro(250, 350, 5)
print(Jaguar.vel_maxima)
print(Jaguar.nitro) ## é possivel acessar, o atributo é criado pra todos os objetos
print(Carro.nitro)
print(Carro.potencia) ## atribute error, porque potencia é atributo de instancia!
  

c)Atributos dinâmico: São criados ao longo da execução do programa, sendo que ele estará
  vinculado apenas ao objeto que o criou.

class Carro:

    ##Atributo de classe:
    nitro = 1.1 ## Aumentar a velocidade máxima de cada objeto em 10%

    def __init__(self, vel_maxima, potencia, num_bancos):
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa var usa classe.nomeatributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

    def cria_atributo(self):
        self.preco = 300000

Jaguar = Carro(250, 350, 5)
Porsche = Carro(260, 310, 5)
# Jaguar.preco = 300000
# print(Jaguar.preco)
Jaguar.cria_atributo()
print(Jaguar.preco)

print(Porsche.preco) # Attribute error pois o atributo pertence apenas ao objeto que o criou

### COMPLEMENTO DA AULA:

- Como deletar atributos? Comando del

class Carro:

    ##Atributo de classe:
    nitro = 1.1 ## Aumentar a velocidade máxima de cada objeto em 10%

    def __init__(self, vel_maxima, potencia, num_bancos):
        self.vel_maxima = vel_maxima * Carro.nitro # Para acessar essa var usa classe.nomeatributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

    def cria_atributo(self):
        self.preco = 300000

Jaguar = Carro(250, 350, 5)
Porsche = Carro(260, 310, 5)
del Jaguar.estado ## Deleta o atributo estado do objeto jaguar
print(Jaguar.__dict__) ## retorna um dict em que achave é atributo e o elemento é o valor do mesmo
print(Porsche.__dict__) ### Os atributos de jaguar não são deletados!

- Subdivisão: Atributos Publicos x Privados
- Na teoria, atributos publicos podem ser acessados por todos, enquanto privados não.

Como declarada cada um?

Ex:
self.potencia = potencia # Declarei um atributo publico
self.__potencia = potencia # Declarei um atributo privado

class Carro:

    ##Atributo de classe:
    nitro = 1.1 ## Aumentar a velocidade máxima de cada objeto em 10%

    def __init__(self, vel_maxima, potencia, num_bancos):
        self.__vel_maxima = vel_maxima * Carro.nitro # Para acessar essa var usa classe.nomeatributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

    def cria_atributo(self):
        self.preco = 300000

Jaguar = Carro(250, 350, 5)
Porsche = Carro(260, 310, 5)
# print(Porsche.vel_maxima) ## não consigo acessar o atributo
# print(Porsche.__vel_maxima) ## não consigo acessar o atributo
print(Porsche.potencia) ## consigo acessar o atributo
print(Porsche._Carro__vel_maxima) ### é possível acessar, mesmo o python dando erro Name mangling: objeto_classe__atributo
print(Jaguar._Carro__vel_maxima)

INCREMENTANDO A CLASSE CARRO: Adicionado método liga desliga

class Carro:

    ##Atributo de classe:
    nitro = 1.1 ## Aumentar a velocidade máxima de cada objeto em 10%

    def __init__(self, vel_maxima, potencia, num_bancos):
        self.__vel_maxima = vel_maxima * Carro.nitro # Para acessar essa var usa classe.nomeatributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False # Carro ligado ou desligado

    def liga_desliga(self):
        if self.estado == False:
            self.estado = True
        else:
            self.estado = False

Jaguar = Carro(250, 350, 5)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)


'''








