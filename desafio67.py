while True:
    numero = int(input('quer ver tabuada de qual valor? '))
    print('-'*30)
    if numero < 0:
        break
    for c in range(1,11):
        print(f'{numero} x {c} = {numero * c}')
    print('-'*30)
print('-'*13+ 'Fim', '-'*13)