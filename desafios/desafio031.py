print('==== DESAFIO 031 ====')
distancia = int(input('Cobramos o valor da passagem de acordo com a quantidade de quilômetros que você vai percorrer. \nViagem de até 200Km: R$0,50 p/km.\nViagem acima de 200Km: R$0,45 p/km.\n'))
valor = 0

if(distancia <= 200):
    valor = distancia * 0.50
    print(f'O valor da viagem é de R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'O valor da viagem é de R${valor:.2f}')