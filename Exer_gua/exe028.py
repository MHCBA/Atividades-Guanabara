print('===========================================================')
print('                     EXERCICIO 28                          ')
print('===========================================================')
import emoji
from random import choice
from time import sleep
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
guess = [1, 2, 3, 4, 5]
guess2 = choice(guess)
print('+'*70)
print('escolhendo um numero... você consegue advinhar qual escolhi?')
print('+'*70)
num = int(input('advinhe o numero que o computador escolheu entre 1 a 5: '))
pr = 'processando...'
print(pr)
sleep(1)
print('processando..') 
sleep(1) 
print('processando.')
sleep(1)
print('processando')
sleep(1)
if num == guess2:
    print(emoji.emojize('parabens, você acertou!:beaming_face_with_smiling_eyes:'))
else:
    print(emoji.emojize(cor_vermelha+'você errou! :sad_but_relieved_face:'))
print(cor_reset+'+++++++++++fim+++++++++++++')