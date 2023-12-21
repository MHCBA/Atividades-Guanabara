lista_temp = []
pessoas = []
mais = 0
menos = 0
while True:
    lista_temp.append(str(input('Digite o nome: ')))
    lista_temp.append(int(input('Digite o peso: ')))
    if len(pessoas) == 0:
        mais= menos = lista_temp[1]
    else:
        if mais < lista_temp[1]:
            mais = lista_temp[1]
        if menos > lista_temp[1]:
            menos = lista_temp[1]
    pessoas.append(lista_temp[:])
    lista_temp.clear()
    alt = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if alt in 'Nn':
        break
print('-='*30)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {mais}. As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if p[1] == mais:
        print('[{p[0]}]', end = '')
print('')
print(f'O menor peso foi de {menos}. As pessoas mais leves são: ', end='')
for p in pessoas:
    if p[1] == menos:
        print(f'[{p[0]}]', end = '')
print('')