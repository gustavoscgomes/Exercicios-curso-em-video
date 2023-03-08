from random import randint

numero = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'o numeros sorteados foram: {numero}')
print(f'o maior numero foi: {max(numero)}')
print(f'o menor numero foi: {min(numero)}')