import Pygame, sys
Pygame.init()

size = (800, 600)

# Crear ventana
screen = Pygame.display.set_mode(size)

while True:
    for event in Pygame.event.get():
        print(event)
        if event.type == Pygame.QUIT:
            sys.exit()

"""
Curso de pygame 2020: Creando una ventana y estructura de nuestro juego
https://www.youtube.com/watch?v=xjAvXGT5z3E&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM
"""