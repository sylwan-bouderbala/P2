from labirinthe import Lab
# import pygame
from perso import Perso
from graph import dysplay

class game(object):
    def __init__ (self):
        self.Map = Lab()
        self.player = Perso()
    def wininggame (self):
        return false
    def instance (self):
        pygame.init()
        gameDisplay = pygame.display.set_mode((self.Map.size*20,self.Map.size*20 ))


game = game()

print(game.Map)