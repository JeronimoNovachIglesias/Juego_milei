import pygame
from lista_vino import *

class DisparoVino:
    def __init__(self, x, y) -> None:
        self.imagen_vino = copa_de_vino
        self.rect_vino = self.imagen_vino.get_rect()
        self.rect_vino.x = x
        self.rect_vino.y = y
        self.mostrar_vino = True

    def disparo(self):
        self.rect_vino.x -= 10

    def colisiono_personaje(self):
        self.mostrar_vino = False

    def update(self, pantalla):
        self.rect_vino.x -= 25

        # if self.mostrar_vino:
        #     print('vino')
        pantalla.blit(self.imagen_vino, self.rect_vino)