print('===========================================================')
print('                     EXERCICIO 55                          ')
print('===========================================================')
peso_anterior = 0
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Digite o seu {i} peso:') )
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

    
print(f'o menor peso é o {menor}')
print(f'o maior é o {maior}')