from classes import Escritor
from classes import Caneta
from classes import MaquinaEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(escritor)
print(caneta.marca)
maquina.escrever()