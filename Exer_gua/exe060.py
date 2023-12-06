print('===========================================================')
print('                     EXERCICIO 60                          ')
print('===========================================================')
n = int(input('Digite o numero para fatoração: '))
c = n
fatorado = 1
while c > 0:
    print(f'{c}', end='')
    print( ' x ' if c > 1  else ' = ', end='' )
    fatorado*=c
    c-=1
print(fatorado)   
'''print(f'o valor {n} fatorado é igual a {fatorado} ')20

from math import factorial
n = int(input('Digite um numero para saber o factorial dele: '))
f = factorial(n)
print(f'o fatorial de {n} é igual a {f}')
'''
'''n = int(input('Digite um numero para fatoração: '))
c = 1
tot = 1  # Inicialize tot com 1, pois qualquer número multiplicado por 1 é o próprio número

while c <= n:
    tot *= c
    c += 1

if n == 0 or n == 1:
    print(f'O fatorial de {n} é igual a 1')
else:
    print(f'O fatorial de {n} é igual a {tot}')'''
