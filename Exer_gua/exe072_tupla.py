numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 21
print('===========================================================')
print('                     EXERCICIO 72                          ')
print('===========================================================')
while True:
    n = int(input('digite um numero de 0 a 20 para vê-lo por extenso:'))
    if n >=0 and n <= 20:
        break
print(f'o numero {n} digitado por extenso é {numeros[n]}')
