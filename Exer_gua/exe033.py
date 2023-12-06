print('===================================================================')
print('                           EXERCICIO 33                            ')
print('===================================================================')
n1 = float(input('digite o primeiro numero:'))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))
maior = n3
menor = n3
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
    #verificando qual é o maior
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
    #verificando qual é o menor
print(f'o numero {maior} é o maior')
print (f'o numero {menor} é o menor')
print('++++++++++++++++++++++++++++++fim+++++++++++++++++++++++++++++++++++')