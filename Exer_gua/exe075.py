c = 0
print('===========================================================')
print('                     EXERCICIO 75                          ')
print('===========================================================')
acu = (int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')))
for cont in acu:
    if cont % 2 == 0:
        c += 1
print(f'o nove aparece {acu.count(9)} vezes')
if 3 in acu:
    print(f'o primeiro 3 foi digitado na posição {acu.index(3)+1}')
else:
    print('o numero três não se encontra nesta lista!')
print(f'os valores pares digitados foram {c}')