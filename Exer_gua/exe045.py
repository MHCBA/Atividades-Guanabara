from time import sleep
import random
import emoji
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
print('===========================================================')
print('                     EXERCICIO 45                          ')
print('===========================================================')
print(f'''jokenpô! escolha entre{cor_verde} pedra{cor_reset}, {cor_vermelha}papel{cor_reset} e {cor_amarela}tesoura{cor_reset}
[1]Pedra vence Tesoura: A pedra quebra a tesoura, então a pedra ganha contra a tesoura. 
[2]Tesoura vence Papel: A tesoura corta o papel, então a tesoura ganha contra o papel. 
[3] Papel vence Pedra: O papel cobre a pedra, então o papel ganha contra a pedra.''')
sleep(2)
jogador_escolha = int(input(f'digite 1 para{cor_verde} pedra{cor_reset}, 2 para {cor_vermelha}papel{cor_reset} e 3 para {cor_amarela}tesoura{cor_reset}: '))
alternativas = ['1, 2, 3']
print('')
print('processando...')
sleep(2)
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
pc_escolha = random.choice(alternativas)
if jogador_escolha == 1:
    if pc_escolha == 1:
        print('você jogou pedra e eu tambem, deu empate!')
    elif pc_escolha == 2:
        print(emoji.emojize('você jogou pedra e eu tesoura, você venceu. :sad_but_relieved_face:'))
    else:
        print('Voce escolheu pedra e eu papel, eu venci! huahuahua')
if jogador_escolha == 2:
    if pc_escolha == 1:
        print('você jogou tesoura e eu pedra, eu venci ahuahuah!')
    elif pc_escolha == 2:
        print("você jogou tesoura e eu tambem, deu empate!")
    else:
        print(emoji.emojize('Voce escolheu tesoura e eu papel, você venceu. :sad_but_relieved_face: '))
if jogador_escolha == 3:
    if pc_escolha == 1:
        print(('você jogou papel e eu pedra, você venceu. :sad_but_relieved_face:'))
    if pc_escolha == 2:
        print('você jogou papel e eu tesoura, eu venci. huahuahua')
    else:
        print('você escolheu papel e eu também! deu empate!')

    

    
