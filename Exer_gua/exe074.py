from random import randint
print('===========================================================')
print('                     EXERCICIO 74                          ')
print('===========================================================')
c=0
acumula = (randint (1, 100), randint(1, 100), randint(1, 100), randint (1, 100), randint(1, 100))
print('os valores sorteados foram: ')
for n in acumula:
    c+=1
    print(n, end=' -> ' if c < 5 else '')
print('')
print(f'o maior valor desta tupla é o {max(acumula)}')
print(f'o menor valor desta tupla é o {min(acumula)}')