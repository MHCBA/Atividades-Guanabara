from time import sleep
print('===========================================================')
print('                     EXERCICIO 71                          ')
print('===========================================================')
banco = "BANCO CHELL'S"
print('='*50)
print(f'{banco:^50}')
print('='*50)
n_sacar = int(input('Digite o valor a ser sacado? R$'))
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0
while True:
    if n_sacar >= 50:
        n_sacar -= 50
        notas_50 +=1
        if notas_50 > 0 and n_sacar < 50:
            print(f'total de {notas_50} cedulas de R$50')
    if n_sacar < 50 and n_sacar >= 20:
        n_sacar -= 20
        notas_20 += 1
        if notas_20 > 0 and n_sacar < 20:
            print(f'total de {notas_20} cedulas de R$20')
    if n_sacar < 20 and n_sacar >=10:
        n_sacar -= 10
        notas_10 += 1
        if notas_10 > 0 and n_sacar < 10:
            print(f'total de {notas_10} cedulas de R$10')
    if n_sacar < 10 and n_sacar >=1:
        n_sacar -= 1
        notas_1 +=1
        if notas_10 > 0 and n_sacar < 1:
            print(f'total de {notas_1} cedulas de R$1')
    if n_sacar == 0:
        break
print('='*50)
print("Volte sempre ao BANCO CHELL'S!")
