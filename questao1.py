tamanhos = []

tvs_vendidas = int(input("Digite quantas tvs foram vendidas hoje: "))

for c in range(tvs_vendidas):
    tamanho_tv = int(input(f"Digite o tamanho da {c+1}ª tv vendida: "))
    tamanhos.append(tamanho_tv)
    
media_tamanhos = sum(tamanhos)/tvs_vendidas
maior_tv = max(tamanhos)
menor_tv = min(tamanhos)

print(f"Os tamanhos das tvs vendidas hoje foram de {tamanhos} polegadas.")
print(f"A média dos tamanhos das tvs vendidas foi de {media_tamanhos} polegadas")
print(f"A maior tv vendida foi de {maior_tv} polegadas")
print(f"A menor tv vendida foi de {menor_tv} polegadas")