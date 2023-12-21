from time import sleep
from random import randint
jogador = {'Jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
print('Valores Sorteados: ')
for j, i in jogador.items():
    print(f'    O {j} tirou {i}')
    sleep(1)
ranking = sorted(jogador.items(), key=lambda item: item[1], reverse = True)
print('Ranking: ')
for j, f in enumerate(ranking):
     print(f'{j +1} lugar: {f[0]} com {f[1]}')
     sleep(1)
