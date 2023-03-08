import random
count = 0
while True:
    computador = random.randrange(11)
    p_ou_i = input('par/impar: ')
    numero = int(input('numero: '))
    print(f'o computador escolheu {computador}')
    soma = computador + numero
    if soma % 2 == 0 and p_ou_i == 'P':
        print('voce ganhou')
    elif soma % 2 != 0 and p_ou_i == 'I':
        print('voce ganhou')
    else:
        print('voce perdeu')
        break
