print('===========================================================')
print('                     EXERCICIO 71                          ')
print('===========================================================')
valor = int(input('Digite um valor para saque: '))
cel = 50
totced = 0
while True:
    if valor >= cel:
        valor-=cel
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de {cel}')
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1 
        totced = 0
        if valor == 0:
            break
print('FIM')