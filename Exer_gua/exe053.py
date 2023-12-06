print('===========================================================')
print('                     EXERCICIO 53                          ')
print('===========================================================')
frase = str(input('digite uma frase: ')).strip().upper()
juntar = frase.replace(' ', '')
letras =''
print(f'{juntar}')

for i in range(len(juntar)-1, -1, -1):
    letras += juntar[i]
print(letras)
if letras == juntar:
    print('é um palindromo')
else:
    print('não é um palindromo')