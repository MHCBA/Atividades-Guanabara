print('===========================================================')
print('                     EXERCICIO 48                          ')
print('===========================================================')
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end = " ")
        soma += i
print(f'a soma dos numeros impares e multiplos dentro do escopo de 1 a 500 é igual a {soma}')
print('Fim')
