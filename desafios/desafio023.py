# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# unidade, dezena, centena, milhar

print('==== DESAFIO 023 ====')
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')