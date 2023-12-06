print('===========================================================')
print('                     EXERCICIO 58                          ')
print('===========================================================')
import emoji
from random import choice
from time import sleep
### Cores
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
### Definindo objetos
guess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
guess2 = choice(guess)
num = 0
soma = 0
sleep(2)
print('+'*70)
print('escolhi um numero... você consegue advinhar qual escolhi?')
print('+'*70)
sleep(2)
### Definindo variaveis e condições
while num != guess2:
    soma+=1
    num = int(input('advinhe o numero que o computador escolheu entre 1 a 10: '))
    pr = 'processando...'
    print(pr)
    sleep(1)
    print('processando..') 
    sleep(1) 
    if num == guess2:
        print(emoji.emojize(f'''parabens, você acertou!:beaming_face_with_smiling_eyes:
voce precisou de {soma} tentativas para acertar'''))
    elif num < guess2:
        print(emoji.emojize(cor_vermelha + 'maior...' + cor_reset + " tente novamente."))
    else:
        print(emoji.emojize(cor_vermelha + 'menor...' + cor_reset + " tente novamente."))

print(cor_reset+'++++++++++++++++++++++++fim+++++++++++++++++++++++++')