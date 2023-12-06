from time import sleep
import emoji
print('===========================================================')
print('                     EXERCICIO 29'                          )
print('===========================================================')
cor_azul = "\033[94m"
vel = int(input('Quantos km/h você está dirigindo? '))
cor_vermelha = "\033[91m"
cor_reset = "\033[0m"
limite = 80
calculo = vel-limite
print(emoji.emojize('        :vertical_traffic_light:'))
print('________________________________')
print(emoji.emojize('---------:racing_car: ---------------------'))
print('________________________________')
print('')
sleep(1)
print('processando...')
sleep(3)
print('')
if vel >limite:
    print(emoji.emojize(cor_vermelha+':disappointed_face: vai ter que pagar multa!'))
    print(cor_vermelha+'A multa ficou em: {} R$ \n '
          'o limite de velocidade dessa rodovia é de 80km/h'.format(calculo*7))
else:
    print(emoji.emojize(cor_azul+'ufa!:grinning_face_with_sweat: dessa vez você passou! \n'
    'o limite de velocidade dessa rodovia é de 80km/h'))
print('')
print(cor_reset+'________________________________fim__________________________________')
