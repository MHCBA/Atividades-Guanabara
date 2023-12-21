lista = []
for i in range(1, 6):
    n1 = int(input('Digite um valor numerico: ' ))
    lista.append(n1)
print('o maior valor desta lista é: ', max(lista), " que se encontra na posição: ", lista.index(max(lista)))
print('o menor valor desta lista é: ', min(lista), " que se encontra na posição: ", lista.index(min(lista)))
