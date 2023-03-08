primeiro_termo = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razao'))
for c in range(primeiro_termo, primeiro_termo + (11 - 1)*razao, razao):
    print(f'{c} - ', end='')