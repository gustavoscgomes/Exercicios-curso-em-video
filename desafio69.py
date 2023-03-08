
h = hmais = mmais = 0 
while True:
    print('Cadastre uma pessoa')
    idade = int(input('idade: '))
    sexo = input('sexo: ').upper()
    if sexo == 'H':
        h += 1
    if sexo == 'H' and idade > 18:
        hmais += 1
    if sexo == 'M' and idade > 20:
        mmais += 1
    continuar = input('quer continuat? S/N').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('quer continuat? S/N').upper()
    if continuar == 'N':
        break
print(f"""homens = {h}
homem com mais de 18 = {hmais}
mulher com mais de 20 = {mmais}""")

