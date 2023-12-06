print('===========================================================')
print('                     EXERCICIO 51                          ')
print('===========================================================')
n1 = int(input('Digite o primeiro termo da progressão: '))
n2 = int(input('Digite a razão da progressão '))
decimo = n1 + (10-1) * n2
for i in range(n1, decimo + n2, n2):
    print(i, end=' -> ')
print('FIM')

