import pygame
pygame.init()
BASIC_FONT = pygame.font.SysFont(None, 48)
BLACK = (0, 0, 0)
GREY = (122, 122, 122)
WHITE = (255, 255, 255)
WIDTH = 1200
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SPIN_PONG')
FPS = 60
left_score = 0
right_score = 0

class Moving_object:

    def invert_velocity(velocity):
        return velocity * -1


class Ball(Moving_object):

    #y_velocity = random
    #x_velocity = random

    def __init__(self):
        #make Ball image
        pass

    def detect_collision(self):
        pass


class Bat(Moving_object):

    velocity = 1

    def __init__(self):
        #make Bat image
        #move in random direction
        pass


def draw_WIN():
    WIN.fill(BLACK)
    #draw playingfield
    #draw bats
    #draw ball
    #draw score
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_WIN()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == '__main__':
    main()