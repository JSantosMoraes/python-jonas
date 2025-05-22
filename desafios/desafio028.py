import random

print('==== DESAFIO 028 ====')
numero_maquina = random.randint(0, 5)
numero_usuario = int(input('Adivinhe o número entre 0 e 5 que foi escolhido pela máquina:'))
if(numero_usuario < 0 or numero_usuario > 5):
    print('Escolha um número entre 0 e 5!')
elif(numero_maquina == numero_usuario):
    print('Você acertou!')
else:
    print('Você errou!')