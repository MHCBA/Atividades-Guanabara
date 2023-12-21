def notas(*n, sit = False):
    """
    -> Programa recebe notas de alunos e retorna valores
    :param *n: recebe notas
    :param sit: mostra se a situação dos alunos baseados na média

    o programa retorna a maior, menor e media de notas, e caso sit 
    seja diferente de False mostra se a situação da turma é BOA, RAZOÁVEL ou RUIM
    """
    tot = len(n)
    maior = menor = number = media = 0
    for i in range(0, len(n)):
        if i == 0:
            maior = n[i]
            menor = n[i]
        else:
            if maior < n[i]:
                maior = n[i]
            elif menor > n[i]:
                menor = n[i]
        number += n[i]
    media = number/ tot
    if media < 4:
        situacion = ' RUIM'
    elif 4 < media <= 6:
        situacion = 'RAZOAVEL'
    else:
        situacion = 'BOA'
    if sit:
        dicionario = {'total': tot,'Maior': maior, 'Menor': menor, 'Média' : f'{media:.2f}', 'Situação': situacion}
    else:
        dicionario = {'total': tot,'Maior': maior, 'Menor': menor, 'Média' : f'{media:.2f}'}
    return dicionario


n = notas(1, 2, 3, 8, 10, 7, sit=True)
print(n)