print('===========================================================')
print('                     EXERCICIO 23                          ')
print('===========================================================')
num = int(input('digite o primeiro numero até 9999: '))
u = num //1 %10
d = num//10 %10
c = num //100 %10
m = num//1000 %10 
print(f'unidade: {u}\n'
      f'dezena: {d}\n'
      f'centena: {c}\n'
        f'milhar: {m}\n')
'''n = str(num)
print(f'analisando o numero {num}')
print(f'unidade: {n[3]}')
print(f'dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'milhar: {n[0]}')'''
