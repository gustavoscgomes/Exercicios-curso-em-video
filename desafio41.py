from datetime import date
ano_nascimento = int(input('Qual seu ano de nascimento'))
data = date.today().year
idade = data - ano_nascimento
print(f'O atleta tem {idade} ano(s)')
if idade > 0 and idade < 9:
    print('Categoria mirin')
elif idade >= 9 and idade < 14:
    print('categoria infantil')
elif idade >= 14 and idade < 19:
    print('categoria junior')
elif idade >= 19 and idade < 25:
    print('categoria senior')
elif idade >= 25:
    print('categoria master')
 