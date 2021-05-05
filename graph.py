import pygame
import PATH


class dysplay():
    def __init__(self):
        self.floor = pygame.image.load(PATH.
                                       floor
                                       ).convert()
        self.McGiver = pygame.image.load(PATH.McGiversrc).convert()
        self.Mechant = pygame.image.load(PATH.Mechantsrc).convert()
        self.Wall = pygame.image.load(PATH.Wallsrc).convert()
        self.seringue = pygame.image.load(PATH.seringuesrc).convert()
        self.tube = pygame.image.load(PATH.tubesrc).convert()
        self.ether = pygame.image.load(PATH.ethersrc).convert()
