# Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores impares digitados, respectivamente.
# Ao final mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:

    numero = int(input('Digite um número. '))
    numeros.append(numero)

    if numero %2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

    pergunta = input('Deseja continuar ? [S/N]').upper()

    while pergunta not in 'SN': #filtro de resposta se corresponde ao solicitado.
        pergunta = input('Resposta invalida. Digite S ou N ').upper()

    if pergunta == 'N': #condição para aplicar o break do loop.
        break

numeros.sort()
pares.sort()
impares.sort()

print(f'A lista com todos os números é {numeros}')
print(f'A lista só com pares é {pares}')
print(f'A lista só com impares é {impares}')