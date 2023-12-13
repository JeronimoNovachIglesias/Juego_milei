import pygame
from lista_chori import *

class DisparoChori:
    def __init__(self, x, y) -> None:
        self.imagen_chori = chori
        self.rect_chori = self.imagen_chori.get_rect()
        self.rect_chori.x = x
        self.rect_chori.y = y
        self.mostrar_chori = True

    def disparo(self):
        self.rect_chori.x -= 10
    
    def colisiono_personaje(self):
        self.mostrar_chori = False

    def update(self, pantalla):
        self.rect_chori.x -= 25
        
        if self.mostrar_chori:
            pantalla.blit(self.imagen_chori, self.rect_chori)