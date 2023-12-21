lista = []
for i in range(0, 5):
    n1 = int(input('Digite um valor: '))
    if i == 0 or n1 >= lista [-1]:
        lista.append(n1)
        print('Alocado a ultima posição!')
    else:
        for c in range(0, 5):
            if n1 <= lista[c]:
                lista.insert(c, n1)
                print(f'Alocado a posição {c}')
                break
print(f'A lista ficou desta maneira: {lista}')