lista = []
print('Programa que analisa se a expressão que você digitou está correta! ')
exp = input('Digite uma expressão: ')
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
            if len(lista) > 0:
                lista.pop()
            else:                       ## funciona para caso que o ')' esteja no começo da lista e tambem se tiver mais do ) que abertos (
                lista.append(')')
                break  
print(lista)                                          ##caso não tenha valor dará um erro, pois pop precisa de valor para funcionar!
if len(lista) == 0:
    print('A expressão digitada está correta!')
else:
    print('A expressão digitada está errada!')
print('fim')    