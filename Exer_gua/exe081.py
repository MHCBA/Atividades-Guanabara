lista = []
vezes = 0
while True:
    alternativa = 'j'
    n1 = int(input('Digite um valor: '))
    lista.append(n1)
    while alternativa not in 'SN':
        alternativa = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if alternativa == 'N':
        break
print('-='*50)
print(f'Foram digitado(s):  {len(lista)} numeros ao total!')
print('a lista de forma decrescente: ')
if 5 in lista:
    print(f'O valor 5 se encontrada nas posições:')
    for pos,n in enumerate(lista):
        if n == 5:
            print(f'{pos}...', end='')
            vezes+=1 
    print(f'')
    print(f'e foi digitado {vezes} vezes')
else:
    print(f'Não foi digitado o valor 5 nesta lista!')
lista.sort(reverse=True)          
print(lista)