def valor_em_centimetros(num):
    pergunta = input("Deseja formatar o valor para centímetros? (S/N) ").upper()
    if pergunta == 'S':
        valor_em_centimetros = valor*100
        print(f"O seu número {valor} em cms é {valor_em_centimetros} ")
    else:
        print("Você desejou não seguir com a conversão.")



def valor_em_quilometros(num):
    pergunta = input("Deseja formatar o valor para quilômetros? (S/N) ").upper()
    if pergunta == 'S':
        valor_em_quilometros = valor/1000
        print(f"O seu número {valor} em kms é {valor_em_quilometros} ")
    else:
        print("Você desejou não seguir com a conversão.")


valor = int(input("Digite o valor em metros: "))
pergunta_norteadora = int(input(f"Deseja formatar {valor} metros para (1)centímetros ou (2)quilômetros? "))
if pergunta_norteadora == 1:
    valor_em_centimetros(valor)
elif pergunta_norteadora == 2:
    valor_em_quilometros(valor)