n1=float(input('Digite o primeiro segmento'))
n2=float(input('Digite o segundo segmento'))
n3=float(input('Digite o terceiro segmento'))
if abs(n2 - n3) < n1 < (n2 + n3) and abs(n1 - n3) < n2 < (n1 + n3) and abs(n1 - n2) < n3 < (n1 + n2):
    if n1 == n2 and n2 == n3:
        print('Os segmentos acima podem formar um triangulo equilatero')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('Os segmentos acima podem formar um triangulo escaleno')
    else:
        print('Os segmentos acima podem formar um triangulo isoceles')
else: 
    print('nao e um triangulo')