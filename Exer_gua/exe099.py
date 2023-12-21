from time import sleep
from random import randint
def maior(*valores):

    c = maior2 = 0
    print('-='*50)
    print('Analisando os valores passados...')
    sleep(1)
    for i in valores:
        print(i, end =' ',flush=True)
        sleep(0.5)
        c+=1
        if c == 1:
            maior2 = i
        else:
            if maior2 < i:
                maior2 = i
    print(f'Foram informados {c} valores ao todo') 
    print(f'O maior valor informado foi de {maior2}')
    sleep(2) 


maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100) )