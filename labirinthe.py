import os 

class Lab(object):
	def __init__(self, size=15):
		self.size = size
		self.format={}
	def initialisation(self,size=15):
		self.mur=[]
		self.listevide=[]
		self.gentil_position=()
		self.mechant=()
		with open('lab.txt','r') as lab:
			for i in range(size):
				x=0
				for j in lab.readline():
						if j != '\n':
							self.format[(i,x)]=j
							x=x+1
							if j=='.':
								self.listevide.append((i,x))
							if j=='x':
								self.mur.append((i,x))
							if j=='1':
								self.gentil_position=(i,x)
							if j=='2':
								self.mechant=(i,x)
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
