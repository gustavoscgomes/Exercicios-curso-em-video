numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove')
while True:
    posicao = int(input('Digite um numero entre 0 e 20: '))
    if posicao < 0 or posicao > 20:
        posicao = int(input('erro. digite novamente: '))
    print(numero[posicao])
    continuar = input('Digite N para fechar ou outra letra para continuar: ').upper()
    if continuar == 'N':
        break