from labirinthe import Lab

<<<<<<< HEAD















# # +
# def inputager():
#
#     if pygame.K_UP:
#         return 5
#     else :
#         return 0
# labyrinthe = Lab()
# continuer=True
# pygame.init()
# while continuer:
#
#     if labyrinthe.win():
#         continuer==False
#     initt=inputager()
#     labyrinthe.move(initt)
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             continuer=False
#         if labyrinthe.win()==True:
#             continuer==False
=======
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
>>>>>>> parent of 3ff2f66... Dernier Pygame 23/04/20
