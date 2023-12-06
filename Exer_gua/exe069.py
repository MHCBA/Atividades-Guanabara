idade_18 = 0
homem_c = 0
mulher_20 = 0
print('===========================================================')
print('                     EXERCICIO 69                          ')
print('===========================================================')
while True:
    print('-'*50)
    print(f'{"CADASTRE UMA PESSOA":^50}')
    print('-'*50)
    idade = int(input('idade: '))
    sexo = ' '
    cont_ou_nao = ' '
    while sexo not in 'FM':
        sexo = str(input('sexo? [M/F]: ')).upper().strip()[0]
    if idade > 18:
        idade_18 += 1
    if sexo == 'M':
        homem_c += 1
    if sexo == 'F' and idade > 20:
        mulher_20 += 1
    while cont_ou_nao not in 'SN':
        cont_ou_nao = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if cont_ou_nao == 'N':
        break
print(f'{idade_18} pessoas tem mais que 18 anos de idade')
print(f'{homem_c} homem(ns) foram cadastrados!')
print(f'{mulher_20} mulher(es) tem mais de 20 anos!')
