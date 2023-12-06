print('===========================================================')
print('                     EXERCICIO 42                          ')
print('===========================================================')
n1 = int(input('digite o tamanho da primeira reta: '))
n2 = int(input('digite o tamanho da segunda reta: '))
n3 = int(input('digite o tamanho da terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('pode se tornar um triangulo!')
    #verifica o tipo de triangulo
    if n1 == n2 == n3:
        print('se tornaria um triangulo equilatero, ou seja,  todos os lados iguais')
        if n1 == 10:
            print('yessir é dez boi')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('seria um trinagulo isosceles, ou seja, que possui dois lado iguais')
    else:
        print('seria um triangulo esscaleno, ou seja, todos os lados sao diferentes')
else:
    print('não pode se tornar um triangulo!')
print('_______fim_______')