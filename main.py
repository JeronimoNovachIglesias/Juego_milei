import pygame
import sys
from base_datos import guardar_datos, obtener_datos
from constantes import *
from personaje_mileiiii import Milei
from lista_milei import *
from lista_pala import *
from vidas import *
from pala import *
from botin import *
from disparo import *
from bullrich_2 import *
from lista_Bullrich import *
from lista_vino import *
from disparo_vino import *
from enemigo_1 import *
from lista_enemigos import *
from random import *
from disparo_chori import *
from modo import *
from massa import *
from disparo_mano import *
from lista_mano import *

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.init()
reloj = pygame.time.Clock()

#--------------------------------------------------------------------



#---------------------------------- Fondos --------------------------------
imagen_fondo = pygame.image.load('fondo_2.jpg')
imagen_fondo = pygame.transform.scale_by(imagen_fondo, 3.6)

imagen_fondo2 = pygame.image.load('imagen_3.jpg')
imagen_fondo2 = pygame.transform.scale_by(imagen_fondo2, 3.6)

imagen_fondo3 = pygame.image.load('fondo_3.jpg')
imagen_fondo3 = pygame.transform.scale_by(imagen_fondo3, 4.8)

fondo_rectangulo2 = imagen_fondo2.get_rect()
fondo_rect = imagen_fondo.get_rect()
fondo_rect3 = imagen_fondo3.get_rect()

acumulador_fondo = 0
acumulador_fondo2 = 0
acumulador_fondo3 = 0

#---------------------------------- Objetos --------------------------------
disparo = False
disparo_enemigo = False
disparo_bullrich = False
jugador_1 = Milei(50,610)
objeto_dolar = Dolar(1300,670)
objeto_pala = Pala(300, 650)
objeto_vidas = Vidas(900, 25)
bullrich_enemigo = BullrichCopia(1000, 610, caminata_izquierda_bullrich, 3)
zurdito = Enemigo(1000, 580,enemigo_caminando,1)
massa_enemigo = Massa(1700,580)
#---------------------------------- Lista Objetos --------------------------------
lista_zurdito = [zurdito]
lista_bullrich = [bullrich_enemigo]
lista_massa = [massa_enemigo]
lista_palas = [objeto_pala]
lista_vidas = [objeto_vidas]
lista_moneda = [objeto_dolar]
lista_disparos = []
lista_disparos_enemigos = []
lista_disparos_vinos = []
lista_pj = [jugador_1]
lista_disparos_manos = []

#---------------------------------- Sonidos --------------------------------
sonido_leon =  pygame.mixer.Sound('soy_el_leon.mp3')
sonido_leon.set_volume(0.1)

sonido_milei = pygame.mixer.Sound('libertad.mp3')
sonido_milei.set_volume(0.5)

sonido_bullrich = pygame.mixer.Sound('audio bullrich.mp3')
sonido_bullrich.set_volume(1.0)

sonido_massa = pygame.mixer.Sound('javier.mp3')
sonido_massa.set_volume(1.0)

bandera_sonido = True
bandera2 = True

#---------------------------------- Tiempo de disparo enemigo --------------------------------
tiempo_disparo_enemigo = pygame.USEREVENT
pygame.time.set_timer(tiempo_disparo_enemigo, 2000)

tiempo_disparo_bullrich = pygame.USEREVENT
pygame.time.set_timer(tiempo_disparo_bullrich, 2000)

tiempo_disparo_massa = pygame.USEREVENT
pygame.time.set_timer(tiempo_disparo_massa, 500)

#---------------------------------- Tiempo de disparo Milei --------------------------------
tiempo_disparo = pygame.time.get_ticks()


#---------------------------------- Textos --------------------------------
fuente = pygame.font.SysFont('Times New Roman', 120)
texto = fuente.render("Nivel Uno", True, (0,0,0))
texto2 = fuente.render("Nivel Dos", True, (0,0,0))
texto3 = fuente.render("Nivel Tres", True, (0,0,0))
fuente_volver = pygame.font.SysFont('Times New Roman', 60)
texto_volver = fuente_volver.render("Volver", True, (0,0,0))
 
texto_anuncio = fuente_volver.render("Este juego no tiene el fin de hacer campaña, simplemente de reirse", True, (0,0,0))

font_input = pygame.font.SysFont("Arial", 50)

ingreso = ""
ingreso_rect = pygame.Rect(200,400,300,80)
enter = False
#---------------------
bandera = True

esta_jugando = False
#---------------------------------- Bandera de creacion de zurdos --------------------------------
zurdo_bandera = True
bullrich_bandera = True
massa_bandera = True
#---------------------------------- Contador de zurdos --------------------------------
enemigos_muertos = 0
ver_puntos = False


while True:

    if esta_jugando == False:
        pantalla.fill(COLOR_ROJO)
        rectangulo_1 = pygame.draw.rect(pantalla, COLOR_BLANCO, (100,40,200,100))
        rectangulo_2 = pygame.draw.rect(pantalla, COLOR_BLANCO, (500,40,400,100))
        fuente = pygame.font.SysFont("Arial",50)
        texto_1 = fuente.render("JUGAR",True,COLOR_CELESTE)
        texto_puntos = fuente.render("VER PUNTOS",True,COLOR_CELESTE)
        pantalla.blit(texto_anuncio,(100,700))
        rect_fuente1 = texto_1.get_rect()
        rect_fuente = texto_puntos.get_rect()
        rect_fuente1.center = (200,100)
        rect_fuente.center = (700, 100)
        resultado = ""

        lista_evento = pygame.event.get()
        for evento in lista_evento:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rectangulo_1.collidepoint(evento.pos):
                    # print('toco boton')
                    esta_jugando = True
                if rectangulo_2.collidepoint(evento.pos):
                    ver_puntos = True
                    # print("ve puntos")
                    # esta_jugando = False




        if ver_puntos == True:
            lista_datos = obtener_datos() 
            for dato in lista_datos:
                resultado += f"Nombre: {dato['nombre']} --- Puntaje: {dato['puntos']} || "

            # print(lista_datos)

        texto_puntaje = fuente.render(resultado,True,COLOR_CELESTE)

        pantalla.blit(texto_puntaje,(100,400))
        pantalla.blit(texto_1,rect_fuente1)
        pantalla.blit(texto_puntos, rect_fuente)

    if esta_jugando == True:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        bandera_sonido = False
        if bandera_sonido == False and bandera2 == True:
            sonido_leon.play()
            
#---------------------------------- Creacion aleatoria de enemigo y su disparo --------------------------------
        if evento.type == tiempo_disparo_enemigo:
            contador_enemigos = 0
            if len(lista_zurdito) != 0 and zurdo_bandera == True:
                if len(lista_zurdito) == 0 or len(lista_zurdito) == 1:
                    x_enemigo = randint(1800, 2000)
                    enemigo_2 = Enemigo(x_enemigo, 580,enemigo_caminando,1)
                    lista_zurdito.append(enemigo_2)

                if tiempo_disparo_enemigo:
                    if len(lista_disparos_enemigos) == 0 or len(lista_disparos_enemigos) <= 1:
                        disparo_enemigo = DisparoChori(lista_zurdito[0].rect_enemigo.x, lista_zurdito[0].rect_enemigo.y)
                        lista_disparos_enemigos.append(disparo_enemigo)
            else:
                # print('pasaste de nivel')
                pass
##---------------------------------- Eventos de cierre del juego --------------------------------
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.K_ESCAPE:
            sys.exit()
            pygame.quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print("Texto ingresado:", ingreso)
                enter = True
            elif evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]  # Método slice
            else:
                ingreso += evento.unicode  # Da el texto que se presiona en el teclado
                print("cargando datos")
            #pantalla.fill(COLOR_ROJO)

        lista_teclas = pygame.key.get_pressed()
        #lista_evento = pygame.event.get()


#---------------------------------- Condicion de disparo del jugador --------------------------------
        if lista_teclas[pygame.K_x]:
            if bandera == True:
                disparo = Disparo(jugador_1.rect.x, jugador_1.rect.y)
                lista_disparos.append(disparo)
                tiempo_disparo = pygame.time.get_ticks()
                bandera = False


#---------------------------------- Lapso de tiempo de disparo del jugador --------------------------------
        if tiempo_disparo + 200 < pygame.time.get_ticks():
            bandera = True

#---------------------------------- Banderas para eliminar el objeto una vez que colisiona --------------------------------
        for palita in lista_palas:
            if jugador_1.colisiono_pala:
                palita.mostrar_pala = False

        # for vidita in lista_vidas:
        #     if jugador_1.colision_con_chori or jugador_1.colision_con_zurdo:
        #         vidita.vidas_visible = False
        #         lista_vidas.remove(vidita)

        for dolarito in lista_moneda:
            if jugador_1.colisiono_dolar:
                dolarito.dolar_visible = False

        for disparo in lista_disparos:
            for chori in lista_disparos_enemigos:
                if disparo.rect_pala.colliderect(chori.rect_chori):
                    lista_disparos_enemigos.remove(chori)
                    lista_disparos.remove(disparo)

                    #print('colisionaron los choris y la pala')

#---------------------------------- Banderas para el sonido --------------------------------
        if jugador_1.colisiono_pala == True:
            bandera_sonido = False
            jugador_1.colisiono_pala = False
            #print("sonido")

        if bandera_sonido == False and bandera2 == True:
            sonido_milei.play()
            bandera2 = False
            bandera_sonido = True


#---------------------------------- NIVELES --------------------------------


#---------------------------------- Nivel 1 --------------------------------
        if acumulador_fondo <= 4000:
            pantalla.blit(imagen_fondo, fondo_rect)
            pantalla.blit(texto_volver,(150,50))
            if acumulador_fondo >= 0 and acumulador_fondo <= 2000:
                #print("texto")
                pantalla.blit(texto,(800, 200))

            #print(acumulador_fondo)


            if lista_teclas[pygame.K_RIGHT]:
                jugador_1.estado = "derecha"
                objeto_dolar.movimiento()
                objeto_pala.movimiento()
                fondo_rect.x -= 15
                acumulador_fondo += 15
                #print(f"Acumulado de fondo: {fondo_rect.x}")
    #---------------------------------- Si no se mueve, el estado del jugador pasa a estar quieto --------------------------------
            else:
                jugador_1.estado = "quieto"

#---------------------------------- Nivel 2 --------------------------------
        if acumulador_fondo >= 4000 and acumulador_fondo <= 4015:
            sonido_bullrich.play()
            #print('sonido')

        if acumulador_fondo >= 4000 and acumulador_fondo <= 8000:
            pantalla.blit(imagen_fondo2, fondo_rectangulo2)
            
            if evento.type == tiempo_disparo_bullrich:
                #print('bullrich')
                contador_enemigos = 0
                if len(lista_bullrich) != 0 and bullrich_bandera == True:
                    if enemigos_muertos == 1 or len(lista_bullrich) <= 5:
                        x_enemigo = randint(1800, 2000)
                        enemigo_2 = BullrichCopia(x_enemigo, 610,caminata_izquierda_bullrich,3)
                        lista_bullrich.append(enemigo_2)
                    if tiempo_disparo_bullrich:
                        if len(lista_disparos_vinos) == 0 and len(lista_disparos_vinos) <= 1:
                            disparo_bullrich = DisparoVino(lista_bullrich[0].rect_enemigo.x, lista_bullrich[0].rect_enemigo.y)
                            lista_disparos_vinos.append(disparo_bullrich)
                else:
                    #print('pasaste de nivel')
                    pass

            for bullrich in lista_bullrich:
                bullrich.update(pantalla, lista_disparos, jugador_1)

                if bullrich.murio == True:
                    lista_bullrich.pop(0)
                    enemigos_muertos += 1
                    #print(f'mate')


            if acumulador_fondo >= 4000 and acumulador_fondo <= 6000:

                pantalla.blit(texto2,(800, 200))

            if lista_teclas[pygame.K_RIGHT]:
                jugador_1.estado = "derecha"
                objeto_dolar.movimiento()
                objeto_pala.movimiento()
                fondo_rectangulo2.x -= 15
                acumulador_fondo += 15

            elif lista_teclas[pygame.K_x]:
                if bandera == True:
                    disparo = Disparo(jugador_1.rect.x, jugador_1.rect.y)
                    lista_disparos.append(disparo)
                    tiempo_disparo = pygame.time.get_ticks()
                    bandera = False
            else:
                jugador_1.estado = "quieto"

            for disparo in lista_disparos:
                for vino in lista_disparos_vinos:
                    if disparo.rect_pala.colliderect(vino.rect_vino):
                        lista_disparos_vinos.remove(vino)
                        lista_disparos.remove(disparo)
        
    #---------------------------------- Nivel 3 --------------------------------
        if acumulador_fondo >= 8000 and acumulador_fondo <= 8015:
            sonido_massa.play()
            #print('sonido')
        if acumulador_fondo >= 8000 and acumulador_fondo <= 12000:

            pantalla.blit(imagen_fondo3, fondo_rect3)

            if evento.type == tiempo_disparo_massa:
                contador_enemigos = 0
                if len(lista_disparos_manos) == 0 and len(lista_disparos_manos) <= 2:
                    disparo_massa = DisparoMano(massa_enemigo.rect_massa.x, massa_enemigo.rect_massa.y)
                    lista_disparos_manos.append(disparo_massa)
                    #print("dispara massa")
                else:
                    #print('pasaste de nivel')
                    pass
            for massi in lista_massa:
                massi.update(pantalla, lista_disparos)

                if massi.visibilidad_massa == True:
                    lista_massa.pop(0)
                    enemigos_muertos += 1
                    #print(f'mate')


            if acumulador_fondo >= 8000 and acumulador_fondo <= 10000:

                pantalla.blit(texto3,(800, 200))

            if lista_teclas[pygame.K_RIGHT]:
                jugador_1.estado = "derecha"
                objeto_dolar.movimiento()
                objeto_pala.movimiento()
                fondo_rect3.x -= 15
                acumulador_fondo += 15

            elif lista_teclas[pygame.K_x]:
                if bandera == True:
                    disparo = Disparo(jugador_1.rect.x, jugador_1.rect.y)
                    lista_disparos.append(disparo)
                    tiempo_disparo = pygame.time.get_ticks()
                    bandera = False
            else:
                jugador_1.estado = "quieto"

            for disparo in lista_disparos:
                for mano in lista_disparos_manos:
                    if disparo.rect_pala.colliderect(mano.rect_mano):
                        lista_disparos_manos.remove(mano)
                        lista_disparos.remove(disparo)


    #---------------------------------- Verifico de que mata enemigos y los borra de la lista --------------------------------
        if zurdo_bandera == True:
            for zurdo in lista_zurdito:
                zurdo.update(pantalla, lista_disparos, jugador_1)
                if zurdo.murio == True:
                    lista_zurdito.remove(zurdo)
                    enemigos_muertos += 1
                    #print(f'mate')



    #---------------------------------- Actualizo los objetos --------------------------------

        objeto_pala.update(pantalla)
        jugador_1.update(objeto_pala, objeto_dolar,lista_disparos_enemigos,lista_zurdito, lista_disparos_vinos, lista_bullrich, lista_disparos_manos, lista_massa, pantalla,  objeto_vidas)
        objeto_dolar.update(pantalla)
        
        texto_vidas = fuente.render(f"vidas: {jugador_1.vida}", True, (COLOR_GRIS))
        texto_score = fuente.render(f"DOLARES: {jugador_1.score}", True, (COLOR_GRIS))
        pantalla.blit(texto_score, (600, 25))
        pantalla.blit(texto_vidas,(900, 25))

    #---------------------------------- FIN DEL JUEGO Y CARGA DE SUS DATOS --------------------------------

        if jugador_1.vida <= 0 or massa_enemigo.visibilidad_massa == False:
            if jugador_1.vida <= 0:
                texto_fin = fuente.render("GAME OVER", True, (COLOR_ROJO))
            if massa_enemigo.visibilidad_massa == False:
                texto_fin = fuente.render("GANASTE", True, (COLOR_ROJO))
            #pantalla.blit(imagen_fondo3, fondo_rect3)
            
            #MOSTRAR FONDO CON LA TABLA DE PUNTAJE
            pantalla.blit(texto_fin,(900, 400))
            #bandera2 = False

            pygame.draw.rect(pantalla, COLOR_BLANCO, ingreso_rect, 2)
            font_input_surface = font_input.render(ingreso, True, COLOR_ROJO)
            pantalla.blit(font_input_surface, (ingreso_rect.x + 5, ingreso_rect.y + 5))
            texto_ingreso = fuente.render("Ingrese su nombre", True, (COLOR_ROJO))
            pantalla.blit(texto_ingreso,(ingreso_rect.x + 5, ingreso_rect.y - 100))
            #print(ingreso)

            if enter == True:
                #print("enter")
                guardar_datos(ingreso, jugador_1.score)
                enter = False
                ingreso = ""

        for mano in lista_disparos_manos:
            mano.update(pantalla)

        for vino in lista_disparos_vinos:
            vino.update(pantalla)

        for chori in lista_disparos_enemigos:
            chori.update(pantalla)

        for disparo in lista_disparos:
            disparo.update(pantalla)


        def dibujar_rectangulos():
            if obtener_modo():
                pygame.draw.rect(pantalla,COLOR_ROJO,jugador_1.rect,2)
                pygame.draw.rect(pantalla,COLOR_ROJO,bullrich_enemigo.rect_enemigo,2)


        dibujar_rectangulos()

    reloj.tick(22)
    pygame.display.flip()