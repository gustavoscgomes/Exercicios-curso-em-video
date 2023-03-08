import time
import random
print("""[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura""")
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogada1 = int(input('Qual sua jogada? '))
jogada2 = random.randrange(3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
if jogada1 == 0:
    if jogada2 == 1:
        print(f"""Voce perdeu!!
        O computador escolheu {lista[jogada2]}""")
    elif jogada2 == 2:
        print(f"""Voce ganhou!!
        O computador escolheu {lista[jogada2]}""")
    else:
        print('Jogada invalida')
elif jogada1 == 1:
    if jogada2 == 0:
         print(f"""Voce ganhou!!
        O computador escolheu {lista[jogada2]}""")
    elif jogada2 == 2:
        print(f"""Voce perdeu!!
        O computador escolheu {lista[jogada2]}""")
    else:
        print('Jogada invalida')
elif jogada1 == 2:
    if jogada2 == 0:
        print(f"""Voce perdeu!!
        O computador escolheu {lista[jogada2]}""")
    elif jogada2 == 1:
         print(f"""Voce ganhou!!
        O computador escolheu {lista[jogada2]}""")
    else:
        print('Jogada invalida')
#if jogada1 == 0 and jogada2 == 2 or jogada1 == 1 and jogada2 == 0 or jogada1 == 2 and jogada2 == 1:
#    print(f"""Voce ganhou!!
#    O computador escolheu {lista[jogada2]}""")
#elif jogada1 == 0 and jogada2 == 1 or jogada1 == 1 and jogada2 == 2 or jogada1 == 2 and jogada2 == 0:
#    print(f"""Voce perdeu!!
#    O computador escolheu {lista[jogada2]}""")