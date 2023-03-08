valor = float(input('Quanto voce quer sacar? R$ '))
ced = 50
totalced = 0
while True:
    if valor >= ced:
        valor -= ced
        totalced += 1
    else:
        print()