'''
### MÉTODOS DE CLASSE:

- NECESSÁRIO USAR O DECORADOR : @classmethod
- NÃO HÁ O 'SELF', mas sim o 'cls', que se refere a própria classe onde está o método.

### CLS É TAMBÉM CONVENCIONAL!

Sintaxe:
    @classmethod
    def nome_metodo(cls):

#MÉTODO DE CLASSE NÃO FAZ ACESSO A ATRIBUTOS DE OBJETO/INSTANCIA!

# SUBTIPOS
- CONSTRUTOR
- PUBLICOS
- PRIVADOS
- MÉTODOS ESTÁTICOS

# MÉTODOS ESTÁTICOS:
- NECESSÁRIO UTILIZAR O DECORADOR: @staticmethod
- SEM PARÂMETROS



'''

## EXEMPLO:

class Computador:

    peixes = 98

    @classmethod
    def conta_peixes(cls):
        print(f'Nome da classe: {cls}')
        print(f'Existem {cls.peixes} peixes na classe {cls}')

    @staticmethod
    def modelo():
        return 'HJKSDSDSKFJFJFJ'

    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas

    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram

    ## METODO PRIVADO
    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'


###
pcVovo = Computador('Dourado', 0.1, 52)
pcVovo.cor
pcVovo.memoria(256, 2)
# print(pcVovo__caracteristicas) ## Atribute error! Tentou acessar um método privado
## forma correta de usar o método privado:
# print(pcVovo._Computador__caracteristicas()) ## Name mangling usar a classe com _ pra acessar atributos e métodos privados

## Acesso ao método estático pela classe direto ou pelo objeto!
print(Computador.modelo())
print(pcVovo.modelo())






