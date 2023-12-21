def ficha(nome = '<Desconhecido>', gols = 0):
        print(f'o jogador {nome} fez {gols} gols no campeonato' )


#Função principal
name = str(input('NOME: ')).strip().upper()
n = str(input('GOLS: ')).strip().upper()
if n.isnumeric():
    int(n)
else:
    n = 0 
if name == '':
    ficha(gols = n)
else:
    ficha(name, n)


