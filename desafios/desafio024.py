# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
print('==== DESAFIO 024 ====')
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')