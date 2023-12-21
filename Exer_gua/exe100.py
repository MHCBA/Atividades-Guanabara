from random import randint
from time import sleep
lista2 = []
def sorteio(lista):
    print('Sorteando os valores da lista: ', end='')
    for i in range(0, 5):
        sleep(0.5)
        n = randint(1, 100)
        print(n, end=' ', flush=True)
        lista.append(n)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


numero = list()
sorteio(numero)
somaPar(numero)