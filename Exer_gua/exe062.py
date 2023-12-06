print('===========================================================')
print('                     EXERCICIO 62                          ')
print('===========================================================')
n1 = int(input('Digite o primeiro termo da progressão: '))
n2 = int(input('Digite a razão da progressão '))
termo = n1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end=' -> ')
        termo += n2
        c+=1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('fim')