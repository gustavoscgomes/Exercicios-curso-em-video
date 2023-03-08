velocidade = int(input('Qual sua velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('voce ultrapassou a velocidade permitida e sera multado')
    print(f'sua multa foi de {multa}')
else:
    print('voce etsa dentro do limite')