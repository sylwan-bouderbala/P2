from perso import Perso
import random


class Lab(object):

    def __init__(self):
        self.attributes()

        self.initialisation()
        self.addobject()

    def move(self, inputage):

        index_change = self.indexchange(inputage)
        try:
            if self.format[tuple(index_change)] == '.':
                self.Movements(inputage)
            if self.format[tuple(index_change)] == 'x':
                print('c"est un mur')
            if self.format[tuple(index_change)] == '2':
                if self.mcgiver.objectnumber >= 3:
                    self.Movements(inputage)
                else:
                    print('il te faut 4 objet')
            if tuple(index_change) in self.objet:
                print('ok')
                self.Movements(inputage)
                self.mcgiver.Addobject()
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
                        self.format[(x, i)] = j
                        self.sub_init(i, j, x)
                        x = x + 1
                    else:
                        pass

    def addobject(self):
        i, j, k, z = False, False, False, False
        while not i:
            x = random.randint(0, 14)
            y = random.randint(0, 14)
            if self.format[x, y] == '.':
                self.format[x, y] = '6'

                self.objet.append((x, y))
                i = True
        while not j:
            x = random.randint(0, 14)
            y = random.randint(0, 14)

            if self.format[x, y] == '.':
                self.format[x, y] = '5'

                self.objet.append((x, y))
                j = True
        while not k:
            x = random.randint(0, 14)
            y = random.randint(0, 14)

            if self.format[x, y] == '.':
                self.format[x, y] = '4'

                self.objet.append((x, y))
                k = True
        while not z:
            x = random.randint(0, 14)
            y = random.randint(0, 14)

            if self.format[x, y] == '.':
                self.format[x, y] = '3'

                self.objet.append((x, y))
                z = True

    def sub_init(self, i, j, x):
        if j == '.':
            self.listevide.append((x, i))
        elif j == 'x':
            self.mur.append((x, i))
        elif j == '1':
            self.mcgiver = Perso([x, i])
        elif j == '2':
            self.mechant = (x, i)

    def attributes(self):
        self.mur = []
        self.objet = []
        self.listevide = []
        self.mcgiver = []
        self.mechant = ()
        self.size = 0
        self.format = {}

    def Movements(self, inputage):
        if inputage == 1:
            if (self.mcgiver.position[1] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] = self.mcgiver.position[1] - 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 2:
            if (self.mcgiver.position[0] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] = self.mcgiver.position[0] + 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 3:
            if (self.mcgiver.position[1] + 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[1] = self.mcgiver.position[1] + 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        if inputage == 5:
            if (self.mcgiver.position[0] - 1) <= self.size - 1:
                self.format[tuple(self.mcgiver.position)] = '.'
                self.mcgiver.position[0] = self.mcgiver.position[0] - 1
                self.format[tuple(self.mcgiver.position)] = '1'
            else:
                print('erreur hors du tableau')
        else:
            print("selectionner un mouvement")

    #
    # def object(self,inputage):
    #     if self.format[(self.indexchange(inputage))] in [3,4,5]:

    def indexchange(self, inputage) -> object:
        if inputage == 1:
            return [self.mcgiver.position[0], self.mcgiver.position[1] - 1]
        if inputage == 2:
            return [self.mcgiver.position[0] + 1, self.mcgiver.position[1]]
        if inputage == 3:
            return[self.mcgiver.position[0], self.mcgiver.position[1] + 1]
        if inputage == 5:
            return [self.mcgiver.position[0] - 1, self.mcgiver.position[1]]

    def win(self):
        if tuple(self.mcgiver.position) == self.mechant:
            return False
        else:
            return True


labir = Lab()
