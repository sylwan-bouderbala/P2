import pygame

class dysplay():
    def __init__(self):
        McGiversrc = 'images/MacGyver.png'
        Mechantsrc='images/Gardien.png'
        floor='images/floor-tiles-20x20.png'
        Wallsrc='images/structures.png'
        seringuesrc='images/seringue.png'
        tubesrc="images/tube_plastique.png"
        ethersrc="images/ether.png"

        self.floor=pygame.image.load(floor).convert()
        self.McGiver=pygame.image.load(McGiversrc).convert()
        self.Mechant=pygame.image.load(Mechantsrc).convert()
        self.Wall=pygame.image.load(Wallsrc).convert()
        self.seringue=pygame.image.load(seringuesrc).convert()
        self.tube=pygame.image.load(tubesrc).convert()
        self.ether=pygame.image.load(ethersrc).convert()



