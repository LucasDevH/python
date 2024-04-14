import pygame
pygame.init()
pygame.mixer.music.load('js.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()  