pt = int(input('primeiro termo: '))
r = int(input('razao: '))
count = 1
mais = 1
total = 10
while mais != 0:
    total += mais
    while count != total:
        pt += r
        count += 1
        print(f'{pt}-', end='')
    print('pausa')
    mais = int(input('quantos mais? '))
print('fim')