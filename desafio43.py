peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / altura ** 2 
print(f'Seu imc é: {imc:,.2f}.', end='')
if imc < 18.5:
    print('voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu peso esta normal')
elif 25 <= imc < 30:
    print('voce esta com sobrepso')
elif 30 <= imc < 40:
    print('voce esta obeso')
elif imc > 40:
    print('voce esta com obesidade morbida')