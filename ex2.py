#50) Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
n = int(input('Digite o numero de termos: '))
soma = 1
print(f'H= 1', end='')
for c in range (2, n + 1):
    soma = soma + 1/c
    print(f' + 1/{c}',end='')
print(f' \n A soma é {soma:.2f}')