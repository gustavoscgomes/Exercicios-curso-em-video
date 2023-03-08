ano = int(input('Digite seu ano de nascimento: '))
ano_atual = 2022
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
if idade < 18:
    alistamento = 18 - idade
    ano_alistamento = ano_atual + alistamento
    print(f'Ainda faltam {alistamento} Ano(s) para o seu alistamento')
    print(f'seu alistamento sera em {ano_alistamento}')
else:
    alistamento = 18 - idade
    ano_alistamento = ano_atual + alistamento
    print(f'Seu alistamento foi em {ano_alistamento}') 