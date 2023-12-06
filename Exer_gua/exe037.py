cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
print('===========================================================')
print('                     EXERCICIO 37                          ')
print('===========================================================')
n1 = int(input('digite um numero inteiro para conversão: '))
n2 = int(input(f'qual base de conversão você deseja converter o numero fornecido? 1 para {cor_amarela} binario{cor_reset}, 2 para {cor_azul}octal{cor_reset} e 3 para {cor_vermelha}hexadecimal{cor_reset}: '))
binario = bin(n1)
octal = oct(n1)
hexadecimal = hex(n1)

if n2 == 1:
    print(f'O numero inteiro {n1} convertido para binario é igual a: {binario[2:]}')
elif n2 == 2:
    print(f'O numero inteiro {n1} convertido para octal é igual a: {octal[2:]}')
elif n2 == 3:
    print(f'O numero inteiro {n1} convertido para hexadecimal é igual a: {hexadecimal[2:]}')
else:
    print('Numero invalido! escreva um numero inteiro de 1 a 3')

print('                                    fim                                            ')