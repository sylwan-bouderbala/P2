import os
import perso

class Lab(object):
    def __init__(self):
        self.attributes()
        self.initialisation()

    def move(self, inputage, nbrobject):
        if nbrobject!=4:
            if inputage==1:
                if self.mcgiver[1] -1 != '.':
                    print('c\'est un mur')



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
        print(self.format)

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
        if j == 'x':
            self.mur.append((i, x))
        if j == '1':
            self.mcgiver = perso.Perso((i,x))
        if j == '2':
            self.mechant = (i, x)

    def attributes(self):
        self.mur = []
        self.listevide = []
        self.mcgiver = []
        self.mechant = ()
        self.size = 0
        self.format = {}
    def mouvements(self,inputage):
        if inputage == 1:
            if (self.mcgiver[1] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.)] = '.'
                self.mcgiver[1] -= 1
                self.format[tuple(self.mcgiver)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 2:
            if (self.mcgiver[0] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver[0] += 1
                self.format[tuple(self.mcgiver)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 3:
            if (self.mcgiver[1] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver)] = '.'
                self.mcgiver[1] += 1
                self.format[tuple(self.mcgiver)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 5:
            if (self.mcgiver[0] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver)] = '.'
                self.mcgiver[0] -= 1
                self.format[tuple(self.mcgiver)] = '1'
            else:
                print('erreur hors du tableau')
        else:
            print("selectionner un mouvement")


Lab = Lab()
Lab.Afficher()
Lab.move(4, 0)
Lab.Afficher()
