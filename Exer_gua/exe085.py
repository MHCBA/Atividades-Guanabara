lista_princ = [[],[]]
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista_princ[0].append(n)
    else:
        lista_princ[1].append(n)
lista_princ[0].sort()
lista_princ[1].sort()
print('Os numeros pares digitados em ordem crescente: ', lista_princ[0])
print('Os numeros impares digitados em ordem crescente:',lista_princ[1])
