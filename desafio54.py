ano_atual = 2022
count = 0
count2 = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano_atual - ano
    if idade < 18:
        count += 1
    elif idade >= 18:
        count2 += 1
print(f""" Ao todo tivemos {count2} pessoas maiores de idade
e tambem tivemos {count} pessoas menores de idade""")