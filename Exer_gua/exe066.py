print('===========================================================')
print('                     EXERCICIO 66                          ')
print('===========================================================')
s=c=0
while True:
    n = int(input('Digite um numero! (999) para parar: '))
    if n == 999:
        break
    s+=n 
    c+=1 
print(f'Você errou {c} vezes!!!')
print(f'A soma dos numeros errados digitado é igual a {s}')