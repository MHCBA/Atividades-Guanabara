from time import sleep
cor_verde = "\033[92m"
cor_reset = "\033[0m"
cor_branca = "\033[97m"
cor_magenta = "\033[95m"
color_code = f"\033[{92};{47}m"
color_code2 = f"\033[{95};{43}m"
txt = 'SISTEMA DE AJUDA PyHELP'
def ajuda(func):
    txt2 = f'ACESSANDO O MANUAL DO COMANDO {func.upper()}'
    print(color_code2 + '~' * (len(txt2) + 2), cor_reset)
    print(color_code2 + f'{txt2:^{len(txt2) + 2}}', cor_reset)
    print(color_code2 + '~' * (len(txt2) + 2), cor_reset)
    sleep(1)
    print(color_code)
    help(func)
    print(cor_reset)
    

# FUNÇÃO PRINCIPAL
while True:
    print(cor_verde + '~' * (len(txt) + 2))
    print(f'{txt:^{len(txt) + 2}}')
    print('~' * (len(txt) + 2), cor_reset)

    function = str(input(('Função ou Biblioteca > ')).strip())
    if function.upper() == 'FIM':
        break
    else:
        ajuda(function)
