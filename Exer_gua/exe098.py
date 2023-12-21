import math
from time import sleep
def contador(i, m, f):

    print(f'Contagem de {i} até {m} de {math.sqrt(f**2)} em {math.sqrt(f**2)}:')
    if m > i:
        for c in range(i, m + 1 if f > 0 else m - 1, math.sqrt(f**2)):
            print(c, end=' ', flush=True)
            sleep(0.5)
    else:
        for c in range(i, m - 1 if f > 0 else m - 1, math.sqrt(f**2) *(-1)):
            print(c, end=' ', flush=True)
            sleep(0.5)
    if f == 0 and i > m:
        for c in range(i, m -1 if f > 0 else m - 1, math.sqrt(f**2) - 1):
            print(c, end=' ', flush=True)
            sleep(0.5)
    elif f == 0 and m > i:
        for c in range(i, m + 1 if f > 0 else m - 1, math.sqrt(f**2) + 1):
            print(c, end=' ', flush=True)
            sleep(0.5)
    
    print('FIM!')
    sleep(1)

contador(1, 10, 1)
contador(10, 0, 2)
while True:
    alt = 'T'
    print('Agora sua vez de personalizar o contador!')
    contador(int(input('Ínicio: ')), int(input('Fim: ')), int(input('Passo: ')))
    while alt not in 'SN':
        alt = str(input('Mais uma vez? [S/N]: ')).upper().strip()[0]
    if alt == 'N':
        break
    