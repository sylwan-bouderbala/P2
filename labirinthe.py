import os 

class Lab(object):
	def __init__(self, size=15):
		self.size = size
		self.format={}
	def initialisation(self,size=15):
		with open('lab.txt','r') as lab:
			for i in range(size):
				x=0
				for j in lab.readline():
						if j != '\n':
							self.format[(i,x)]=j
							x=x+1
						else:
							pass
		print(self.format)
	def affichage(self,size=15):
		listeaffichage=""
		for i in range(size):
			for j in range(size):
				if j != 14  :
				  listeaffichage= listeaffichage+self.format[(i,j)]+" "
				else:
					listeaffichage=listeaffichage +self.format[(i,j)]+ "\n"
		print(listeaffichage)

lab=Lab()
lab.initialisation()
lab.affichage()