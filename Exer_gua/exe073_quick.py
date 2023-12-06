time = ('Flamengo', 'Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'São Paulo',
    'Fluminense', 'Bahia', 'Cuiabá', 'Santos', 'Internacional',
    'Juventude', 'Ceará', 'Athletico Paranaense', 'Corinthians', 'América Mineiro',
    'Sport', 'Grêmio', 'Chapecoense', 'Vasco da Gama', 'Botafogo')
print('===========================================================')
print('                     EXERCICIO 72                          ')
print('===========================================================')
print('-='*50)
print(f'Lista de times do brasileirão: {time}')
print('-='*50)
print(f'Os 5 primeiros times da tabela do brasileirão são: {time [0:5]}')
print('--'*50)
print(f'Os 4 ultimos times são: {time[len(time)-4: len(time) +1 ]}')
print('--'*50)
print(f'Times em ordem alfabética: {sorted(time)}')
print('--'*50)
print(f'botafogo se encontra na  {time.index("Botafogo")+1}ª posição')
print('-='*50)
