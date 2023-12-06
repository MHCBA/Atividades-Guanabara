print('===========================================================')
print('                     EXERCICIO 34                          ')
print('===========================================================')
sal = float(input('digite o seu salario: '))
if sal>1250:
    print(f'o seu aumento será de 10% o seu salario final será de: {sal+(sal*0.10)}')
if sal<1250:
    print(f'o seu aumento será de 15% o seu salario final será de: {sal+(sal*0.15)}')
print("_"*27, 'fim',"_"*27)
