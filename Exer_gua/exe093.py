jogador = {}
lista_gols = []
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for i in range(0, jogador['Partidas']):
    lista_gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
jogador['Gols'] = lista_gols
print('-='*50)
print(jogador)
print('-='*50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)
c=0
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i in range(0, jogador['Partidas']):
    print(f'=> Na partida {i+1}, fez {jogador["Gols"][i]} gols.')
    c+= jogador["Gols"][i]
print(f'O jogador fez {c} gols em {jogador["Partidas"]} jogos!')
