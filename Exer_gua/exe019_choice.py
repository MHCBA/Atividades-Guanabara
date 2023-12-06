print('===========================================================')
print('                     EXERCICIO 19                          ')
print('===========================================================')
import random
n1 = str(input('digite o nome do primeiro aluno: '))
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('digite o nome do terceiro aluno: '))
n4 = str(input('digite o nome do quarto aluno: '))
lista2 = [n1, n2, n3, n4]
sorteio2 = random.choice(lista2)
print(f'o aluno {sorteio2} será o escolhido  para apresentar')
