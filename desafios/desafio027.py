# Faça um programa que leia um nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente.
print('==== DESAFIO 027 ====')
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')
