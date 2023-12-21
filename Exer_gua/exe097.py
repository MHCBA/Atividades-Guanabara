def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f'{txt:^{len(txt) + 2}}')
    print('~' * (len(txt) + 2))


escreva(str(input('Digite um texto (somente em string): ')))