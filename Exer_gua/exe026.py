print('===========================================================')
print('                     EXERCICIO 26                          ')
print('===========================================================')
nm = str(input("digite seu nome> ")).strip()
nm2 = nm.lower().strip()
print(f'seu nome tem {nm2.count("a")} as \n'
    f'primeira vez que a letra "a" aparece é na posição: {nm2.find("a")} \n'
    f'ultima vez que aparece:{nm2.rfind("a")}')
