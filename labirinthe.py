import os 


class Lab(object):
	def __init__(self,reglage,size=15):
		self.format={}
		self.reglage=reglage.read()
		self.size=size
	def initialisermap(self,size=15):
		positions=[]
		for i in range(15):
			for j in range(15):
				positions.append((i,j))

		self.reglage
		liste2=[]
		for caracters in self.reglage:
			if caracters != "\n":
			    liste2.append(caracters+" ")
			else :
				pass 
		print(liste2)
             
		for x in range(size*size):
			self.format[positions[x]]=liste2[x]
		print(self.format)

	def affichermap(self,size=15):
		for i in range(size):
			listeaffichage=""
			print(listeaffichage)
			for j in range(size):
				listeaffichage= listeaffichage + self.format[(i,j)] 
			print(listeaffichage)


reglage=open("reglage.txt","r")			
Lab=Lab(reglage)
Lab.initialisermap()
Lab.affichermap()