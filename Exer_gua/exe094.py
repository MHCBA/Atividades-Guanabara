pessoas = [[],]
pessoas_dic = {}
c=0
media_idade = 0
while True:
    alt = 't'
    c+=1
    pessoas_dic.clear()
    pessoas_dic = {"Nome":str(input('Nome: ')), "Idade": int(input('Idade:')), "Sexo" : str(input('Sexo [M/F]: ').upper().strip()[0])}
    media_idade += pessoas_dic['Idade']
    pessoas.append(pessoas_dic.copy())
    if pessoas_dic['Sexo'] in 'F':
        pessoas[0].append(pessoas_dic['Nome'])
    while alt not in 'NS': 
        alt = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if alt in 'N':
        break
print('-'*50)
media_idade = media_idade/c
print(f'- Foram cadastradas {c} pessoa(s)!')
print(f'- A media de idade é de {media_idade} anos')
if pessoas[0] != []:
    print('- As mulheres cadastradas foram: ', pessoas[0]) 
else:
    print('- Mulheres não foram cadastradas !')
print('- A lista das pessoas que estão acima da média:')
print('-'*50)
for val in pessoas[1:]:
    if val['Idade'] >= media_idade:
        print('     ')
        print('-'*50)
        for k, v in val.items():
            print(f'{k} = {v};', end=' ') 
        print('')
print('-'*50)    
