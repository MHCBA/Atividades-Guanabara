print('===========================================================')
print('                     EXERCICIO 31                          ')
print('===========================================================')
dis = int(input('digite a distancia da viagem em km: '))
lim = 200
cal = dis*0.50
cal2 = dis*0.45
if dis<=lim:
    print(f'o valor ser pago será de: R${cal:.2f}')
else:
    print(f'o valor a ser pago será de: R${cal2:.2f}')
print('fimmmmmmmmmmmmm')