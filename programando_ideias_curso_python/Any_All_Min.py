"""

Any, All, Max e Min

- Any Retorna True se QUALQUER elemento do iterável for True
#OBS: Neste caso, um iterável vazio retorna False.

### Exemplos de Any:
print(any([1,2,3,4,5,6,7,8,9,10])) #$## Existem pelo menos um elemento True
print(any([0, False, {}, [], ()])) ### Existem elementos False

### Iterando uma lista e usando o Any:

numeros = [1,2,3,4,5]
print(list(num % 5 == 0 for num in numeros)) ## Refaz a lista dizendo quais são False e quais são True
print(any(num % 5 == 0 for num in numeros))  ## Pega só elemento divisivel por 5 da lista e diz que ele é True


-- All: Retorna True se TODOS os elementos do iterável forem True
# OBS: Neste caso, um iterável vazio retorna True

### Exemplos de All: 
print(all([1,2,3,4,5,6,7,8,9,10])) ### Todos os iteráveis são retornados como true
print(all([0, False, {}, [], ()])) ### Todos os iteráveis são retornados como False
print(all([])) ### Retorna True por ser um iterável vazio
numeros = [2,4,6,8,10]
print(all(num % 2 == 0 for num in numeros))
 
- MAX Retorna o maior valor de um iterável ou dos elementos passados como argumentos

#### Exemplos de MAX
numeros = [13, 12, 343, 43, 11, 242, 15]
print(max(numeros))

cores = {'azul': 2, 'vermelho': 5, 'verde': 3}
print(max(cores.values())) ### RETORNA O MAIOR VALOR DA CHAVE
print(max(cores)) ### RETORNA A CHAVE COM O MAIOR VALOR

#### Exemplos de MIN
numeros = [13, 12, 343, 43, 11, 242, 15]
print(min(numeros))

cores = {'azul': 2, 'vermelho': 5, 'verde': 3}
print(min(cores.values())) ### RETORNA O MAIOR VALOR DA CHAVE
print(min(cores)) ### RETORNA A CHAVE COM O MAIOR VALOR

## Exemplo com Max e Min (retorno por ordem alfabética)
alunos = ['Pedro', 'Isadora', 'Lucas', 'Camila', 'Samuel']
print(max(alunos)) ### retorno por ordem alfabética
print(min(alunos)) ### retorno por ordem alfabética

"""
alunos = ['Pedro', 'Isadora', 'Lucas', 'Camila', 'Samuel']
## Usando Lambda para iterar o tamanho da cadeia de caracteres de cada aluno:
print(max(alunos, key=lambda aluno: len(aluno))) 
print(max(alunos, key=lambda aluno: len(aluno)))




 




















