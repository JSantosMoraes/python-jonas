import random

print('==== CRIAÇÃO DE CPF ==== \n')

estado = str(input('Digite o número correspondente ao seu estado: \n1 - Destrito Federal, Goiás,'
                   'Mato Grosso do sul e Tocantins \n2 - Pará, Amazonas, Acre, Amapá, Rondônia e Roraima'
                   '\n3 - Ceará, Maranhão e Piauí \n4 - Pernambuco, Rio Grande do Norte, Paraíba e Alagoas'
                   '\n5 - Bahia e Sergipe \n6 - Minas Gerais \n7 - Rio de Janeiro, e Espírito Santo'
                   '\n8 - São Paulo \n9 - Paraná e Santa Catarina 0 - Rio Grande do Sul\n \nDigite aqui: '))

def oito_numeros():
    numeros = ''.join(str(random.randint(0, 9)) for _ in range(8))
    return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"

concatenacao = str(oito_numeros() + estado)

resulm = []
contador = 10
for caractere in concatenacao:
    if caractere.isdigit():
        numero = int(caractere)
        resultado = numero * contador
        resulm.append(resultado)
        contador -= 1

print("Concatenacao:", concatenacao)
print("Resultados das multiplicações:", resulm)

soma = resulm[0] + resulm[1] + resulm[2] + resulm[3] + resulm[4] + resulm[5] + resulm[6] + resulm[7] + resulm[8]

resto = soma % 11

def J():
    if resto < 2:
        J = 0

    else: J = 11 - resto
    return J

valordej = J()
concatenacao += str(valordej)

print(valordej)
print("Novo valor de concatenacao com J:", concatenacao)


# O método append() em Python é usado para adicionar um elemento ao final de uma lista.
# O método isdigit() em Python é usado para verificar se todos os caracteres em uma string são dígitos (números inteiros), retornando em um valor booleano.