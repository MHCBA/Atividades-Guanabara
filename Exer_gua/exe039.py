import math
from datetime import date
print('===========================================================')
print('                     EXERCICIO 39                          ')
print('===========================================================')
ano_atual = date.today().year 
nasc = int(input('Informe o teu ano de nascimento para você saber se ja deve se alistar: '))
idade = ano_atual - nasc
cal_idade = (idade - 18)**2
if idade < 18:
    print(f'''Você ainda tem {idade} de idade ainda falta(m) {math.sqrt(cal_idade)} ano(s) para você se alistar.
seu alistamento será em {nasc + 18}!!!!!''')
elif idade > 18:
    print(f'''Você deveria ter se alistado a {idade - 18} anos atrás!
o seu ano de alistamento foi em {nasc + 18}''')
else:
    print('Agora é a hora para você se alistar!!')