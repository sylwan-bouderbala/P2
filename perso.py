import os

class Perso(object):
    def __init__(self,positon):
        self.position = positon
        self.objectnumber=0

    def addobject(self):
        self.objectnumber+=1
perso = Perso([0])
print(perso.objectnumber)
perso.addobject()
print(perso.objectnumber)

