#3 - Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre - 
# os em uma lista, já na posição de inserção (sem usar o sort())
# . No final, mostre a lista ordenada na tela.

numeros = []

for c in range (5):
    numero = int(input('Digite um numero. '))

    if not numeros or numero > numeros[-1]: # se o contador estiver em zero ou o numero digitado for maior
        numeros.append(numero) # que o ultimo elemento da lista adicione o novo elemento no final da lista.
        print('Adicionado ao final da lista... ')
    else:
        pos = 0
        while pos < len(numeros): # enquanto a posição for menor que a quantidade de elementos na lista.
            if numero <= numeros [pos]: # condição de filtro para verificar se o numero que vou inserir
                 # na lista é menor ou igual oque já está dentro na posição atual que está o contador.
                numeros.insert(pos, numero) #caso verdadeiro vou inserir o elemento na posição que está o contador.
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1 # passo o contador para a proxima posição.

print('-=' *30 )
print (f'Os valores digitados em ordem são {numeros}')

