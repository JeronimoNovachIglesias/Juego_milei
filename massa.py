import pygame
from enemigo_1 import Enemigo
from constantes import *
from lista_massa import *
from lista_mano import *
from disparo_vino import *
from constantes import *
from bullrich_2 import *
from pala import *


class Massa():

    def __init__(self, x, y) -> None:
        self.massa = panqueque
        self.vida = 0

        self.rect_massa = self.massa.get_rect()
        self.rect_massa.x = x
        self.rect_massa.y = y
        self.estado = 'activo'
        self.velocidad_massa = 8
        self.visibilidad_massa = True 
        self.colisiono_pala = False

    def update(self, pantalla, lista):
        self.draw(pantalla, panqueque)
        self.vidas()
        self.rect_massa.x -= 2
        if self.colision_con_pala(lista):
            return 0
        if self.vida == 3:
            #print('estoy muerto')
            return 1


    def draw(self, pantalla, lista):

        pantalla.blit(panqueque,(self.rect_massa.x,self.rect_massa.y))

    def movimiento_izquierda(self):
        
        self.rect_massa.x -= self.velocidad_massa

    def colision_con_pala(self, lista):
        for pala in lista:
            if self.rect_massa.colliderect(pala.rect_pala):
                lista.remove(pala)
                #print("colisiono")
                self.vida += 1

    def vidas(self):
        if self.vida == 5:
            self.visibilidad_massa = False
    
