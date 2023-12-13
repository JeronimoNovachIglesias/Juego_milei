import pygame 


if acumulador_fondo >= 4000 and acumulador_fondo <= 8000:
        zurdo_bandera = False

        pantalla.blit(imagen_fondo2, fondo_rectangulo2)
        bullrich_enemigo.update(pantalla, lista_palas)

        
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



    if acumulador_fondo >= 8000 and acumulador_fondo <= 12000:
        pantalla.blit(imagen_fondo2, fondo_rectangulo2)
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
