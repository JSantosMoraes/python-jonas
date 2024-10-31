# Crie um programa python que leia o nome completo de uma pessoa  e motre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem primeiro nome

print('==== DESAFIO 22 ====')

nome = str(input('Digite seu nome completo: '))
print('Seu nome com todas as letras maiúsculas:',nome.upper())
print('\n Seu nome com todas as letras minúsculas:',nome.lower())
print('\n Quantas letras ao todo tem seu nome sem considerar os espaços:',len(nome.replace(" ", "")))
dividido = nome.split()
print('\n Quantas letras tem seu primeiro nome:', len(dividido[0]))
# que lindo cara

