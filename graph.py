import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame

pygame.init()

Screen = pygame.display.set_mode((300, 300))

Continue = True

while Continue:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            Continue = False
pygame.quit()

McGiver = 'MacGyver.png'
Mechant='Gardien.png'
Wall='structures.png'
seringue='seringue.png'
