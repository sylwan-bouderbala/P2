import os 

class Lab(object):
	def __init__(self):
		attributes()
		initialisation()
	def move():
		pass
	def initsize(self):
		with open('lab.txt','r') as po :
			for i in po.read():
				if i=="\n":
					self.size=1+self.size
	def initialisation(self):
		with open('lab.txt','r') as lab:
			for i in range(self.size):
				x=0
				for j in lab.readline():
						if j != '\n':
							self.format[(i,x)]=j
							x=x+1
							sub_init(i,j,x)
						else:
							pass
		print(self.format)
    def affichage(tab,size):
		listeaffichage=""
		for i in range(size):
			for j in range(size):
				if j != size-1  :
				  listeaffichage= listeaffichage+tab[(i,j)]+" "
				else:
					listeaffichage=listeaffichage +tab[(i,j)]+ "\n"
		print(listeaffichage)

	def sub_init(i,j,x):
		if j=='.':
			self.listevide.append((i,x))
		if j=='x':
			self.mur.append((i,x))
		if j=='1':
			self.gentil_position=(i,x)
		if j=='2':
			self.mechant=(i,x)
    def attributes(self):
		self.mur=[]
		self.listevide=[]
		self.gentil_position=()
		self.mechant=(
		self.size= 0 #à remplacer par 0
		self.format={}