print('===========================================================')
print('                     EXERCICIO 27                          ')
print('===========================================================')
nm = str(input('digite o seu nome completo: ')).strip()
nm2 = nm.split()
print(f'seu primeiro nome é {nm2[0]} \n' 
      f'seu sobrenome é: {nm2[1]} \n'
      f'seu ultimo nome é: {nm2[len(nm2)-1]} \n')
