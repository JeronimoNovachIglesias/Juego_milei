from pala import *
import random
from botin import *
from personaje_mileiiii import *

class Enemigo:
    def __init__(self, x, y,lista_img,vidas) -> None:
        self.vigila = lista_img
        self.vida = vidas
        self.fotograma = 0

        self.rect_enemigo = self.vigila[0].get_rect()
        self.rect_enemigo.x = x
        self.rect_enemigo.y = y
        self.velocidad_enemigo = 8
        self.estado = 'activo'
        self.velocidad_disparo = random.randint(500, 2000)
        self.murio = False


    def update(self, pantalla, lista, jugador:Milei):
        self.draw(pantalla)
        self.colision_con_pala(lista, jugador)
        self.rect_enemigo.x -= self.velocidad_enemigo
        if len(lista) > 0:
            self.colision_con_pala(lista, jugador)
            self.murio = False
        
        if self.vida == 0:
            
            self.murio = True

    def draw(self, pantalla):
        largo = len(self.vigila)
        if self.fotograma >= largo:
            self.fotograma = 0
        pantalla.blit(self.vigila[self.fotograma],(self.rect_enemigo.x,self.rect_enemigo.y))
        self.fotograma += 1

    def colision_con_pala(self, lista, jugador:Milei):
        for pala in lista:
            if self.rect_enemigo.colliderect(pala.rect_pala):
                
                lista.remove(pala)
                
                self.vida -= 1
                jugador.score += 10
                print(jugador.score)