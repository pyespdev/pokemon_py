import pygame, sys
pygame.init()

# Definir colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)

size = (800, 600)

# Crear ventana
screen = pygame.display.set_mode(size)
# Controlar FPS
clock = pygame.time.Clock()
# Coordenadas del cuadrado
cord_x = 400
cord_y = 200

# Velocidad a la que se moverá mi cuadrado
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    ### INICIO -------- LÓGICA            
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 520 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y
    ### FINAL --------- LÓGICA
    # Color de fondo
    screen.fill(WHITE)
    ### INICIO -------- ZONA DE DIBUJO
    """
    pygame.draw.line(screen, GREEN, [0, 100], [0, 100], 5)
    pygame.draw.rect(screen, RED, [100, 100], 80, 80)
    pygame.draw.circle(screen, BLUE, (200,200), 30)
    """
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    ### FINAL --------- ZONA DE DIBUJO
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
    
"""
Curso de pygame 2020: Creando una ventana y estructura de nuestro juego
https://www.youtube.com/watch?v=xjAvXGT5z3E&list=PLuB3bC9rWQAu6cGeRo_I6QV8cz1_2V6uM
"""