from labirinthe import Lab
import pygame
from perso import Perso
from graph import dysplay


class game(object):
    def __init__(self):
        display_width = 15*20
        display_height = 16*20

        self.gameDisplay = pygame.display.set_mode(
            (display_width, display_height)
        )
        pygame.display.set_caption('A bit Racey')
        pygame.init()
        self.Map = Lab()
        self.player = Perso(self.Map.mcgiver)
        self.graphisme = dysplay()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 12)

    def textobj(self, number, text):
        textsurface = self.myfont.render( text+str(number), False, (255, 0, 0))
        return textsurface

    def print(self):
        if self.Map.win():
            for i in range(self.Map.size):
                for j in range(self.Map.size):
                    if self.Map.format[(i, j)] == "1":
                        self.gameDisplay.blit(self.graphisme.McGiver,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == ".":
                        self.gameDisplay.blit(self.graphisme.floor,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == "2":
                        self.gameDisplay.blit(self.graphisme.Mechant,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == "x":
                        self.gameDisplay.blit(self.graphisme.Wall,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == "3":
                        self.gameDisplay.blit(self.graphisme.tube,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == "4":
                        self.gameDisplay.blit(self.graphisme.ether,
                                              (i * 20, j * 20)
                                              )
                    elif self.Map.format[(i, j)] == "5":
                        self.gameDisplay.blit(self.graphisme.seringue,
                                              (i * 20, j * 20)
                                              )
                    else:
                        self.gameDisplay.blit(self.graphisme.floor,
                                              (i * 20, j * 20)
                                              )
            self.gameDisplay.blit(self.textobj(self.Map.mcgiver.objectnumber,
                                               'nombre d\'objets'),
                                  (0*20,15*20)
                                  )
            pygame.display.flip()


    def instance(self):
        pygame.init()
        pygame.display.set_caption('McGiver Labirinthe')

        clock = pygame.time.Clock()
        crashed = False

        while not crashed :
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    crashed = True
                if self.Map.win()==False :
                    self.gameDisplay.fill((0,0,0))

                    winsurface = self.myfont.render('you win', False, (255, 0, 0))

                    self.gameDisplay.blit(winsurface,
                                      (7 * 20, 7 * 20))
                    pygame.display.flip()

                else :
                    self.print()

                    if event.type == pygame.QUIT:
                        crashed = True
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



        pygame.quit()
        quit()


game = game()
game.instance()
