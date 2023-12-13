import pygame
from enemigo_1 import Enemigo
from constantes import *
from lista_Bullrich import *
from lista_vino import *
from disparo_vino import *
from constantes import *
from pala import *


class BullrichCopia(Enemigo):

    def __init__(self, x, y, lista_img,vidas) :
        super().__init__(x, y, lista_img,vidas)
        
    
