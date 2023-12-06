print('===========================================================')
print('                     EXERCICIO 32                          ')
print('===========================================================')
from datetime import date
anob = int(input('digite o ano que deseja, digite 0 para analisar o ano atual: '))
if anob==0:
    anob = date.today().year
anob2 = anob%4
if anob2==0 and anob%100!= 0 or anob % 400 == 0:
    print('O ano informado é bissexto!')
else:
    print('O ano informado não é bissexto!')
print('_____fim_____')
