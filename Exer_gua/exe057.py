print('===========================================================')
print('                     EXERCICIO 57                          ')
print('===========================================================')
sexo = 3
sexo = str(input('Digite o seu sexo m ou f: [M/F]:')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Digite o seu sexo masculino ou feminino: [M/F]:')).upper().strip()[0]
print(f'sexo {sexo} registrado com sucesso!!!')
print('fim')