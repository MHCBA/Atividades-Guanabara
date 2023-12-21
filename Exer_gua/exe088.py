# Importa as bibliotecas necessárias
from time import sleep
from random import randint

# Imprime linhas de separação
print('-' * 50)
# Imprime o título centralizado na tela
print(f'{"JOGA NA MEGA SENA":^50}')
# Imprime mais linhas de separação
print('-' * 50)

# Inicializa a lista vazia para armazenar os números sorteados
jogo = []
# Inicializa os contadores de jogos e o número gerado
c = n1 = 0

# Solicita ao usuário a quantidade de jogos a serem gerados
n = int(input('Quantos jogos você quer que eu sorteie? '))

# Loop principal para gerar jogos
while True:
    # Inicializa um contador para controlar a quantidade de números gerados
    cont = 0
    
    # Loop interno para gerar 6 números distintos
    while cont < 6:
        n1 = randint(1, 60)
        
        # Verifica se o número gerado não está na lista 'jogo'
        if n1 not in jogo:
            jogo.append(n1)
            cont += 1  # Incrementa o contador de números gerados
    
    # Ordena a lista 'jogo'
    jogo.sort()
    
    # Imprime o jogo gerado
    print(f'Jogo {c + 1}: {jogo}')
    
    # Limpa a lista 'jogo' para o próximo sorteio
    jogo.clear()
    
    # Incrementa o contador de jogos
    c += 1
    
    # Pausa a execução por 1 segundo entre os jogos
    if c < n:
        sleep(1)
    
    # Sai do loop principal quando a quantidade desejada de jogos foi gerada
    if c == n:
        break