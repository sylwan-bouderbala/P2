from labirinthe import Lab

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


Game = game()
