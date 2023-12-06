from time import sleep
print('===========================================================')
print('                     EXERCICIO 59                          ')
print('===========================================================')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
saída = False
while not saída:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa''')
    escolha = int(input('Qual a sua opção? '))
    if escolha == 1:
        print(f'a soma de {n1} e {n2} é igual a {n1 + n2}')
        sleep(2)
    elif escolha == 2:
        print(f'a multiplicação de {n1} e {n2} é igual a {n1*n2}')
        sleep(2)
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} o primeiro valor digitado é o maior')
        if n2 > n1:
            print(f'{n2} o segundo valor digitado é o maior')
        sleep(2)
    elif escolha == 4:
        print('Reiniciando sistema...')
        sleep(2)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Saindo...')
        sleep(2)
        saída = True 