import random
numero = random.randrange(10)
print("""Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi?""")
palpite = int(input('Qual seu palpite? '))
count = 1
while palpite != numero:
    if palpite > numero:
        palpite = int(input('menos ...tente mais uma vez: '))
    if palpite < numero:
        palpite = int(input('mais...tente mais uma vez'))
    count+= 1
print(f'fim... voce acertou em {count} vezes.')