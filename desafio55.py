maior = 0
menor = 0
for p in range(1, 8):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            peso = menor
print(f'o maior peso foi {maior} e o menor foi {menor}')