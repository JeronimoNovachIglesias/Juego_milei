import pygame
from constantes import *
from lista_milei import *
from lista_pala import *
from lista_dolar import *
from pala import *
from botin import *
from disparo import *
from disparo_chori import *
from lista_vidas import *
from vidas import *
from disparo_vino import *

pygame.mixer.init()
pygame.mixer_music.set_volume(0.7)
sonido_milei = pygame.mixer.Sound('audio.mp3')
sonido_milei.set_volume(0.5)



class Milei:
    def __init__(self, x, y) -> None:
        self.caminar = caminar_derecha
        self.nada = caminar_quieto
        self.caminar_con_pala = caminar_derecha_con_pala
        self.nada_con_pala = caminar_quieto_con_pala
        self.rect_con_pala = self.caminar_con_pala[0].get_rect()
        self.rect_con_pala.x = x 
        self.rect_con_pala.y = y 
        self.score = 0
        self.vida = 3
        self.fotograma = 0


        self.rect = self.caminar[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.estado = 'quieto'
        self.salto = 10
        self.velocidad_caminata = 9
        self.colisiono_pala = False 
        self.colisiono_dolar = False




        #vidas
        # self.yvidas = 25
        # self.xvidas = 900
        # self.imagen_vidas_3 = tres_vidas
        # self.imagen_vidas_2 = dos_vidas
        # self.imagen_vida_1 = una_vida
        # self.imagen_vidas = 3
        # print(self.imagen_vidas_2)
        # self.rect_vidas_3 = self.imagen_vidas_3.get_rect()
        # self.rect_vidas_2 = self.imagen_vidas_2.get_rect()
        # self.rect_vidas_1 = self.imagen_vida_1.get_rect()
        # self.rect_vidas_3.x = self.xvidas
        # self.rect_vidas_2.x = self.xvidas
        # self.rect_vidas_1.x = self.xvidas
        # self.rect_vidas_3.y = self.yvidas
        # self.rect_vidas_2.y = self.yvidas
        # self.rect_vidas_1.y = self.yvidas
        # self.vidas_visible = True


    def update(self, pala, dolar,lista_choris, lista_zurdos,lista_vino, lista_bullrich, lista_mano, lista_massa, pantalla,  vida_personaje):

        self.colision_con_pala(pala)
        self.colision_con_coin(dolar)
        self.colision_con_chori(lista_choris, pantalla)
        self.colision_con_zurdo(lista_zurdos, pantalla)
        self.colision_con_vino(lista_vino, pantalla)
        self.colision_con_bullrich(lista_bullrich, pantalla)
        self.colision_con_mano(lista_mano, pantalla)
        self.colision_con_massa(lista_massa, pantalla)

        ##self.draw_vidas(pantalla)       
        if self.estado == 'derecha':
            if self.colisiono_pala:
                self.draw(pantalla, self.caminar_con_pala)
            else:
                self.draw(pantalla, self.caminar)
            self.movimiento()
            
        elif self.estado == 'quieto':
            if self.colisiono_pala:
                self.draw(pantalla, self.nada_con_pala)
            else:
                self.draw(pantalla, self.nada)

        if vida_personaje == 2:
            pantalla.blit(self.imagen_vidas_2,(self.rect_vidas_2.x, self.rect_vidas_2.y)) 
        if vida_personaje == 1:
            pantalla.blit(self.imagen_vida_1,(self.rect_vidas_1.x, self.rect_vidas_1.y))  
        if self.vida == 0:
            #print('estoy muerto')
            return 1
            
        #self.crear_rectangulo()

    def draw(self, pantalla, lista_movimientos):
        largo = len(lista_movimientos)
        if self.fotograma >= largo:
              self.fotograma = 0
        pantalla.blit(lista_movimientos[self.fotograma],(self.rect.x,self.rect.y))
        self.fotograma += 1

    def movimiento(self):
        lista_teclas = pygame.key.get_pressed()
        
        if lista_teclas[pygame.K_RIGHT]:
            #self.rect.x += self.velocidad_caminata
            if self.rect.x >= ANCHO_VENTANA:
                self.rect.x = 0

    def colision_con_pala(self, pala):
        # print(pala)
        if self.rect.colliderect(pala.rect_pala):
            self.colisiono_pala = True
            
            # print("colisionaron milei y la pala")

    def colision_con_coin(self, dolar):
        # print(dolar)
        if self.rect.colliderect(dolar.rect_dolar) and self.colisiono_dolar == False:
            self.colisiono_dolar = True
            self.score += 5
            
            print(self.score)
            # print("colisionaron milei y dolar")

    def colision_con_chori(self, lista_choris, pantalla):
        for chori in lista_choris:
            if self.rect_con_pala.colliderect(chori.rect_chori):
                lista_choris.remove(chori)

            if self.rect.colliderect(chori.rect_chori):
                chori.colisiono_personaje()
                if self.vida >= 1:
                    print("hola")
                    self.vida -= 1
                #self.draw_vidas(pantalla)

    def colision_con_zurdo(self,lista_zurdos, pantalla):
        for zurdito in lista_zurdos:
            if self.rect.colliderect(zurdito.rect_enemigo):
                if self.vida >= 1:
                    self.vida -= 1
                    print("chau")
                    lista_zurdos.remove(zurdito)
                #self.draw_vidas(pantalla)
    


# def draw_vidas(self, pantalla):
    ##pantalla.blit(self.imagen_vidas_3,(self.rect_vidas_3.x, self.rect_vidas_3.y))
    def colision_con_bullrich(self,lista_bullrich, pantalla):
        for bullrich in lista_bullrich:
            if self.rect.colliderect(bullrich.rect_enemigo):
                if self.vida >= 1:
                    self.vida -= 1
                    print("chau")
                    lista_bullrich.remove(bullrich)


    def colision_con_vino(self,lista_vino, pantalla):
        for vino in lista_vino:
            if self.rect_con_pala.colliderect(vino.rect_vino):
                lista_vino.remove(vino)

            if self.rect.colliderect(vino.rect_vino):
                vino.colisiono_personaje()
                if self.vida >= 1:
                    print("hola")
                    self.vida -= 1

    def colision_con_massa(self,lista_massa, pantalla):
        for massita in lista_massa:
            if self.rect.colliderect(massita.rect_massa):
                if self.vida >= 1:
                    self.vida -= 1
                    print("chau")
                    lista_massa.remove(massita)


    def colision_con_mano(self,lista_mano, pantalla):
        for mano in lista_mano:
            if self.rect_con_pala.colliderect(mano.rect_mano):
                lista_mano.remove(mano)

            if self.rect.colliderect(mano.rect_mano):
                mano.colisiono_personaje()
                if self.vida >= 1:
                    print("hola")
                    self.vida -= 1
                #self.draw_vidas(pantalla)