print('===========================================================')
print('                     EXERCICIO 40                          ')
print('===========================================================')
n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
media = (n1+n2)/2
if media >=7:
    print(f'sua media final foi de {media} você passou, parabéns!!')
elif media <5:
    print(f'sua media final foi de {media} você está reprovado!')
else:
    print(f'sua media final foi de {media} você está de recuperação! Já comece a estudar para PF')
print('_________fim__________')