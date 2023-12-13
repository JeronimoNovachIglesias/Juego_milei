import pygame
from lista_dolar import *

class Dolar:
    def __init__(self, x, y) -> None:
        self.dolar = dolar_simple
        self.dolar_boss = dolar_boss
        self.fotograma = 0

        self.rect_dolar = self.dolar.get_rect()
        self.rect_dolar.x = x
        self.rect_dolar.y = y
        self.dolar_visible = True

    def update(self, pantalla):
        if self.dolar_visible:
            self.draw(pantalla)
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    #print("me muevo a la izq")
                    self.movimiento()

                    
        #self.movimiento()
        #self.crear_rectangulo()

    def draw(self, pantalla):
        dolar = self.dolar
        self.fotograma = 0
        pantalla.blit(dolar,(self.rect_dolar.x,self.rect_dolar.y))

    def movimiento(self):
        self.rect_dolar.x -= 15
