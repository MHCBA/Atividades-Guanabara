from random import randint
print('===========================================================')
print('                     EXERCICIO 68                          ')
print('===========================================================')
v_c = 0
par_ou_imp = ' '
while True:
    nplayer = int(input('Digite um numero: '))
    computador = randint(0, 101)
    valor_final = nplayer + computador
    while par_ou_imp not in 'PI':
        par_ou_imp = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]    
    
    if valor_final %2 == 0 and par_ou_imp == 'P':
        valor_p_i = 'Par'
        print(f'Você jogou {nplayer} e o computador jogou {computador}. Total de {valor_final}. deu {valor_p_i}')
        print('Você venceu!')
        print('Vamos jogar novamente!!')
        v_c += 1
    elif valor_final %2 != 0 and par_ou_imp == 'I':
        valor_p_i = 'Impar'
        print(f'Você jogou {nplayer} e o computador jogou {computador}. Total de {valor_final}. deu {valor_p_i}')
        print('Você venceu!')
        print('Vamos jogar novamente!!')
        v_c += 1
    elif valor_final %2 == 0 and par_ou_imp == 'I':
        valor_p_i = 'Par'
        break
    elif valor_final %2 != 0 and par_ou_imp == 'P':
        valor_p_i = 'Impar'
        break
print('-_'*50)
print(f'Você jogou {nplayer} e o computador jogou {computador}. Total de {valor_final}. deu {valor_p_i}')
print(f'_-'*50)
print(f'Você Perdeu! você teve {v_c} vitórias consecutivas!')
print('-='*50)