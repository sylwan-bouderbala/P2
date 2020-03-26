import os
from perso import Perso

class Lab(object):
    def __init__(self):
        self.attributes()
        self.initialisation()

    def move(self, inputage):
        try:
            indexchange=self.indexchange(inputage)
            if self.format[tuple(indexchange)]=='.':
                self.mouvements(inputage)
            elif self.format[tuple(indexchange)]=='x':
                print('c"est un mur')
            elif self.format[tuple(indexchange)]=='2':
                if self.mcgiver.objectnumber==4:
                    self.mouvements(inputage)
                else :
                    print('il te faut 4 objet')
            elif self.format[tuple(indexchange)] in self.objet:
                self.mouvements(inputage)
                self.mcgiver.addobject()
        except KeyError:
            print('hors du tableau')


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

    def Afficher(self):
        listeaffichage = ""
        for i in range(self.size):
            for j in range(self.size):
                if j != self.size - 1:
                    listeaffichage = listeaffichage + self.format[(i, j)] + " "
                else:
                    listeaffichage = listeaffichage + self.format[(i, j)] + "\n"
        print(listeaffichage)

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

    def mouvements(self,inputage):
        if inputage == 1:
            if (self.mcgiver.position[1] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] -= 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 2:
            if (self.mcgiver.position[0] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] += 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 3:
            if (self.mcgiver.position[1] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] += 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 5:
            if (self.mcgiver.position[0] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] -= 1
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
    def win (self):
        return True
        if self.mcgiver.position==self.mechant:
            return False
