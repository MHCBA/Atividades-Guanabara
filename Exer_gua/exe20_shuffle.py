print('===========================================================')
print('                     EXERCICIO 20                          ')
print('===========================================================')
from random import shuffle
n1 = str(input('escreva o nome do primeiro aluno: '))
n2 = str(input('escreva o nome do segundo aluno: '))
n3 = str(input('escreva o nome do terceiro: '))
n4 = str(input('escreva o nome do ultimo aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'a ordem de apresentação será: {lista}')
