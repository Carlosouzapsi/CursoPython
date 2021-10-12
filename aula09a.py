frase = 'Curso em Vídeo Python'
### pegando o terceiro indice:
print(frase[3])

### fatiando do indice 3 até o indice 13:
print(frase[3:13])

### do Inicio até o 13:
print(frase[:13])

### contando os caracteres:
print(frase.count('o'))

### verificando tamanhos:
print(len(frase))

### removendo espaços indesejados:
print(len(frase.strip()))

### trocando com replace:
print(frase.replace('Python', 'Android')) ### Muda somente nessa execução
print(frase)
### mudando uma string pra sempre:
# frase = frase.replace('Python', 'Android')
# print(frase)

### encontrando na frase:
print(frase.find('Vídeo'))

### Criando uma lista a partir da frase:
print(frase.split())