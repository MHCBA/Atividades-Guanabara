cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
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
        num = input(txt)
        if num.strip() == '' or num.isnumeric() == False:
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
        elif num.isnumeric() and float(num) % 1 != 0.0:
            print(cor_vermelha, 'ERRO! Digite um valor inteiro válido!', cor_reset)
        else:
            return num
        
        

number = leiaInt('Digite um numero inteiro: ')
print(f'Você digitou o numero {number}')
