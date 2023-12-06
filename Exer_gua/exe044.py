from time import sleep
print('===========================================================')
print('                     EXERCICIO 44                          ')
print('===========================================================')
print ('{:=^80}'.format("Chell's room"))
sleep(2)
print("Seja bem vindo a loja Chell's room")
sleep(2)
produto = str(input('digite o produto que deseja comprar: '))
valor = float(input('digite o valor do produto: R$'))
cal_20 = valor + (valor * 0.20)
print('''Nós aceitamos estas formas de pagamento:
[1] à vista dinheiro/cheque: (10%) de desconto
[2] à vista no cartão: (5%) de desconto
[3] em até duas vezes no cartao de credito: valor normal
_3x_ ou mais no cartão: (20%) de juros''')
sleep(2)
forma_pag = int(input('''Digite 1 caso deseje pagar à vista dinheiro/cheque, 2 para a vista no cartão,
3 no cartao de credito: '''))
if forma_pag == 1:
    print(f'À vista no dinheiro/cheque o(a) {produto} fica no valor de R${valor - (valor*0.10)}')
elif forma_pag == 2:
    print(f'À vista no cartão o(a) {produto} sai no valor de R${valor - (valor*0.05)}')
elif forma_pag == 3:
    vezes = int(input('em quantas vezes deseja parcelar o(a) {produto}? '))
    if vezes <= 2:
        print(f'Parcelado no cartao nessas condições o(a) {produto} sai por {vezes}x de R${valor}')
    else:
        print(f'parcelado no cartão nessas condições o(a) {produto} sai por {vezes}x de R${cal_20/vezes :.2f}')

