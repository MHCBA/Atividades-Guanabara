print('===========================================================')
print('                     EXERCICIO 22                          ')
print('===========================================================')
nome = str(input('Qual é o seu nome completo? '))
letras = len(nome) - nome.count (' ') #função para contar e retirar espaços
print(f'Analisando seu nome...\n' #/n serve para quebrar linha
      f'Seu nome em  maiúsculas é {nome.upper()}\n'
      f'Seu nome em minúsculas é {nome.lower()}\n'
      f'Seu nome tem ao todo {letras} letras\n'
      f'Seu primeiro nome tem {nome.find(" ")} letras \n')





