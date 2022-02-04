animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra', 'Cobra',
           'Coelho', 'Mosquito', 'Peixe', 'Macaco']

# 1
listaAnimais = [animal for animal in animais if animal[0] == 'C' and len(animal) <= 7]

print(listaAnimais)
