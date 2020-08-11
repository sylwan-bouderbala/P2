# Simple pygame program

# Import and initialize the pygame library
import pygame
from graph import dysplay
from labirinthe import Lab
map=Lab()
pygame.init()
print(map.format)

i1 = 20


def blit(x,   i1):
    if x == '.':
        screen.blit(d.floor, (i[1] * i1, i[0] * i1))
    if x == 'x':
        screen.blit(d.Wall, (i[1] * i1, i[0] * i1))
    if x == '2':
        screen.blit(d.Mechant, (i[1] * i1, i[0] * i1))
    if x == '1':
        screen.blit(d.McGiver, (i[1] * i1, i[0] * i1))
    else:
        if x == '3':
            screen.blit(d.seringue, (i[1] * i1, i[0] * i1))
        if x == '4':
            screen.blit(d.tube, (i[1] * i1, i[0] * i1))
        if x == '5':
            screen.blit(d.ether, (i[1] * i1, i[0] * i1))


screen = pygame.display.set_mode([15*i1, 15*i1])
running = True
while running:
    d = dysplay()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                map.move(5)
                print(2)
            if event.key == pygame.K_RIGHT:
                map.move(3)
                print(3)
    # Fill the background with white
    for i in map.format.keys():
        blit(map.format[i], i1)

    # Draw a solid blue circle in the center
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()