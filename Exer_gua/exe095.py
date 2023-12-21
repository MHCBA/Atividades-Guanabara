jogador = {}
lista_gols = []
jogadores = []

while True:
    alt = 't'
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    for i in range(0, jogador['Partidas']):
        lista_gols.append(int(input(f'  Quantos gols na partida {i + 1}? ')))
    jogador['Gols'] = lista_gols[:]
    print(f'{lista_gols}')
    jogadores.append(jogador.copy())
    lista_gols.clear()
    jogador.clear()
    while alt not in 'SN':
        alt = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if alt == 'N':
        break

print('-='*50)
print(jogadores)
print('-='*50)
c=cont=0
print(f'{"No":<4} {"NOME:":<18} {"Gols:"} {"Total:":>21}')
for i in range(0, len(jogadores)):
    cont = 0
    print('-'*50)
    for numb in jogadores[i]["Gols"]:
        c += jogadores[i]["Gols"][cont]
        cont += 1
    print(f'{i + 1:<5} {jogadores[i]["Nome"]:<19} {str(jogadores[i]["Gols"]):<22} {c}')
    c= 0
print('-'*50)
while True:
    alternativa = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if alternativa == 999:
        break
    elif alternativa > i + 1 or alternativa < 0:
        print('Opção invalida, erro!')
    else:
        jogador_selecionado = jogadores[alternativa - 1]
        print(jogador_selecionado['Partidas'])
        print(jogadores[alternativa - 1]['Nome'])
        print(f'O jogador {jogadores[alternativa - 1]["Nome"]} jogou {jogadores[alternativa - 1]["Partidas"]} partidas')
        for y in range(0, (jogador_selecionado['Partidas'])):
            print(f'=> Na partida {y +1}, fez {jogadores[alternativa - 1]["Gols"][y]} gols.')
            c+= jogadores[alternativa - 1]["Gols"][y]
        print(f'O jogador fez {c} gols em {jogador_selecionado["Partidas"]} jogos!')
    

print('-'*50)
    