import os
import labirinthe
import perso 

Lab = labirinthe.Lab()
Lab.initialisation()
labirinthe.affichage(Lab.format,15)
pi = perso.Perso(Lab.mur, Lab.listevide, Lab.mcgiver, Lab.mechan)
pi.move()
labirinthe.affichage(Lab.format,15)