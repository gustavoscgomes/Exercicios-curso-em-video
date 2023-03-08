c = 0
numero = (int(input('Digite um numero:')), int(input('Digite mais um numero:')), int(input('Digite mais um numero:')),
        int(input('Digite mais um numero:')), int(input('Digite mais um numero:')))
print(f'voce digitou: {numero}')
print(f'o numero 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'o numero 3 apareceu na {numero.index(3)+1} posicao')
for n in numero:
    if n % 2 == 0:
        print(n)