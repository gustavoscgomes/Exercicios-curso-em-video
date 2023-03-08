distancia = float(input('Qual distancia da sua viagme? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'Sua viajem custara {preco}')
