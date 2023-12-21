# Lista de coordenadas iniciais
lista = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

# Loop para receber valores do usuário e atualizar a lista
for i in range(0, 9):
    # Solicita ao usuário que digite um número para a posição correspondente
    n = int(input(f'Digite o numero da posição {lista[i]}: '))
    
    # Limpa a lista existente e adiciona o novo valor
    lista[i].clear()
    lista[i].append(n)

# Loop para imprimir a lista formatada em 3 linhas
for i in range(0, 9, 3):
    c = 0
    # Imprime os valores formatados em uma linha
    print(f'[{lista[i][0]:^5}] [{lista[i + 1][0]:^5}] [{lista[i + 2][0]:^5}]')
