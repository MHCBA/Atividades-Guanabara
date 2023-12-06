from datetime import date
from time import sleep
print('===========================================================')
print('                     EXERCICIO 41                          ')
print('===========================================================')
print('Descubra sua categoria de acordo com sua idade')
sleep(1)
ano = int(input('digite o seu ano de nascimento para saber em qual categoria irá entrar: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    print(f'Você tem {idade} anos de idade fará parte da categoria mirim!')
elif idade <= 14:
    print(f'Você tem {idade} anos de idade você faz parte da categoria infantil!')
elif idade <= 19:
    print(f'Você tem {idade} anos de idade, Você faz parte da categoria junior')
elif 1<= 25:
    print(f'Você tem {idade} anos de idade, você faz parte da categoria senior')
else:
    print(f'Você tem {idade} anos de idade, você faz parte da categoria master')
print("-="*40)
print('                                    fim')
print("-="*40)