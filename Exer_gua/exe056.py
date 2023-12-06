p_vez = 0
p_vez1 = 0 
soma = 0
soma_20 = 0
older = 0
nome_velho = ''
print('===========================================================')
print('                     EXERCICIO 56                          ')
print('===========================================================')
for i in range (1, 5):
    nome = str(input(f'digite o {i} nome: '))
    idade = int(input('Digite sua idade:'))
    sexo = int(input('digite o 1 se for masculino e 2 para feminino: '))
    soma+= idade
    if i == 1 and sexo == 1:
        older = idade
        nome_velho = nome
    if sexo == 1 and idade > older:
        older = idade
        nome_velho = nome
    if sexo == 2 and idade < 20:
        soma_20 + 1
media = soma / 4
print(f'a media de idade desse grupo é {media}')
print(f'o homem mais velho tem {older} anos e o nome dele é {nome_velho}')
print(f'{soma_20} tem menos de vinte anos')


