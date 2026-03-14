# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos 
# e fechados na ordem correta.

expressão = input('Digite uma expressão. ')

contador = 0

for simbolo in expressão:

    if simbolo == '(':
        contador += 1
    elif simbolo == ')':
        contador -= 1
    if contador < 0:
        print('A expressão está com os parenteses em ordem incorreta.')
        break
if contador == 0:
    print ('A expressão está com os parenteses em ordem correta.')
else:
    print('A expressão está com os parenteses em ordem incorreta.')

