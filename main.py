from labirinthe import Lab

inputpossible=['1','2','3','5']
affichage = Lab()
gagner=affichage.win()
affichage.Afficher()
while 1==1:
    inputage=input("entrez votre input : ")
    if inputage not in inputpossible:
        print('pas un input possible')
    else:
        inputage=int(inputage)
        affichage.move(inputage)
        affichage.Afficher()
print('c\est gaggner')