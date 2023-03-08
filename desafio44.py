preconormal = float(input('Preco das compras: R$'))
print("""[ 1 ] a vista dinheiro
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao """)
opcao = input('Qaul a opcao? ')
if opcao == '1':
    precofinal = preconormal - (preconormal * (10/100))
    print(f'voce ira pagar {precofinal}')
elif opcao == '2':
    precofinal = preconormal - (preconormal * (5/100))
    print(f'voce ira pagar  {precofinal}')
elif opcao == '3':
    print(f'sua compra sera parcelada em 2x de {preconormal/2}')
elif opcao == '4':
    precofinal = preconormal + (preconormal * (20/100))
    parcelas = int(input('Quantas parcelas? '))
    print(f'sua compra sera parcelada em {parcelas}x de {precofinal/parcelas} com juros')