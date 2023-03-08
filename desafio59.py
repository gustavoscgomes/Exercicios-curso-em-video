n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = True
while opcao != '5':
    print("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numero
    [5] sair""")
    opcao = input('Digite a opcao: ')
    while opcao == '4':
        n1 = int(input('Primeiro valor: '))
        n2 = input(input(('Segundo valor: ')))
    if opcao == '1':
        print(f'{n1 + n2}')
    if opcao == '2':
        print(f'{n1 * n2}')
    if opcao == '3':
        if n1 > n2:
            print(n1)
        else:
            print(n2)
print('Fim')
