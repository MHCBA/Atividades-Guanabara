brasil = []
aluno = {}
while True:
    aluno['Nome'] = str(input('Nome do aluno: '))
    aluno['Media'] = int(input(f'Média final do aluno {aluno["Nome"]}: '))
    if aluno['Media'] < 7:
        aluno['Situação'] = 'Recuperação'
    elif aluno['Media'] < 2:
        aluno['Situação'] = 'Reprovado'
    else:
        aluno ['Situação'] = 'Aprovado'
    brasil.append(aluno.copy())
    alt = str(input('Deseja continuar? ')).upper().strip()[0]
    if alt == 'N':
        break
print('-' * 70)
for i in range(0, len(brasil)):
    print(f'O aluno {brasil[i]["Nome"]} com media final igual a {brasil[i]["Media"]} está {brasil[i]["Situação"]}')
print('-' * 70)
