from time import sleep
print('===========================================================')
print('                     EXERCICIO 64                          ')
print('===========================================================')
n = c = soma = 0
print('Você caiu em um labirinto!!!''')
sleep(2)
print('''para sair dele você tem que adivinha a senha!!!''')
sleep(1)
print('a senha é um numero dentro do escopo de 0 a 999')
sleep (2)
n = int(input('digite um numero inteiro entre 0 a 999: '))
while n != 999:
    c +=1
    soma+=n
    n = int(input('digite um numero inteiro entre 0 a 999: '))
print('')
print(f'''Boa!!! voce conseguiu sair do labirinto, voce errou {c} vezes
para conseguir acertar a senha e sair do labirinto''')
print(f'A soma dos numeros errados digitados é igual a {soma}')