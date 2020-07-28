import pygame
from perso import Perso
from graph import dysplay

class Lab(object):
    def __init__(self):
        self.attributes()
        self.initialisation()
        pygame.init()
        pygame.display.set_mode((600,600))

    def move(self, inputage):
        Indexchange = self.indexchange(inputage)
        try:
            if self.format[tuple(Indexchange)]=='.':
                self.Movements(inputage)
            if self.format[tuple(Indexchange)]=='x':
                print('c"est un mur')
            if self.format[tuple(Indexchange)]=='2':
                if self.mcgiver.objectnumber==4:
                    self.Movements(inputage)
                else :
                    print('il te faut 4 objet')
            if tuple(Indexchange) in self.objet:
                self.Movements(inputage)
                self.mcgiver.addobject()

        except:
            print("c'est hors du tableau ")

    def initsize(self):
        with open('lab.txt', 'r') as po:
            for i in po.read():
                if i == "\n":
                    self.size = 1 + self.size

    def initialisation(self):
        self.initsize()
        with open('lab.txt', 'r') as lab:
            for i in range(self.size):
                x = 0
                for j in lab.readline():
                    if j != '\n':
                        self.format[(i, x)] = j
                        self.sub_init(i, j, x)
                        x = x + 1
                    else:
                        pass

    def Display(self):
        # ListeAffichage = ""
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if j != self.size - 1:
        #             ListeAffichage = ListeAffichage + self.format[(i, j)]
        #         else:
        #             ListeAffichage = ListeAffichage + self.format[(i, j)]
        # print(len(ListeAffichage))

        pygame.init()
        ecran=pygame.display.set_mode((300,300))
        image= dysplay()
        for i in range(self.size):
            for j in range(self.size):
                if self.format[(j,i)]=='.':
                    ecran.blit(image.floor,(i*20,j*20))
                if self.format[(j,i)]=='x':
                    ecran.blit(image.Wall,(i*20,j*20))
                if self.format[(j,i)]=='1':
                    ecran.blit(image.McGiver,(i*20,j*20))
                if self.format[(j,i)]=='2':
                    ecran.blit(image.Mechant,(i*20,j*20))
                if self.format[(j,i)]=='3':
                    ecran.blit(image.ether,(i*20,j*20))
                if self.format[(j,i)]=='4':
                    ecran.blit(image.seringue,(i*20,j*20))
                if self.format[(j,i)]=='5':
                    ecran.blit(image.tube,(i*20,j*20))

        pygame.display.flip()
        Continuer = True
        while Continuer:
             for events in pygame.event.get():
                 if events.type == pygame.QUIT:
                     Continuer = False
                     print(events)
        pygame.display.flip()

    def sub_init(self, i, j, x):
        if j == '.':
            self.listevide.append((i, x))
        elif j == 'x':
            self.mur.append((i, x))
        elif j == '1':
            self.mcgiver = Perso([i, x])
        elif j == '2':
            self.mechant = (i, x)
        else :
            self.objet.append((i,x))

    def attributes(self):
        self.mur = []
        self.objet=[]
        self.listevide = []
        self.mcgiver = []
        self.mechant = ()
        self.size = 0
        self.format = {}

    def Movements(self, ):
        pygame.init()
        if pygame.event.get() == pygame.K_LEFT:
            if (self.mcgiver.position[1] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] =self.mcgiver.position[1]-1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if  pygame.K_DOWN:
            if (self.mcgiver.position[0] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] =self.mcgiver.position[0] + 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if  pygame.K_UP:
            if (self.mcgiver.position[1] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] = self.mcgiver.position[1] + 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if pygame.K_RIGHT:
            if (self.mcgiver.position[0] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] =self.mcgiver.position[0]-1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        else:
            print("selectionner un mouvement")

    def indexchange(self,inputage):
        if inputage == 1:
            return [self.mcgiver.position[0],self.mcgiver.position[1]-1]
        if inputage ==2 :
            return [self.mcgiver.position[0]+1,self.mcgiver.position[1]]
        if inputage == 3:
            return [self.mcgiver.position[0],self.mcgiver.position[1]+1]
        if inputage== 5:
            return [self.mcgiver.position[0]-1,self.mcgiver.position[1]]

    def win(self):
        if tuple(self.mcgiver.position)==self.mechant:
            return False
        else:
            return True

