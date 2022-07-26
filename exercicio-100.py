from random import randint

def sorteio(list):

    for c in range(1, 6):
        list.append(randint(1, 10))
    print(f'Sorteando os 5 valores da lista:')
    for k, v in enumerate(list):
        print(f' {v} ', end=" ")
    print(' PRONTO!')


def par(list):
    soma = 0
    for k, v in enumerate(list):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {a}, temos {soma}')


a = []
sorteio(a)
par(a)
