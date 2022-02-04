def class_parcial(primeiro, segundo, terceiro, **outros):
    op = str(input('Houve trapaça?')).strip().upper()[0]
    quarto = ''
    quinto = ''
    ultimo = ''
    if 'N' in op:
        for posicao, corredor in outros.items():
            if posicao == '4':
                quarto = corredor
            elif posicao == '5':
                quinto = corredor
            elif posicao == '6':
                ultimo = corredor
    elif 'S' in op:
        colocacao = [primeiro, segundo, terceiro]
        colocacao.extend(outros.values())  # adiciona à lista os valores do dicionário

        trapaceiro = str(input('QUEM TRAPACEOU? : '))
        vitima = str(input('QUEM FOI PREJUDICADO? : '))

        posTrapaceiro = colocacao.index(trapaceiro)  ## Retorna os indices dos corredores na lista 'colocacao'
        posVitima = colocacao.index(vitima)

        colocacao[posTrapaceiro] = vitima
        colocacao[posVitima] = trapaceiro

        classFinal(*colocacao)  ## DESEMPACOTA A LISTA PARA SER ENVIADA À FUNÇÃO 'classFinal'

    else:
        print('Digite uma opção válida!')


def classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo):
    print('Classificação Final: ')
    print(f'Primeiro: {primeiro}')
    print(f'Segundo: {segundo}')
    print(f'Terceiro: {terceiro}')
    print(f'Quarto: {quarto}')
    print(f'Quinto: {quinto}')
    print(f'Ultimo: {ultimo}')

    # classFinal(primeiro, segundo, terceiro, quarto, quinto, ultimo)


print('CORREDORES: ')
print('MERCÚRIO(MC), PAPA-LÉGUAS(PL), SUPER-HOMEM(SH), FLASH(FS), SONIC(SN), LIGEIRINHO(LG)')
print('INFORME A POSIÇÃO DOS CORREDORES:')

pri = str(input('Vencedor: '))
seg = str(input('Segundo: '))
ter = str(input('Terceiro: '))
qua = str(input('Quarto: '))
quin = str(input('Quinto: '))
ult = str(input('Ultimo: '))

outros = {'4': qua, '5': quin, '6': ult}

class_parcial(pri, seg, ter, **outros)
