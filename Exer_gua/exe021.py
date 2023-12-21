print('===========================================================')
print('                     EXERCICIO 21                          ')
print('===========================================================')
import pygame
pygame.init()
pygame.mixer.music.load(r'Exer_Guanabara_py/exe021.mp3')
pygame.mixer.music.play()
pygame.time.delay(2 * 60 * 1000 + 35 * 1000)  # Delay for 2 minutes and 35 seconds

pygame.event.wait()