#3 - Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre - 
# os em uma lista, já na posição de inserção (sem usar o sort())
# . No final, mostre a lista ordenada na tela.

numeros = []

for c in range (5):
    numero = int(input('Digite um numero. '))
    numeros.append(numero)

print (numeros)

