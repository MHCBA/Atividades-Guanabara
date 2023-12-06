print('===========================================================')
print('                     EXERCICIO 36                          ')
print('===========================================================')
val_c = float(input('digite o valor da casa que pretende comprar: '))
sal = float(input('digite o seu salario: '))
anos = float(input('digite em quantos anos pretende pagar: '))
cal_mes = anos*12
cal_men = val_c/cal_mes
cal_por = sal*0.30
if cal_men > cal_por:
    print('infelizmente o credito não foi aceito.\n'
        'tente uma casa com valor mais acessivel ou aumente o tempo de pagamento.')
else:
    print(f'seu crédito foi liberado! você ira pagar parcelas mensais de: R${cal_men :.2f} ')
print('                               fim                                         ')