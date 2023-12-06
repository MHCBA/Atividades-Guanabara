tupla = ('Drake', 'TravisScott', 'KidCudi', 'KanyeWest', 'Yeat', '21Savage')
print('===========================================================')
print('                     EXERCICIO 77                          ')
print('===========================================================')
print(f'As palavras salvas são {tupla}')
for words in tupla:
    print('')
    print(f'a palavra {words} tem as vogais: ')
    for letras in words:
        if letras.lower in "aeiou":
            print(letras, end=' ' )

