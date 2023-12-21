galera = list()
temp = list()
aluno = '9'
while True:
    temp.append(str(input('Digite o nome do aluno: ')).upper().strip())
    temp.append(float(input('Digite a nota da prova 1: ')))
    temp.append(float(input('Digite a nota da prova 2: ')))
    media = (temp[1] + temp[2]) / 2 
    temp.append(media)
    galera.append(temp[:])
    temp.clear()
    alt = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if alt in 'Nn':
        break
print('-'*35)
print(f'{"No":<4} {"NOME:":<18} MÉDIA:')
for i, pessoa in enumerate(galera):
    print(f'{i:<5}{pessoa[0] :<19} {pessoa[3]:<9}')
print('-'*35)
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno != 999:
        print(f'a notas de {galera[aluno][0]} foram {galera[aluno][1:3]}')
 