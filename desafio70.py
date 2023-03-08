soma = 0
maior = 0
nomemenor = True
maisdemil = 0
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if preco > 1000:
        maisdemil += 1
    if soma == 0:
        menor = preco
        nomemenor = nome
    if preco < menor:
        nomemenor = nome
        menor = preco
    soma += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? S/N ').strip().upper()[0]
    if continuar == 'N':
        break
print(f"""o total da compra foi R${soma}
tivemos {maisdemil} produto(s) custando mais de R$1000
o produto mais barato foi {nomemenor} que custou R${menor}""")