lista_animais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo'
    , 'Baleia', 'Gato', 'Urso', 'Abelha',
                 'Carneiro', 'Cabra', 'Coelho', 'Mosquito', 'Peixe',
                 'Peixe', 'Macaco', 'Aranha']

gen_animais = (animal for animal in lista_animais if (animal[0] == 'C'
                                                      or animal[0] == 'A') and len(animal) > 5)

### PRECISA ITERAR PARA CONSEGUIR IMPRIMIR DE FORMA CORRETA O GENERATOR:
### CASO NÃO SEJA ITERADO, SÓ MOSTRARÁ O ENDEREÇO DE MEMÓRIA.
for animal in gen_animais:
    print(animal, end=' ')
