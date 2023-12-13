import sqlite3

class Score:
    def __init__(self, nombre, tiempo, puntuación):
        self.nombre = nombre
        self.tiempo = tiempo
        self.puntuación = puntuación
    
    score = []

    def actualizar_score():
        score = Score("Juan", 100, 100)

        # Actualizar el score
        score.actualizar_score(10)

        print(score.puntuación)

    def mostrar_score(fuente, posicion_pantalla):
        score = Score("Juan", 100, 100)
        # Mostrar el score
        score.mostrar(fuente, (10, 10))
    
    def guardar_score(scores):
        score = Score("Juan", 100, 100)
        # Guardar los scores
        score.guardar("scores.txt")

    def cargar_score(scores):
        score = Score("", 0, 0)
        # Cargar los scores
        score.cargar("scores.txt")

        print(score.nombre)
        print(score.tiempo)
        print(score.puntuación)