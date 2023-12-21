from time import sleep
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
        
def escolha(n):
    if n == 1 or n ==2:
        print('-'*50)
        print(f'{f"Opção {n}":^50}')
        print('-'*50)
    elif n == 3:
        print('-'*50)
        print(f'{f"Saindo do sistema..":^50}')
        print('-'*50)

def leiaInt(txt):
    """
    Função que recebe uma mensagem (txt) e solicita ao usuário a inserção de um valor inteiro.

    Parâmetros:
    - txt (str): Mensagem a ser exibida para solicitar a entrada do usuário.

    Retorna:
    - int: Valor inteiro inserido pelo usuário.

    A função continua solicitando a entrada até que um valor inteiro válido seja inserido.
    Um valor é considerado válido se for uma representação numérica inteira (sem casas decimais).
    Caso contrário, a função exibe uma mensagem de erro e solicita a entrada novamente.
    """
    while True:
        try:
            num = int(input(f'{cor_verde}{txt}{cor_reset}'))
        except (ValueError, TypeError):
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        except KeyboardInterrupt:
            print(cor_vermelha,'O usuário prefiriu não informar os dados!', cor_reset)
            return 0
        except Exception as erro:
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        if num > 3 or num < 1:
            print(cor_vermelha + 'ERRO! Opção invalida!', cor_reset)
            break
        else:
            return num
while True:
    print('-'*50)
    print(f'''{cor_verde}1 - {cor_azul}Ver pessoas cadastradas
{cor_verde}2 - {cor_azul}Cadastrar novas pessoas
{cor_verde}3 - {cor_azul}Sair do sistema{cor_reset}''')
    print('-'*50)
    num = leiaInt('SUA OPÇÃO: ')
    escolha(num)

    if num == 3:
        break
