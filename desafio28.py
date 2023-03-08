import random
numero = int(input('Digite um numero para o computador tentar adivinhar'))
if numero == random.randrange(6):
    print('Vcoe acertou')
else:
    print('voce perdeu')
    print(f'o numero era {random.randrange(6)}')

