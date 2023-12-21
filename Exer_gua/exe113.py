cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
def Leiareal(txt):
    while True:
        try:
            num = float(input(txt))
           
        except (ValueError, TypeError):
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        except KeyboardInterrupt:
            print('')
            print(cor_vermelha, 'O usuário prefiriu não informar os dados!', cor_reset)
            return 0
        except Exception as erro:
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        else:
            print('')
            return num

        


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
            num = int(input(txt))
        except (ValueError, TypeError):
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        except KeyboardInterrupt:
            print(cor_vermelha,'O usuário prefiriu não informar os dados!', cor_reset)
            return 0
        except Exception as erro:
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
            continue
        else:
            return num


n = leiaInt('DIGITE UM VALOR INTEIRO: ')
print(f'O valor digitado foi o {n}')
n2 = Leiareal('Digite um numero real: ')
print(f'O valor inteiro digitado foi o {n} e o real foi {n2}')
 