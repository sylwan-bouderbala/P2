from labirinthe import Lab
import pygame
from graph import dysplay

class game(object):
    def __init__(self):
        self.inputpossible = ['1', '2', '3', '5']
        self.display=Lab()
        self.win= self.display.win()
        self.Maingame()
    def Maingame(self):
        self.display.Display()
        while self.win == True:
            Inputage = input("entrez votre input : ")
            if Inputage not in self.inputpossible:
                print('pas un input possible')
            else:
                Inputage = int(Inputage)
                self.display.move(Inputage)
                self.display.Display()
        print('c\'est gagner')

pygame.init()
ecran = pygame.display.set_mode((600, 600))
McGiversrc = 'images/MacGyver.png'
Mechantsrc = 'images/Gardien.png'
Wallsrc = 'images/structures.png'
seringuesrc = 'images/seringue.png'
tubesrc = "images/tube_plastique.png"
ethersrc = "images/ether.png"

McGiver = pygame.image.load(McGiversrc).convert()
Mechant = pygame.image.load(Mechantsrc).convert()
Wall = pygame.image.load(Wallsrc).convert()
seringue = pygame.image.load(seringuesrc).convert()
tube = pygame.image.load(tubesrc).convert()
ether = pygame.image.load(ethersrc).convert()
ecran = pygame.display.set_mode((600, 600))

continuer = True
for i in range(15):
    for j in range(15):
        ecran.blit(McGiver, (i,j))
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
pygame.quit()