from labirinthe import Lab
import pygame
from perso import Perso
from graph import dysplay

class game(object):
    def __init__ (self):
        display_width = 15*20
        display_height = 15*20

        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('A bit Racey')
        pygame.init()
        self.Map = Lab()
        self.player = Perso(self.Map.mcgiver)
        self.graphisme= dysplay()


        clock = pygame.time.Clock()
        crashed = False

    def print(self):
        for i in range(self.Map.size):
            for j in range(self.Map.size):
                if self.Map.format[(i, j)] == "1":
                    self.gameDisplay.blit(self.graphisme.McGiver, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == ".":
                    self.gameDisplay.blit(self.graphisme.floor, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == "2":
                    self.gameDisplay.blit(self.graphisme.Mechant, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == "x":
                    self.gameDisplay.blit(self.graphisme.Wall, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == "3":
                    self.gameDisplay.blit(self.graphisme.tube, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == "4":
                    self.gameDisplay.blit(self.graphisme.ether, (i * 20, j * 20))
                elif self.Map.format[(i, j)] == "5":
                    self.gameDisplay.blit(self.graphisme.seringue, (i * 20, j * 20))
                else:
                    self.gameDisplay.blit(self.graphisme.floor, (i * 20, j * 20))

    def wininggame (self):
        return false


    def instance (self):
        pygame.init()

        display_width = self.Map.size*20
        display_height = self.Map.size*20

        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('A bit Racey')

        clock = pygame.time.Clock()
        crashed = False

        while not crashed and self.Map.win():
            self.print()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed =True
                    print(crashed)
                elif event.type == pygame.KEYDOWN:
                    print(pygame.KEYDOWN)

                    if event.key == pygame.K_DOWN:
                        self.Map.move(3)
                    if event.key == pygame.K_LEFT:
                        self.Map.move(5)
                    if event.key == pygame.K_RIGHT:
                        self.Map.move(2)
                    if event.key == pygame.K_UP:
                        self.Map.move(1)
                    print(pygame.K_LEFT)
                    print(event.key)
            pygame.display.flip()
            pygame.display.update()
            clock.tick(60)

        pygame.quit()
        quit()


game = game()
game.instance()




