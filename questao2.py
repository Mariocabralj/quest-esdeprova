lista_de_convidados = []
nomes_repetidos = []

c = 0

num = int(input("Digite quantos convidados serão adicionados na sua lista: "))

for c in range (num):
    nomes_convidados = input(f"Digite o nome do seu {c+1}º convidado: ").upper()
    lista_de_convidados.append(nomes_convidados)

if lista_de_convidados[0:num] == nomes_convidados:
    nomes_repetidos.append(nomes_convidados)

print(f"A seguir, podemos verificar os convidados para a festa: {lista_de_convidados}")
print(f"Os convidados com nomes repetidos são esses: {nomes_repetidos}")
