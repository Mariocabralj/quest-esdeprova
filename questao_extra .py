botao = int(input("Digite o primeiro botão (de 0 a 5) pressionado: "))
if botao > 5:
    print("Botão não encontrado.")
botao2 = int(input("Digite o segundo botão (de 0 a 5) pressionado: "))
if botao2 > 5:
    print("Botão não encontrado.")


soma_botes = botao + botao2


if soma_botes == 0 :
    print("Reproduzindo música Cheia de manias... ")
elif soma_botes == 1: 
    print("Repduzindo música Me leva junto com você...")
elif soma_botes == 2:
    print("Reproduzindo música É tarde demais... ")
elif soma_botes == 3:
    print("Reproduzindo música Quando te encontrei... ")
elif soma_botes == 4:
    print("Reproduzindo música Deus me livre... ")
elif soma_botes == 5:
    print("Reproduzindo música Ciúme de você... ")
elif soma_botes == 6: 
    print("Reproduzindo música Cigana...")
else:
    print("A soma dos botões gerou um valor que não foi possível encontrar na lista! ")