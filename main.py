from labirinthe import Lab
import pygame
from perso import Perso
from graph import dysplay

class game(object):
    def __init__ (self):
        self.Map = Lab()
        self.player = Perso(self.Map.mcgiver)
        self.graphisme= dysplay()
        pygame.init()

        display_width = 800
        display_height = 600

        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('A bit Racey')

        clock = pygame.time.Clock()
        crashed = False
        carImg = pygame.image.load('racecar.png')
    def wininggame (self):
        return false

    # def dysplay(self):

    def instance (self):
        pygame.init()

        display_width = 800
        display_height = 600

        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('A bit Racey')

        clock = pygame.time.Clock()
        crashed = False
        carImg = pygame.image.load('racecar.png')

        for i in range(self.Map.size):
            for j in range(self.Map.size):
                gameDisplay.blit(self.Map.floor, (x,y))


        x = (display_width * 0.45)
        y = (display_height * 0.8)

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            gameDisplay.fill(white)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()


game = game()
game.instance()


