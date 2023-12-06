print('===========================================================')
print('                     EXERCICIO 63                          ')
print('===========================================================')
n = int(input('digite quais primeiros elementos da lista de finobacci você deseja ver: ')) 
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
lista = []
if n == 1:
    lista.append(t1)
elif n == 2:
    lista.append(t1)
    lista.append(t2)
elif n == 3:
    lista.append(t1)
    lista.append(t2)
    lista.append(t3)
elif n >= 4:
    lista.append(t1)
    lista.append(t2)
    lista.append(t3)
    t1 = t2
    t2 = t3
    while c < n:
        t3 = t1 + t2
        c+=1
        lista.append(t3)
        t1 = t2
        t2 = t3
        
print(f'os primeros {n} termos da lista de fibonacci são: {lista} ')