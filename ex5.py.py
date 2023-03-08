
tempo = 0
populacaoa = int(input('Tamanho a populacao A: '))
populacaob = int(input('Tamanho da populacao B: '))
taxa_a = float(input('Taxa de crescimento A em %'))
taxa_b = float(input('Taxa de crescimento B em %'))
if populacaob > populacaoa and taxa_a > taxa_b:
    while (populacaob > populacaoa):
        populacaoa = populacaoa + (populacaoa * (taxa_a/100))
        populacaob = populacaob + (populacaob * (taxa_b/100))
        tempo = tempo + 1
elif populacaob < populacaoa and taxa_a < taxa_b:
    while (populacaob < populacaoa):
        populacaoa = populacaoa + (populacaoa * (taxa_a/100))
        populacaob = populacaob + (populacaob * (taxa_b/100))
        tempo = tempo + 1
else:
    print('ERRO')
print(f'Sao necessarios {tempo} anos')