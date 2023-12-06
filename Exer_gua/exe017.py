print('===========================================================')
print('                     EXERCICIO 17                          ')
print('===========================================================')
from math import hypot
n1 = int(input('digite o cateto adjacente: '))
n2 = int(input('digite o oposto: '))
hipotenusa = hypot(n1, n2)
print(f' o comprimento da hipotenusa: {hipotenusa}')
