import random

print('==== CRIAÇÃO DE CPF ==== \n')

estado = str(input('Digite o número correspondente ao seu estado: \n1 - Destrito Federal, Goiás,'
                   'Mato Grosso do sul e Tocantins \n2 - Pará, Amazonas, Acre, Amapá, Rondônia e Roraima'
                   '\n3 - Ceará, Maranhão e Piauí \n4 - Pernambuco, Rio Grande do Norte, Paraíba e Alagoas'
                   '\n5 - Bahia e Sergipe \n6 - Minas Gerais \n7 - Rio de Janeiro, e Espírito Santo'
                   '\n8 - São Paulo \n9 - Paraná e Santa Catarina 0 - Rio Grande do Sul\n \nDigite aqui: '))

def oito_numeros():
    numeros = ''.join(str(random.randint(0, 9)) for _ in range(8))
    return numeros

concatenacao = str(oito_numeros() + estado)

resulm = []
contador = 10
for caractere in concatenacao:
    if caractere.isdigit():
        numero = int(caractere)
        resultado = numero * contador
        resulm.append(resultado)
        contador -= 1

soma = sum(resulm)
resto = soma % 11

def J():
    if resto < 2:
        J = 0

    else: J = 11 - resto
    return J

valordej = J()
concatenacao += str(valordej)

resulm_k = []
contador_k = 11
for caractere in concatenacao:
    if caractere.isdigit():
        numero = int(caractere)
        resultado = numero * contador_k
        resulm_k.append(resultado)
        contador_k -= 1

soma_k = sum(resulm_k)
resto_k = soma_k % 11

def K():
    if resto_k < 2:
        return 0
    else:
        return 11 - resto_k

valordek = K()
concatenacao += str(valordek)

ordenacao = (f'{concatenacao[:3]}.{concatenacao[3:6]}.{concatenacao[6:9]}-{concatenacao[9:]}')

print(f'\n\nO resultado da criação do seu CPF é: {ordenacao} \n\nDetalhes da criação: \n- Os oito primeiros números são'
      f'criados aleatoriamente. \n- O nono número é escolhido de acordo com o seu estado. \n- Os digitos verificadores'
      f'são definidos pelo resto da divisão da soma de uma multiplicação sequenciada')


# O método append() em Python é usado para adicionar um elemento ao final de uma lista.
#n é usado para verificar se todos os caracteres em uma string são dígitos (números inteiros), retornando em um valor booleano.