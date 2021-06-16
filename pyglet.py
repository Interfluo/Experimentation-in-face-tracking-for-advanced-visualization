import pygame
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import stl_import

'''
# cube
verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))

# triangular Pyramid
verticies = ((-1, -1, -1), (1, -1, -1), (0, 1, 0), (0, -1, 1))
edges = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

# square Pyramid
verticies = [(1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1), (-1, 0, 0)]
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)]

# more shapes...
'''
file_name = "dat/simple.STL"
verticies, edges = stl_import.stl_verticies_edges(file_name)



def shape():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-1, -1, -15)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glTranslatef(0.1*cos(counter/100), 0.1*sin(counter/100), 0)

        pitch_rate = 3  # tan(counter/100)
        yaw_rate = 3    # 10*sin(counter/100)
        roll_rate = 3   # 5*pi*cos(counter/100)
        glRotatef(pitch_rate, 1, 0, 0)
        glRotatef(yaw_rate, 0, 1, 0)
        glRotatef(roll_rate, 0, 0, 1)

        counter += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        shape()
        pygame.display.flip()
        pygame.time.wait(1)


main()
