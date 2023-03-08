soma = 0
vezes = 0
maior = 0
menor = 0
cont = True
while cont != 'N':
    n = int(input('numero: '))
    soma += n
    vezes += 1
    if soma == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    cont = input('quer continuar? ').upper()
media = soma / vezes
print(f"""voce digitou {vezes} numeros a media foi{media}
e a soma foi {soma} o maior {maior} e o menor {menor}""")

