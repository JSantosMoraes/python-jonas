print('==== DESAFIO 034 ====')
salario = int(input('Qual é o seu salário atual? R$'))
aumento = 0

if(salario > 1250):
    aumento = (salario/100) * 10
    salario = salario + aumento

else:
    aumento = (salario/100) * 15
    salario = salario + aumento

print(f'Seu novo salário é de R${salario}')