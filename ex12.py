n1 = 1
n2 = 1
nesimo = int(input('Digite o n-ésimo termo da serie de Fibonacci: '))
for c in range(2,nesimo):
    termo = n2 + n1
    n1 = n2
    n2 = termo
    c += 1
    print(termo)