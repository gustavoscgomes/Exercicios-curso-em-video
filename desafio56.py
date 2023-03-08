somaidade = 0
idadehmv = 0
nomehmv = ''
countm = 0
for c in range(1, 5):
    print('-'* 5 , f'{c}ª Pessoa','-' * 5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    somaidade = somaidade + idade
    if c == 1 and sexo == 'M':
        idadehmv = idade
        nomehmv = nome
    if sexo == 'M' and idade > idadehmv:
        idadehmv = idade
        nomehmv = nome
    if sexo == 'F' and idade < 20:
        countm = countm + 1
mediaidade = somaidade / 4
print(f'a media de idade e:{mediaidade}')
print(f'o homem mais velho tem {idadehmv} anos e se chama {nomehmv}')
print(f'tem {countm} ,uler com menos de 20 anos')