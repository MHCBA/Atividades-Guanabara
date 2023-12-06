numeros = []
numerosi = []
soma = 0
print('===========================================================')
print('                     EXERCICIO 50                          ')
print('===========================================================')
for i in range(1, 7):
    num = int(input(f'Digite o {i} valor: '))
    if num %2 == 0:
        numeros.append(num)
        soma+=num
    else:
        numerosi.append(num)
print('os numeros pares desta lista são: ', numeros)
print('os numeros impares desta lista são: ', numerosi)
print('a soma dos numeros pares é igual a:', soma)
