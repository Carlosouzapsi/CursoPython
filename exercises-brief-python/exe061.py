licenca = str(input('Informe o número da licença: ')).upper()

if len(licenca) == 6 and \
        licenca[0] >= "A" and licenca[0] <= "Z" and \
        licenca[1] >= "A" and licenca[1] <= "Z" and \
        licenca[2] >= "A" and licenca[2] <= "Z" and \
        licenca[3] >= "0" and licenca[3] <= "9" and \
        licenca[4] >= "0" and licenca[4] <= "9" and \
        licenca[5] >= "0" and licenca[5] <= "9":
    print("A licença é válida para o formato antigo")
elif len(licenca) == 7 and \
        licenca[0] >= "A" and licenca[0] <= "Z" and \
        licenca[1] >= "A" and licenca[1] <= "Z" and \
        licenca[2] >= "A" and licenca[2] <= "Z" and \
        licenca[3] >= "0" and licenca[3] <= "9" and \
        licenca[4] >= "0" and licenca[4] <= "9" and \
        licenca[5] >= "0" and licenca[5] <= "9" and \
        licenca[6] >= "0" and licenca[6] <= "9":
    print("A licença possui o formato novo.")
else:
    print('Formato da licença é inválido.')
