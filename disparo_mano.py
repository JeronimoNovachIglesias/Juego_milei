import pygame
from lista_mano import *

class DisparoMano:
    def __init__(self, x, y) -> None:
        self.imagen_mano = mano_k
        self.rect_mano = self.imagen_mano.get_rect()
        self.rect_mano.x = x
        self.rect_mano.y = y
        self.mostrar_mano = True

    def disparo(self):
        self.rect_mano.x -= 10

    def colisiono_personaje(self):
        self.mostrar_mano = False

    def update(self, pantalla):
        self.rect_mano.x -= 30

        # if self.mostrar_vino:
        #     print('vino')
        pantalla.blit(self.imagen_mano, self.rect_mano)