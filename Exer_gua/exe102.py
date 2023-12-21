def fatorial(valor, show=False):
    """
    -> Funcao para saber o fatorial de um valor
    :param valor: numero a ser fatorado
    :param show: (OPCIONAL) mostra o calculo e resultado
    :Return: Retorna o resultado da fatoracao do valor 
    Funcao feita por Michell Vasconcelos 
    """
    c = 1
    for i in range(valor, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end= '' )
            else:
                print(' = ' , end= '' )
        c *= i
    return c


print(fatorial(9, True))
help(fatorial)