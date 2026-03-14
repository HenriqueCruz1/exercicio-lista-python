#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já esteja lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    
    numero = int(input('Digite um número.'))
    
    if numero not in numeros:
        numeros.append(numero)
    else:
        print('Esse número já existe na lista e não será adicionado')

    pergunta = input('Deseja continuar ? [S/N]').upper()

    while pergunta not in 'SN': #filtro de resposta se corresponde ao solicitado.
        pergunta = input('Resposta invalida. Digite S ou N ').upper()

    if pergunta == 'N': #condição para aplicar o break do loop.
        break

numeros.sort()
print(f'Os números cadastrados com sucesso foram {numeros}')
    

    


        