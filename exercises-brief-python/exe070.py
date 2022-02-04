while True:
    bits = input("Informe o número de bits: ")
    if bits == "":
        print("Programa encerrado pelo usuário.")
        break
    else:
        if bits.count("0") + bits.count("1") != 8 or len(bits) != 8:
            print("Erro. Precisar ser 8 bits")
        else:
            ocorr_um = bits.count("1")
            ### Contando o número de ocorrências de "1":
            if ocorr_um % 2 == 0:
                print("A paridade do bit deve ser 0.")
            else:
                print("A paridade do bit deve ser 1.")
