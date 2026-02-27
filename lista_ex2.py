numeros = []

while True:
    numero = int(input('Digite um número. '))
    if numero not in numeros:
        numeros.append(numero)
        
    else:
        print('Esse número já está na lista e não será adicionado')

    pergunta = input('Quer continuar [S/N]').upper()
    if pergunta != 'S':
        break

print (numeros.sort())


        
