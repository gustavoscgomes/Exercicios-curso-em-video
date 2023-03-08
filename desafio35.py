n1=float(input('Digite o primeiro segmento'))
n2=float(input('Digite o segundo segmento'))
n3=float(input('Digite o terceiro segmento'))
if abs(n2 - n3) < n1 < (n2 + n3) and abs(n1 - n3) < n2 < (n1 + n3) and abs(n1 - n2) < n3 < (n1 + n2):
    print('é um triangulo')
else: 
    print('nao e um triangulo')