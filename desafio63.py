quant = int(input('quantos termos? '))
count = 1
t1 = 0
t2 = 1
t3 = 0
print(f'{t1}-{t2}-', end='')
while count != quant:
    count += 1
    t3 = t1 + t2
    print(f'{t3}-', end='')
    t1 = t2
    t2 = t3
    
    