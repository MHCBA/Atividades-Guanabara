print('===========================================================')
print('                     EXERCICIO 61                          ')
print('===========================================================')
n1 = int(input('Digite o primeiro termo da progressão: '))
n2 = int(input('Digite a razão da progressão '))
termo = n1
c = 1
while c <= 10:
    print(termo, end=' -> ')
    termo += n2
    c+=1
print('FIM')
 