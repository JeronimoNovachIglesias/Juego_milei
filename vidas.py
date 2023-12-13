import pygame
from lista_vidas import *
from lista_milei import *

class Vidas:
    def __init__(self, x, y) -> None:
        self.imagen_vidas_3 = tres_vidas
        self.imagen_vidas_2 = dos_vidas
        self.imagen_vida_1 = una_vida
        self.imagen_vidas = 3
        print(self.imagen_vidas_2)
        self.rect_vidas_3 = self.imagen_vidas_3.get_rect()
        self.rect_vidas_2 = self.imagen_vidas_2.get_rect()
        self.rect_vidas_1 = self.imagen_vida_1.get_rect()
        self.rect_vidas_3.x = x
        self.rect_vidas_2.x = x
        self.rect_vidas_1.x = x
        self.rect_vidas_3.y = y
        self.rect_vidas_2.y = y
        self.rect_vidas_1.y = y
        self.vidas_visible = True

    def update(self, pantalla, vida_personaje):
        if self.vidas_visible:
            self.draw_vidas(pantalla, vida_personaje)


    def draw_vidas(self, pantalla, vida_personaje):
        # if vida_personaje == 3:
        #     pantalla.blit(self.imagen_vidas_3(self.rect_vidas_3.x, self.rect_vidas_3.y))
        # if vida_personaje == 2:
        #     pantalla.blit(self.imagen_vidas_2,(self.rect_vidas_2.x, self.rect_vidas_2.y)) 
        # if vida_personaje == 1:
        #     pantalla.blit(self.imagen_vida_1,(self.rect_vidas_1.x, self.rect_vidas_1.y)) 
        if self.vidas == 3:
            pantalla.blit(vida_personaje,(self.rect_vidas_3.x, self.rect_vidas_3.y))
        if self.vidas == 2:
            pantalla.blit(vida_personaje,(self.rect_vidas_2.x,self.rect_vidas_2.y))
        if self.vidas == 1:
            pantalla.blit(vida_personaje,(self.rect_vidas_1.x,self.rect_vidas_1.y))

    def vidas_contadas(self):
        if self.colision_con_chori():
            print('choque')
            self.vidas -= 1
        #si impactan contra el personaje, se muestra una menos