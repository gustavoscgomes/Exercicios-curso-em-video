print('=' * 50) 
print('=' * 12+ 'consulta para emprestimo'+ '=' * 12)
preco=float(input('Qual valor da casa? '))
salario=float(input('Qual seu salario? '))
tempo=float(input('Quantos anos de financiamento casa? '))
parcela = preco / (tempo * 12)
if parcela < (30 / 100) * salario:
    print('financimento aprovado')
else: 
    print('financimento reprovado')