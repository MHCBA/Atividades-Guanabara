lista= [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
c_ul = 0
maior = 0
for i in range(0, 9):
    n = int(input(f'Digite o numero da posição {lista[i]}: '))
    lista[i].clear()
    lista[i].append(n)
print('-='*36)
for i in range(0, 9, 3):
    c = 0
    print(f'[   {lista[i][0]:^5}   ] [   {lista[i + 1][0]:^5}   ] [   {lista[i + 2][0]:^5}   ]')
    c_ul += lista[i + 2][0]
print('-='*36)    
for i , n in enumerate(lista):
    if n[0] % 2 == 0:
        c+=n[0]
    if i == 2:
        maior = lista[i][0]
    elif i < 6:
        if maior < lista[i][0]:
            maior = lista[i][0]
print(f'A soma de todos os valores pares é igual a {c}')
print(f'A soma dos valores da terceira coluna é igual a {c_ul}')
print(f'O maior valor da segunda linha é o {maior}')       
        