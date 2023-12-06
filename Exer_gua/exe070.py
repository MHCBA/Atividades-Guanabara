total = 0
lista_produto_1000 = []
produto_1000 = 0
barato = 0
caro = 0
barato_prod = ''
caro_prod = ''
rep = 0
print('===========================================================')
print('                     EXERCICIO 70                          ')
print('===========================================================')
while True:
    cont_ou_nao = ' ' ## definido como ' '  dentro do loop, pois se não após o primeiro loop ele não irá repetir se deseja ou nao continar
    produto = str(input('qual o produto? ')).upper().strip()
    preço = float(input('Qual o preço do produto? '))
    rep+=1
    total += preço
    if preço > 1000:
        lista_produto_1000.append(produto)
        produto_1000 += 1
    if rep == 1:
        barato_prod = produto
        caro_prod = produto
        barato = preço
        caro = preço
    else:
        if barato > preço:
            barato = preço
            barato_prod = produto
        if caro < preço:
            caro = preço
            caro_prod = produto
    while cont_ou_nao not in 'SN':
        cont_ou_nao = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if cont_ou_nao == 'N':
        break
print('#'*80)
print(f'Você gastou {total} no total!')
if produto_1000 > 0:
    print(f'{produto_1000} produto(s) custaram mais que R$1000, listado(s) na sequencia: {lista_produto_1000}')
elif produto_1000 == 0:
    print('nenhum produto custou mais que R$1000')
if barato_prod != '':
    print(f'{barato_prod} custou R${barato:.2f} e foi o produto mais barato.')

if caro_prod != '':
    print(f'{caro_prod} foi o mais caro e custou R${caro:.2f}!')
print('#'*80)    