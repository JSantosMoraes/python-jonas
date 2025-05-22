print('==== DESAFIO 029 ====')
velocidade = int(input('Digite sua velocidade (O limite da via é 80km/h):'))
velocidade_calc = velocidade - 80

if(velocidade_calc <= 0):
    print('Você não foi multado!')
else:
    multa = velocidade_calc * 7
    print(f'Você foi pego em {velocidade}km/h, e por isso foi multado em R${multa},00')