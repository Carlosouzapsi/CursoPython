lista = list()

while True:    
    try: 
        numero = int(input('Informe um número inteiro: '))  
    except ValueError:       
        print('Valor digitado deve ser um número inteiro ')
    else:
        if numero == 0:
            break
        else:
            lista.append(numero)
           
def imprime_maior(l):
    ordenada = sorted(l)
    tamanho = len(l)
    ### Lista sempre começa em zero:
    print(f'Maior valor: {ordenada[tamanho - 1]}')

imprime_maior(lista) 

if len(lista) % 2 == 0:
    def imprime_media(l):
        invertida = reversed(l)
        tamanho = len(l)
        inter_1 = len(l) / 2
        inter_2 = (len(l) / 2) + 1
        media = (inter_1 + inter_2) / 2
        invertida_lista = list(invertida)
        print(invertida_lista)
        print(f'Média dos termos intermediários da lista: {media}')
    imprime_media(lista)     
else:
    def imprime_valor_intermediario(l):
        invertida = reversed(l)
        tamanho = len(l)
        intermediario = len(l) // 2
        invertida_lista = list(invertida)
        print(invertida_lista)
        print(f'Termo médio da lista: {invertida_lista[intermediario]}')  
    imprime_valor_intermediario(lista)    

                
            
            
    