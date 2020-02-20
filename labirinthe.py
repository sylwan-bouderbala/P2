import os 

class Lab(object):
	def __init__(self):
		self.attributes()
		self.initialisation()
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
							self.sub_init(i,j,x)
						else:
							pass
		print(self.format)
	def affichage(self):
		listeaffichage=""
		for i in range(self.size):
			for j in range(self.size):
				if j != self.size-1:
				  listeaffichage= listeaffichage+self.format[(i,j)]+" "
				else:
				  listeaffichage=listeaffichage +self.format[(i,j)] + "\n"
		print(listeaffichage)

	def sub_init(self,i,j,x):
		if j=='.':
			self.listevide.append((i,x))
		if j=='x':
			self.mur.append((i,x))
		if j=='1':
			self.gentil_position=[i,x]
		if j=='2':
			self.mechant=(i,x)
	def attributes(self):
		self.mur=[]
		self.listevide=[]
		self.gentil_position=[]
		self.mechant=()
		self.size=0
		self.format={}

Lab=Lab()
