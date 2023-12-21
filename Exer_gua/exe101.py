def voto(ano_nasc):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if 18 <= idade <= 65:
        f = f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade > 65:
        f = f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        f = f'Com {idade} anos: VOTO NEGADO!'
    return f


situação = int(input('Em que ano você nasceu? '))
print(voto(situação))
