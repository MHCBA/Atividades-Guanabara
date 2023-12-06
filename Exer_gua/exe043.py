print('===========================================================')
print('                     EXERCICIO 43                          ')
print('===========================================================')
print('descubra seu imc')
altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso/altura**2
if imc < 18.5:
    print(f'seu imc é de {imc:.2f} que é considerado abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'seu imc é de {imc:.2f} que é considerado ideal')
elif 25 <= imc < 30:
    print(f'seu imc é de {imc:.2f} que é considerado sobrepeso')
elif 30 <= imc < 40:
    print(f'seu imc é de {imc:.2f} que é considerada obesidade morbida')
