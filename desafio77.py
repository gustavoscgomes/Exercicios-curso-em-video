palavras = ('APRENDER', 'PROGRAMAR', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'PYTHON')
for palavra in palavras:
    print(f'\n{palavra} ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')