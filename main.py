import os
import labirinthe as Lab
import perso as per

tab= Lab.Lab()
tab.init()
tab.affichage()
gentil = per.Perso()
gentil.id(tab.format)
gentil.positions(tab.format)