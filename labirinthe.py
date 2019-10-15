import os 


class Lab(object):
	def __init__(self,reglage,size=15):
		self.format={}
		self.reglage=reglage.read()
		self.size=size
	def initialisermap(self,size=15):
		positions=[]
		for i in range(1,15):
			for j in range(1,15):
				positions.append((i,j))

		self.reglage
		liste2=[]
		for caracters in self.reglage:
			if caracters != "\n":
			    liste2.append(caracters)
			else :
				pass 

		for x in range(size**2):
			self.format[positions[x]]=liste2[x]
	def affichermap(self,size=15):
		for i in range(size):
			listeaffichage=""
			print(listeaffichage)
			for j in range(size):
				listeaffichage= self.format[(i,j)] + listeaffichage
			print(listeaffichage)


reglage=open("reglage.txt","r")			
Lab=Lab(reglage)
Lab.initialisermap()
Lab.affichermap()