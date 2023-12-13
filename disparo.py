import pygame
from constantes import *
from lista_milei import *
from lista_pala import *
from pala import *

import pygame
from lista_pala import *


class Disparo:
    def __init__(self, x, y) -> None:
        self.imagen_pala = pala
        self.agarrar = pala_para_agarrar
        self.rect_pala = self.imagen_pala.get_rect()
        self.rect_pala.x = x
        self.rect_pala.y = y
        self.desaparecion = True
        
    def disparo(self):
        self.rect_pala.x += 10
    
    def update(self, pantalla):
        self.rect_pala.x += 25
        pantalla.blit(self.imagen_pala, self.rect_pala)

    #def colision_de_pala():
