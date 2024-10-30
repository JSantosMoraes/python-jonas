print('Vamos abrir uma conta! \n')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
RG = input('Digite seu RG: ')
CPF = input('Digite seu CPF: ')
endereco = input('Digite seu endereço: ')
CEP = input('Digite seu CEP: ')
Credito = 1500

print(f'\nCadastro realizado com sucesso: \n\nInformações:\n\nNome: {nome}\nIdade: {idade}\nRG: {RG}\nCPF: {CPF}\nEndereço: {endereco}\nCEP: {CEP}\n')
print('O valor de crédito liberado foi de R$1.500,00!')

Celular = float(input('Digite o valor do celular para realizar a compra: R$'))

if Credito >= Celular:
    final = Credito - Celular
    print(f'Compra efetuada! O seu saldo atual é de R${final:.2f}')
else:
    print('Saldo insuficiente!')
