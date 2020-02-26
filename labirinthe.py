import os

import HEAD as HEAD

import perso

class Lab(object):


	def __init__(self):
		self.attributes()
		self.initialisation()
	def move():
		pass
	def move(self,direction):
		if direction == 1 :
			try :
				if self.gentil_position in self.listevide :
				   pass
	def initsize(self):
		with open('lab.txt','r') as po :
			for i in po.read():
				if i=="\n":
					self.size=1+self.size
	def initialisation(self):
		self.initsize()
		with open('lab.txt','r') as lab:
			for i in range(self.size):
				x=0
				for j in lab.readline():
						if j != '\n':
							self.format[(i,x)]=j
							x=x+1
							
							if j=='.' :
								self.listevide.append((i,x))
							if j=='x':
								self.mur.append((i,x))
		                    if j=='1':
								self.gentil_position=perso.perso([i,x])
		                    if j=='2':
								self.mechant=(i,x)
						else:
							pass
		print(self.format)
	
	def affichage(tab,size):

=======
							self.sub_init(i,j,x)
						else:
							pass
		print(self.format)
	def affichage(self):
>>>>>>> 94cf410193dcbe0822ce1c037338143643bef29e
		listeaffichage=""
		for i in range(self.size):
			for j in range(self.size):
				if j != self.size-1:
				  listeaffichage= listeaffichage+self.format[(i,j)]+" "
				else:
				  listeaffichage=listeaffichage +self.format[(i,j)] + "\n"
		print(listeaffichage)

<<<<<<< HEAD

=======
	def sub_init(self,i,j,x):
		if j=='.':
			self.listevide.append((i,x))
		if j=='x':
			self.mur.append((i,x))
		if j=='1':
			self.gentil_position=[i,x]
		if j=='2':
			self.mechant=(i,x)
>>>>>>> 94cf410193dcbe0822ce1c037338143643bef29e
	def attributes(self):
		self.mur=[]
		self.listevide=[]
		self.gentil_position=[]
		self.mechant=()
<<<<<<< HEAD
		self.size = 0
		self.format={}
Lab = Lab()
=======
		self.size=0
		self.format={}

Lab=Lab()
>>>>>>> 94cf410193dcbe0822ce1c037338143643bef29e
