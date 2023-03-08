#37) Uma academia deseja fazer um senso entre seus clientes 
# para descobrir o mais alto, o mais baixo, a mais gordo 
# e o mais magro, para isto você deve fazer um programa 
# que pergunte a cada um dos clientes da academia seu 
# código, sua altura e seu peso. O final da digitação 
# de dados deve ser dada quando o usuário digitar 0 (zero) 
# no campo código. Ao encerrar o programa também deve ser 
# informados os códigos e valores do clente mais alto, do 
# mais baixo, do mais gordo e do mais magro, além da média 
# das alturas e dos pesos dos clientes

maisalto = 0
maisbaixo = 0
maisgordo = 0
maismagro = 0
cod = '1'
codmaisgordo = '1'
codmaismagro = '1'
codmaisalto = '1'
codmaisbaixo = '1'
count = 0
while cod != '0':
    cod = str(input('Digite o codigo: '))
    peso = float(input('Digite o peso: '))
    altura = float(input('Altura: '))
    count +=1
    if count == 0:
        codmaismagro = cod
        codmaisgordo = cod
        codmaisalto = cod
        codmaisbaixo = cod
        maisalto = altura
        maisbaixo = altura
        maisgordo = peso
        maismagro = peso
    if altura > maisalto:
        maisalto = altura
        codmaisalto = cod
    if peso > maisgordo:
        maisgordo = peso
        codmaisgordo = cod
    if altura < maisbaixo:
        maisbaixo = altura
        codmaisbaixo = cod
    if peso < maismagro:
        maismagro = peso
        codmaismagro = cod
print(f"""mais magro: {codmaismagro} {maismagro}
mais gordo : {codmaisgordo} {maisgordo}
mais baixo: {codmaisbaixo} {maisbaixo}
mais alto: {codmaisalto} {maisalto}""")
