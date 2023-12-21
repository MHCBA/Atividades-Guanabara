lista = []
while True:
    alt = 'j'
    n1 = int(input('Digite um numero: '))
    if n1 not in lista:
        lista.append(n1)
    else:
        print('Valor duplicado não vou adicionar')
    while alt not in 'SN':
        alt = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if alt == 'N':
        break
lista.sort()
print(f'A lista dos valores digitados em ordem crescente: {lista}')