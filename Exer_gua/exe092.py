pessoa = {}
idade_tra = {}
pessoa['Nome'] = str(input('Digite o nome:'))
pessoa['idade'] = int(input('Digite o ano de nascimento: '))
pessoa['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['Ctps'] != 0:
    pessoa['Ano_cont'] = int(input('Digite o ano de contratação'))
    pessoa['Salario'] = float(input('Salario: '))
    idade_tra = pessoa['Ano_cont'] - pessoa['idade'[:]]
    pessoa['Aposentadoria'] = idade_tra + 35
    pessoa['idade'] = 2023 - pessoa['idade']
else:
    pessoa['idade'] = 2023 - pessoa['idade']
print('-='*50)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
