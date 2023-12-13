import pygame
from constantes import *
from lista_Bullrich import *
from lista_vino import *
from disparo_vino import *
from constantes import *
from pala import *

class Bullrich:

    def __init__(self, x, y) -> None:
        self.caminar = caminata_derecha_bullrich
        self.caminar_izquierda = caminata_izquierda_bullrich
        self.score = 0
        self.vida = 0
        self.fotograma = 0

        self.rect_bullrich = self.caminar[0].get_rect()
        self.rect_bullrich.x = x
        self.rect_bullrich.y = y
        self.estado = 'activo'
        self.velocidad_bullrich = 8
        self.visibilidad_bullrich = True 
        self.colisiono_pala = False

    def update(self, pantalla, lista):
        #self.colision_con_pala(pala)
        # self.vidas()
        self.draw(pantalla, caminata_izquierda_bullrich)
        # if self.estado == 'activo':
        #     if self.rect_bullrich.x > 1300:
        #         self.movimiento_izquierda() 
        self.rect_bullrich.x -= 2

        if self.colision_con_pala(lista):
            return 0
        if self.vida == 3:
            #print('estoy muerto')
            return 1
        if self.rect_bullrich.x > ANCHO_VENTANA:
            self.rect_bullrich.x = ANCHO_VENTANA
        if self.rect_bullrich.x < 0:
            self.rect_bullrich.x = 0


    def draw(self, pantalla, lista_movimientos):
        largo = len(lista_movimientos)
        if self.fotograma >= largo:
              self.fotograma = 0
        pantalla.blit(lista_movimientos[self.fotograma],(self.rect_bullrich.x,self.rect_bullrich.y))
        self.fotograma += 1

    # def movimiento_derecha(self):
    #     if self.visibilidad_bullrich:
    #         self.rect_bullrich.x += self.velocidad_bullrich

    def movimiento_izquierda(self):
        self.caminar_izquierda
        self.rect_bullrich.x -= self.velocidad_bullrich

    def colision_con_pala(self, lista):
        for pala in lista:
            if self.rect_bullrich.colliderect(pala.rect_pala):
                lista.remove(pala)
                #print("colisiono")
                self.vida += 1

    def vidas(self):
        if self.vida == 3:
            self.visibilidad_bullrich = False