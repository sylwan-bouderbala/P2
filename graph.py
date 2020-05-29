import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame


class dysplay():
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((600, 600))
        McGiversrc = 'images/MacGyver.png'
        Mechantsrc='images/Gardien.png'
        Wallsrc='images/structures.png'
        seringuesrc='images/seringue.png'
        tubesrc="images/tube_plastique.png"
        ethersrc="images/ether.png"


        self.McGiver=pygame.image.load(McGiversrc).convert()
        self.Mechant=pygame.image.load(Mechantsrc).convert()
        self.Wall=pygame.image.load(Wallsrc).convert()
        self.seringue=pygame.image.load(seringuesrc).convert()
        self.tube=pygame.image.load(tubesrc).convert()
        self.ether=pygame.image.load(ethersrc).convert()


