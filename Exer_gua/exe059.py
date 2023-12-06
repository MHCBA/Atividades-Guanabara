from time import sleep
print('===========================================================')
print('                     EXERCICIO 59                          ')
print('===========================================================')
cal = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero: '))
while cal != 5:
    cal = int(input('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
digite a operação que deseja: '''))
    if cal == 1:
        print(f'a soma desses dois valores é igual a {n1 + n2}')
        sleep(2)
    elif cal ==2:
        print(f'esses dois valores multiplicados é igual a {n1 * n2}')
        sleep(2)
    elif cal == 3:
        if n1 > n2:
            print(f'o primeiro valor {n1} é o maior')
        if n2 > n1:
            print(f'o segundo valor {n2} é o maior')
        sleep(2)
    elif cal == 4:
        print('reiniciando sistema...')
        sleep(2)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo numero: '))
    elif cal == 5:
        print('saindo...')
        sleep(2)
