from labirinthe import Lab
import pygame
from perso import Perso
from graph import dysplay

class game(object):
    def __init__ (self):
        self.Map = Lab()
        self.player = Perso(self.Map.mcgiver)
    def wininggame (self):
        return false

    def dysplay(self):

    def instance (self):
        pygame.init()
        gameDisplay = pygame.display.set_mode((self.Map.size*20,self.Map.size*20 ))
        clock = pygame.time.Clock()
        crashed = False

        while not crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                print(event)

            pygame.display.update()
            clock.tick(60)



game = game()
game.instance()

