lista = []
par = []
impar = []
while True:
    choice = 'y'
    n1 = int(input('digite um valor: '))
    lista.append(n1)
    if choice != 'SN':
        choice = str(input('Você deseja continuar? [S/N]: ')).upper().strip()
    if choice == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
print(f'A lista com todos os valores digitados: {lista}')
print(f'A lista de todos os valores pares desta lista: {par}')
print(f'A lista de todos os valores impares desta lista: {impar}')