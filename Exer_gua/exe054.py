from datetime import date
ano_atual = date.today().year 
quant = 0
quant_m = 0 
print('===========================================================')
print('                     EXERCICIO 54                         ')
print('===========================================================')
for i in range(1, 8):
    data_nasc = int(input('Digite o seu ano de nascimento: '))
    idade = ano_atual - data_nasc
    if idade >= 18:
        quant = i
    else:
        quant_m = i
print(f'a quantidade de pessoas de menor é {quant_m} e de maior é {quant}')
