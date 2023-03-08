soma = 0
count = 0
while True:
    numero = int(input('numero: '))
    if numero == 999:
        break
    count += 1
    soma += numero

print(soma, count)