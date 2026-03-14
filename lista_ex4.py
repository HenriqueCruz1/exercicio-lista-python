#Crie um programa que vai ler varios números e colocar em uma lista.

#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

numeros = [] #cria a lista números
while True: #condição loop se verdadeiro

    numero = int(input('Digite um numero. ')) #pergunta ao usuario
    numeros.append(numero) #adiciona o número a lista

    pergunta = input('Deseja continuar [S/N]').upper() #validação de permanencia do usuario.

    while pergunta not in 'SN': #filtro de resposta se corresponde ao solicitado.
        pergunta = input('Resposta invalida. Digite S ou N ').upper()

    if pergunta == 'N': #condição para aplicar o break do loop.
        break

print('-' * 30)

print (f'A quantidade de números digitados foi: {len(numeros)}') #função para ler a quantidade de elementos na lista.

(numeros.sort(reverse=True)) #ferramenta para deixar a lista ordenada e aplicar a condição reversa.
print (numeros)

if 5 in numeros: #validação para o caso do número 5 estar na lista.
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não está na lista.')
