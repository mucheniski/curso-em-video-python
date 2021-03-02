# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()

# No caso precisa existir um arquivo mp3 com o path informado dentro do load
pygame.mixer.music.load('nomeDoMp3.mp3')
pygame.mixer.music.play()

# Serve para esperar o evento terminar
pygame.event.wait()