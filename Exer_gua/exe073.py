Tabela_Brasileirao_2023 = ('Flamengo', 'Atlético Mineiro', 'Palmeiras', 'Fortaleza', 'São Paulo',
    'Fluminense', 'Bahia', 'Cuiabá', 'Santos', 'Internacional',
    'Juventude', 'Ceará', 'Athletico Paranaense', 'Corinthians', 'América Mineiro',
    'Sport', 'Grêmio', 'Chapecoense', 'Vasco da Gama', 'Botafogo')
c = 0
print('===========================================================')
print('                     EXERCICIO 73                          ')
print('===========================================================')
print('='*50)
print('Os cinco primeiros colocados do brasileirão são: ')
for cont in Tabela_Brasileirao_2023:
    c+=1
    if c <= 5:
        print('-'*50)    
        print(f' o {c}ª colocado é o {cont}')
    elif c >= 16:
        print('-'*50)
        if c == 16:
            print('Os ultimos 4 colocados da tabela são: ')
            print('-'*50)
        print(f'{cont} em {c}ª')
    elif cont == 'Chapecoense':
        print('-'*50)
        print(f'chapecoense se encontra na {c}ª posição')
print('-'*50)
print(f'''Os times do brasileirao em ordem alfabetica: 
{sorted(Tabela_Brasileirao_2023)}''')
print('-='*50)

