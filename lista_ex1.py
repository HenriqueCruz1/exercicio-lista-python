# 1 -  Faça um programa que leia 5 valores numéricos e guarde em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []

for c in range (5):
    numero = (int(input('Digite um número. ')))
    numeros.append(numero)
    maior = numeros[1]
    if numero > maior:
        maior = numero
    menor = numeros[1]
    if numero < menor:
        menor = numero
        
print (numeros)
print (maior)
print (menor)


        