from time import sleep
import os
print('===========================================================')
print('                     EXERCICIO 65                          ')
print('===========================================================')
while True:
    os.system('cls')
    maior = 0
    menor = 0
    answer = 1
    i = 0
    s = 1
    soma = 0
    answer2 = 1
    print('Digite no minimo dois numeros para que você descubra a media e, o maior e menor entre eles')
    sleep(2)

    while answer == 1:
        num = float(input(f'Digite o seu {s}ª numero:') )
        i+= 1
        if i == 1:
            maior = num
            menor = num
            s+=1
            soma+=num
        else:
            soma+=num
            s+=1
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
            answer = int(input('Voce deseja continuar se sim digite [1] se nao digite [0] -> '))
    print('-='*50)
    print(f'A media dos numeros digitado é igual a: {soma / (s-1)}')
    print(f'Dentre os {s-1} numeros digitados...')   
    print(f'o menor numero é o {menor}')
    print(f'o maior é o {maior}')
    print('-='*50)
    answer2 = int(input('Quer executar o programa novamente? [1] para sim e [0] para não: '))
    if answer2 != 1:
        break

