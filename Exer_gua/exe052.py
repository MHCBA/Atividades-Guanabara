cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_reset = "\033[0m"
tot = 0
print('===========================================================')
print('                     EXERCICIO 52                          ')
print('===========================================================')
n = int(input('digite um numero para saber se ele é primo ou não: '))
for i in range (1, n +1 , 1):
    if n % i == 0:
        print(cor_vermelha, i, cor_reset, end = ' ')
        tot += 1
    else:
        print(cor_verde, i, cor_reset, end=' ')
print(f'o numero {n} foi divisivel {tot} vezes')
print('')
if tot > 2:
    print('não é um numero primo!!')
else:
    print('é um numero primo!!')