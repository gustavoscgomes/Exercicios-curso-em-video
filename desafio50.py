count = 0
s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º numero: '))
    if n % 2 == 0:
        s = s + n
        count = count + 1 
print(f' a soma dos {count} numeros pares é: {s}')