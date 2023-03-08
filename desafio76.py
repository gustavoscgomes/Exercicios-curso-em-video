produtos = ('leite', 4.5,
            'banana', 2.99,
            'arroz', 3.9,
            'cuscuz', 1.9,
            'pao', 3.5,
            'queijo', 4.5,
            'mamao', 5.5)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:-<30}', end='')
    else:
        print(f'R${produtos[item]:>6}')