print('===========================================================')
print('                     EXERCICIO 35                          ')
print('===========================================================')
n1 = int(input('digite o tamanho da primeira reta: '))
n2 = int(input('digite o tamanho da segunda reta: '))
n3 = int(input('digite o tamanho da terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('pode se tornar um triangulo!')
else:
    print('não pode se tornar um triangulo equilatero!')
print('_______fim_______')