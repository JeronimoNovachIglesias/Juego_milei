import pygame
from lista_pala import *

class Pala:
    def __init__(self, x, y) -> None:
        self.imagen_pala = pala
        self.agarrar = pala_para_agarrar
        self.rect_pala = self.imagen_pala.get_rect()
        self.rect_pala.x = x
        self.rect_pala.y = y
        self.mostrar_pala = True

    def update(self, pantalla):
        if self.mostrar_pala:
            self.draw(pantalla)
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    print("me muevo a la izq")
                    self.movimiento()

    def draw(self, pantalla):
        agarrar = self.agarrar
        self.fotograma = 0
        pantalla.blit(agarrar,(self.rect_pala.x,self.rect_pala.y))

    def movimiento(self):
        self.rect_pala.x -= 15
