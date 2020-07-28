import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame

pygame.init()

<<<<<<< HEAD
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

=======
Screen = pygame.display.set_mode((300, 300))

Continue = True

while Continue:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            Continue = False
pygame.quit()
>>>>>>> parent of 3ff2f66... Dernier Pygame 23/04/20

McGiver = 'MacGyver.png'
Mechant='Gardien.png'
Wall='structures.png'
seringue='seringue.png'
