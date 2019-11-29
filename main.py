import os
import labirinthe as Lab
import perso 

tab= Lab.Lab()
tab.init()
tab.affichage()
tag_gentil='1'
perso=perso.Perso()
perso.positionner(tab.format,tag_gentil)

